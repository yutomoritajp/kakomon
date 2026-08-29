import argparse

from constants.pdf_type import PdfType
from constants.period import Period
from constants.section import Section
from services.pdf_service import PdfService
from values.page_range import PageRange


def main() -> None:
    """
    試験年度、試験区分を選択し、問題のpdfを作成します。
    作成されたPDFは一時フォルダに作成されます。
    """

    parser = argparse.ArgumentParser(
        description="指定範囲のPDFを一時フォルダに作成します。"
    )
    parser.add_argument(
        "--period", dest="period", required=True, choices=[p.value for p in Period]
    )
    parser.add_argument(
        "--section", dest="section", required=True, choices=[s.value for s in Section]
    )
    parser.add_argument("--start", dest="start", required=True, type=int)
    parser.add_argument("--end", dest="end", required=True, type=int)

    args = parser.parse_args()

    pdf_service = PdfService(
        Period(args.period), Section(args.section), PdfType.QUESTION
    )
    filename = pdf_service.create_file_to_temp(PageRange(args.start, args.end))

    print(f"PDFを作成しました。{filename}")


if __name__ == "__main__":
    main()
