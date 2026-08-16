from pydantic import BaseModel
from services.pdf_service import PdfService
from services.claude_api_service import ClaudeApiService
from services.values.page_range import PageRange
from services.constants.pdf_type import PdfType
from services.constants.period import Period
from services.constants.section import Section


class QuizSeederResponseDto(BaseModel):
    number: int
    content: str
    image_flag: bool

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
    question_pdf_service = PdfService(period, section, PdfType.QUESTION)
    
    pdf_data = question_pdf_service.get_base64_data(page_range)
    
    ## answer_pdf_service = PdfService(period, section, PdfType.ANSWER)
    
    claude_api_service = ClaudeApiService()
    response = claude_api_service.create_parse_message([
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
    output_format = list[QuizSeederResponseDto]
    )
    return response
    