from pydantic import BaseModel
from services.pdf_service import PdfService
from services.claude_api_service import ClaudeApiService
from values.page_range import PageRange
from constants.pdf_type import PdfType
from constants.period import Period
from constants.section import Section
from dtos.quiz_seed import QuizSeed
import re


class ParsedQuiz(BaseModel):
    number: int
    content: str
    has_image: bool

_SYSTEM_PROMPT = """
PDFから問題を読み取り、マークダウン形式に変換する。
numberにはその問題番号を入れる。
contentにはマークダウンに変換した文字列が入る。
簡単な表はそのままマークダウン形式として作成する。
複雑な表や、グラフや、図は'<<image>>'と置き換える。
image_flagは、content内に'<<image>>'と置き換えた個所がある場合のみTrueにする。
"""

def create_quiz_data(period: Period, section: Section, page_range: PageRange) -> list[QuizSeed]:
    """
    公式過去問題のPDFをもとに、Quizテーブルのシーディングファイルを作成します。
    """
    ## ClaudeAPIでPDFから問題文を生成する。
    pdf_service = PdfService(period, section, PdfType.QUESTION)   
    pdf_data = pdf_service.get_base64_data(page_range)
    
    ## 有効な値が入っていない場合は、例外を出す。
    if not pdf_data:
        raise ValueError(f"有効なPDFの値が取得できませんでした。{pdf_data}")
    
    claude_api_service = ClaudeApiService(max_tokens=10000)
    parsed_list = claude_api_service.create_parse_message([
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
    output_format = list[ParsedQuiz]
    )
    
    option_dict = _get_correct_options(period, section)
    
    return _build_quiz_seeds(parsed_list, option_dict)
    
    
def _get_correct_options(period: Period, section: Section) -> dict[int, str]:
    """
    選択形式の問題（午前Ⅰ/午前Ⅱ）の正解の選択肢を取得する。
    
    Returns:
        問題番号と正解の選択肢のオブジェクト。
        { 1: "ア"} は1問目の正解がアであることを表す。
    """
    
    ## 選択式の問題を想定しているため、quiz_countが存在しないSectionの場合は例外を出す。
    if section.quiz_count is None:
        raise ValueError(f"予期しないSectionです。Section: {section.value}")
    
    result = { number: "" for number in range(1, section.quiz_count + 1)}
    
    pdf_service = PdfService(period, section, PdfType.ANSWER)
    
    option_list = [
        (int(number), option) 
            for number, option 
            in re.findall(r"問\s*(\d+)\s+([アイウエ])", pdf_service.get_first_page_text())
    ]
    
    for number, option in option_list:
        if number not in result:
            raise ValueError(f"予期しない問題番号が取得されました。number: {number}")
        if result[number] != '':
            raise ValueError(f"問題番号が2重に登録されました。number: {number}")
        result[number] = option
        
    ## 空文字が含まれている場合はErrorを出す。
    for key, value in result.items():
        if value == '':
            raise ValueError(f"{key}問目の問題が登録されていません。")
        
    return result

def _build_quiz_seeds(parsed_list: list[ParsedQuiz], option_dict: dict[int, str]) -> list[QuizSeed]:
    return [
        QuizSeed(**quiz.model_dump(), correct_option = option_dict[quiz.number])
        for quiz in parsed_list
    ]
