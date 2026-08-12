from fastapi import FastAPI
from services.pdf_service import PdfService
from services.constants.pdf_type import PdfType
from services.constants.period import Period
from services.constants.section import Section

app = FastAPI()

@app.get("/pdf")
def read_root():
    create_quiz = PdfService(Period.R7, Section.AM1, PdfType.QUESTION)
    return create_quiz.confirm_pdf(2, 10)