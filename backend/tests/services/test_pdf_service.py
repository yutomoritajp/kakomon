"""
PdfServiceのテスト。令和7年/午前Ⅰ/問題PDFのみを対象に、一通りの機能が動作することを確認する。
他の組み合わせはtest_create_quiz.pyとconfirm_question_pdf.pyの目視フローでカバーされるため扱わない。
"""

from pathlib import Path

import pytest

from constants.pdf_type import PdfType
from constants.period import Period
from constants.section import Section
from services.pdf_service import PdfService
from values.page_range import PageRange

## 令和7年/午前Ⅰ/問題PDFのページ数は20ページである。
MAX_PAGE_COUNT = 20


@pytest.fixture(scope="module")
def pdf_service() -> PdfService:
    return PdfService(Period.R7, Section.AM1, PdfType.QUESTION)


def test_create_path(pdf_service: PdfService):
    """
    正しいパスが作成されることを確認するテスト。
    """
    assert pdf_service._create_path() == Path("past_exams/r7/am1/question.pdf")


def test_get_target_doc_with_max_page(pdf_service: PdfService):
    """
    PageRange の end が実際のページ数と同じ場合、正常値を返すこと。
    """
    assert pdf_service._get_target_doc(PageRange(1, MAX_PAGE_COUNT)).page_count == 20


def test_get_target_doc_with_out_of_range_end(pdf_service: PdfService):
    """
    PageRange の end が実際のページ数より多い場合、例外を出すこと。
    """
    with pytest.raises(ValueError) as e:
        pdf_service._get_target_doc(PageRange(1, MAX_PAGE_COUNT + 1))
    assert (
        str(e.value) == "終了ページの値がページ数を超えています。end=21, page_count=20"
    )
