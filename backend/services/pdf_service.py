import pymupdf
import os
from services.constants.pdf_type import PdfType
from services.constants.period import Period
from services.constants.section import Section

class PdfService():   
    _TEMP_DIR = "temp/"
    _period: Period
    _section: Section
    _pdf_type: PdfType
    _document: pymupdf.Document
         
    def __init__(self, period: Period, section: Section, pdf_type: PdfType) -> None:
        self._period = period
        self._section = section
        self._pdf_type = pdf_type
        self._document = pymupdf.open(self._create_pdf_path())
            
    def create_pdf(self, start:int, end:int) -> str:
        """
        指定された範囲のPdfを一時保存フォルダに作成する。
        
        Args:
            start: 最初のページ
            end: 最後のページ
        
        Returns:
            filename: 作成したpdfのファイル名
        """
        
        ## 対象pdfを取得
        pdf = self._get_target_pdf(start, end)
                
        ## 一時保存ディレクトリがない場合は作成する。
        os.makedirs(self._TEMP_DIR, exist_ok=True)
        
        filename = f"p{start}-p{end}_{self._period.value}_{self._section.value}_{self._pdf_type.value}"
        pdf.save(self._TEMP_DIR + filename)
        
        return filename
        
    
    def _get_target_pdf(self, start: int, end: int) -> pymupdf.Document:
        """
        指定された範囲のPdfを取得する。ページ番号は1始まり。
            
        Args:
            start: 最初のページ
            end: 最後のページ
        """
            
        if start > end:
            raise ValueError(f"開始ページは終了ページより小さい値を指定してください。start={start}, end={end}")
            
        if start < 1 or end > self._document.page_count:
            raise ValueError(f"開始ページまたは終了ページの値が不正です。start={start}, end={end}")
            
        new_pdf = pymupdf.open()
        new_pdf.insert_pdf(self._document, from_page=start - 1, to_page=end - 1)
            
        return new_pdf
        
    def _create_pdf_path(self) -> str:
        return f"past_exams/{self._period.value}/{self._section.value}/{self._pdf_type.value}"