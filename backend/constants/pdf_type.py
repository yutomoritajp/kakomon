from enum import Enum


class PdfType(Enum):
    """
    PDFのタイプ
    """

    ## 問題
    QUESTION = "question.pdf"

    ## 解答
    ANSWER = "answer.pdf"
