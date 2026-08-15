from services.pdf_service import PdfService
from services.claude_api_service import ClaudeApiService
from services.values.page_range import PageRange
from services.constants.pdf_type import PdfType
from services.constants.period import Period
from services.constants.section import Section

def create_quiz_seeder(period: Period, section: Section, page_range: PageRange):
    question_pdf_service = PdfService(period, section, PdfType.QUESTION)
    
    pdf_data = question_pdf_service.get_base64_data(page_range)
    
    ## answer_pdf_service = PdfService(period, section, PdfType.ANSWER)
    
    claude_api_service = ClaudeApiService()
    response = claude_api_service.create_message([
        {
            "role": "user",
            "content": [
                {"type": "document",
                "source": {"type": "base64", "media_type": "application/pdf", "data": pdf_data}},
                {"type": "text", "text": "このページで問1について以下のoutput_configのフォーマット通りに出力してください。numberは問題番号でcontentは問題文です。"}
            ]
        }
    ],
    {
        "format":{
            "type": "json_schema",
            "schema": {
                "type": "object",
                "properties": {
                    "number": {"type": "string"},
                    "content": {"type": "string"}
                },
                "required": ["number", "content"],
                "additionalProperties": False
            }
        }
    })
    return response
    