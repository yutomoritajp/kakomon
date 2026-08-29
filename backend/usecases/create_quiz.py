import re

from pydantic import BaseModel
from sqlmodel import Session

from constants.pdf_type import PdfType
from constants.period import Period
from constants.quiz_option import QuizOption
from constants.quiz_status import QuizStatus
from constants.section import Section
from data.database import engine
from data.models import Quiz
from data.repositories.exam_repository import ExamRepository
from data.repositories.quiz_repository import QuizRepository
from services.claude_api_service import ClaudeApiService
from services.pdf_service import PdfService
from values.page_range import PageRange


class ParsedQuiz(BaseModel):
    number: int
    content: str
    has_image: bool


class ParsedQuizList(BaseModel):
    quizzes: list[ParsedQuiz]


_SYSTEM_PROMPT = """
PDFから問題を読み取り、マークダウン形式に変換する。
numberにはその問題番号を入れる。
contentにはマークダウンに変換した文字列が入る。
簡単な表はそのままマークダウン形式として作成する。
複雑な表や、グラフや、図は'<<image>>'と置き換える。
image_flagは、content内に'<<image>>'と置き換えた個所がある場合のみTrueにする。
"""


def create_quiz_data(period: Period, section: Section, page_range: PageRange) -> None:
    """
    公式過去問題のPDFをもとに、Quizテーブルのシーディングファイルを作成します。
    """
    ## マークダウン化した問題テキストを取得
    parsed_quiz_list = _get_parsed_quizzes(period, section, page_range)

    ## 正解の選択肢を取得
    correct_option_dict = _get_correct_options(period, section)

    ## 試験Id(exam_id)を取得して、同Sessionでクイズをクイズを作成
    with Session(engine) as session:
        exam_id = ExamRepository(session).get_exam_id(period, section)

        QuizRepository(session).add_all(
            [
                Quiz(
                    exam_id=exam_id,
                    number=quiz.number,
                    content=quiz.content,
                    correct_option=QuizOption(correct_option_dict[quiz.number]).code,
                    status=QuizStatus.DRAFT.value
                    if quiz.has_image
                    else QuizStatus.IN_REVIEW.value,
                )
                for quiz in parsed_quiz_list.quizzes
            ]
        )

        session.commit()


def _get_parsed_quizzes(
    period: Period, section: Section, page_range: PageRange
) -> ParsedQuizList:
    ## ClaudeAPIでPDFから問題文を生成する。
    pdf_service = PdfService(period, section, PdfType.QUESTION)
    pdf_data = pdf_service.get_base64_data(page_range)

    ## 有効なPDF情報が取得できていない場合は、例外を投げる。
    if not pdf_data:
        raise ValueError(f"有効なPDFの値が取得できませんでした。{pdf_data}")

    claude_api_service = ClaudeApiService()
    response = claude_api_service.create_parse_message(
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "document",
                        "source": {
                            "type": "base64",
                            "media_type": "application/pdf",
                            "data": pdf_data,
                        },
                    },
                    {"type": "text", "text": "問題ごとに作成してください。"},
                ],
            }
        ],
        output_format=ParsedQuizList,
        system=_SYSTEM_PROMPT,
    )

    if not response.parsed_output:
        raise ValueError(
            f"ClaudeAPIから値が取得できませんでした。{response.stop_reason}"
        )

    return response.parsed_output


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

    result = {number: "" for number in range(1, section.quiz_count + 1)}

    pdf_service = PdfService(period, section, PdfType.ANSWER)

    option_list = [
        (int(number), option)
        for number, option in re.findall(
            r"問\s*(\d+)\s+([アイウエ])", pdf_service.get_first_page_text()
        )
    ]

    for number, option in option_list:
        if number not in result:
            raise ValueError(f"予期しない問題番号が取得されました。number: {number}")
        if result[number] != "":
            raise ValueError(f"問題番号が2重に登録されました。number: {number}")
        result[number] = option

    ## 空文字が含まれている場合はErrorを出す。
    for key, value in result.items():
        if value == "":
            raise ValueError(f"{key}問目の問題が登録されていません。")

    return result
