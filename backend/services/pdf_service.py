import base64
from pathlib import Path

import pymupdf

from constants.pdf_type import PdfType
from constants.period import Period
from constants.section import Section
from values.page_range import PageRange


class PdfService:
    _TEMP_DIR = Path("temp")
    _PAST_EXAM_DIR = Path("past_exams")
    _period: Period
    _section: Section
    _pdf_type: PdfType
    _document: pymupdf.Document

    def __init__(self, period: Period, section: Section, pdf_type: PdfType) -> None:
        self._period = period
        self._section = section
        self._pdf_type = pdf_type
        self._document = pymupdf.open(self._create_path())

    def create_file_to_temp(self, page_range: PageRange) -> str:
        """
        指定された範囲のPdfを一時保存フォルダに作成する。

        Returns:
            filename: 作成したpdfのファイル名
        """

        ## 対象pdfを取得
        pdf = self._get_target_doc(page_range)

        ## 一時保存ディレクトリがない場合は作成する。
        self._TEMP_DIR.mkdir(parents=True, exist_ok=True)

        pages = f"p{page_range.start}-p{page_range.end}"
        exam = f"{self._period.value}_{self._section.value}_{self._pdf_type.value}"
        filename = f"{pages}_{exam}"

        pdf.save(Path(self._TEMP_DIR, filename))

        return filename

    def get_base64_data(self, page_range: PageRange) -> str:
        """
        指定された範囲のPDFのバイナリデータを取得する。

        Returns:
            base64エンコードされたPDFデータ（文字列）
        """
        target_doc = self._get_target_doc(page_range)
        pdf_bytes = target_doc.tobytes()
        target_doc.close()

        return base64.standard_b64encode(pdf_bytes).decode("utf-8")

    def get_first_page_text(self, **kwargs) -> str:
        """
        最初のページのプレーンテキストを取得する。

        Args:
          kwargs: get_textに渡す引数（任意）
        """
        target_doc = self._get_target_doc(PageRange(1, 1))
        result = target_doc[0].get_text(**kwargs)
        target_doc.close()

        return str(result)

    def _get_target_doc(self, page_range: PageRange) -> pymupdf.Document:
        """
        指定された範囲のPdfを取得する。ページ番号は1始まり。
        """

        if page_range.end > self._document.page_count:
            raise ValueError(
                "終了ページの値がページ数を超えています。"
                f"end={page_range.end}, page_count={self._document.page_count}"
            )

        new_pdf = pymupdf.open()
        new_pdf.insert_pdf(
            self._document, from_page=page_range.start - 1, to_page=page_range.end - 1
        )

        return new_pdf

    def _create_path(self) -> Path:
        return Path(
            self._PAST_EXAM_DIR,
            self._period.value,
            self._section.value,
            self._pdf_type.value,
        )
