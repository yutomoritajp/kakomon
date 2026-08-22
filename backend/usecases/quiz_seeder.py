from pydantic import BaseModel
from services.pdf_service import PdfService
from services.claude_api_service import ClaudeApiService
from values.page_range import PageRange
from constants.pdf_type import PdfType
from constants.period import Period
from constants.section import Section
import re


class QuizDto(BaseModel):
    number: int
    content: str
    image_flag: bool
    correct_option: str = ""

_SYSTEM_PROMPT = """
PDFから問題を読み取り、マークダウン形式に変換する。
numberにはその問題番号を入れる。
contentにはマークダウンに変換した文字列が入る。
簡単な表はそのままマークダウン形式として作成する。
複雑な表や、グラフや、図は'<<image>>'と置き換える。
image_flagは、content内に'<<image>>'と置き換えた個所がある場合のみTrueにする。
"""

def create_quiz_seeder(period: Period, section: Section, page_range: PageRange):
    """
    公式過去問題のPDFをもとに、Quizテーブルのシーディングファイルを作成します。
    """
    ## ClaudeAPIでPDFから問題文を生成する。
    question_pdf_service = PdfService(period, section, PdfType.QUESTION)   
    pdf_data = question_pdf_service.get_base64_data(page_range)
    
    claude_api_service = ClaudeApiService(max_tokens=10000)
    quiz_list = claude_api_service.create_parse_message([
        {
            "role": "user",
            "content": [
                {"type": "document",
                "source": {"type": "base64", "media_type": "application/pdf", "data": pdf_data}},
                {"type": "text", "text": "問題ごとに作成してください。"}
            ]
        }
    ],
    system = _SYSTEM_PROMPT,
    output_format = list[QuizDto]
    )

    ## 正解を取得
    correct_option_list = _get_correct_options(period, section)

    for quiz, correct_option in zip(quiz_list, correct_option_list):
        if quiz.number != correct_option.numbeer:
            ### 問題番号が一致しない場合は例外
            raise ValueError("問題番号が不一致です。")
        quiz.correct_option = correct_option.option

    return quiz_list
    
def _get_correct_options(period: Period, section: Section) -> list[dict[int, str]]:
    """
    公式過去問題の解答PDFから各問題の正解の選択肢を取得する。
    問題番号の昇順にソート。
    
    Returns:
        問題番号と正解の選択肢の辞書のリスト。("number": '問題番号', "option": '正解の選択肢')
        例：[{"number": 1, "option": 'イ'}, ... , {"number": 30, "option": 'ア'}]
    """
    answer_pdf_service = PdfService(period, section, PdfType.ANSWER)
    answer_text = answer_pdf_service.get_first_page_text()
    
    result = [{"number": int(number), "option": option} for number, option in re.findall(r"問\s*(\d+)\s+([アイウエ])", answer_text)]
    # 問題番号順に並べる。
    result.sort(key="number")
    
    if [number for number, _ in result] != list(range(1, section.quiz_count + 1)):
        ## 問題番号が1から30まで並んでいない場合は例外を出す。
        raise ValueError("PDFから抽出した解答選択肢リストの値が不正です。")
    
    return result
