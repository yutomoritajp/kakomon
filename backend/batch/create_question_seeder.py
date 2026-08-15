import argparse
from services.values.page_range import PageRange
from services.constants.pdf_type import PdfType
from services.constants.period import Period
from services.constants.section import Section
from services.quiz_seeder_service import create_quiz_seeder

def main() -> None:
    message = create_quiz_seeder(Period.R7, Section.AM1, PageRange(4, 16))
    print("レスポンス↓")
    print(message)
    
    
if __name__ == "__main__":
    main()