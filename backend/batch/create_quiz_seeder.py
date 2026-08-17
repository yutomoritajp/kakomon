import argparse
from services.values.page_range import PageRange
from services.constants.period import Period
from services.constants.section import Section
from services.quiz_seeder_service import create_quiz_seeder
from batch.setup_logging import setup_logging

def main() -> None:
    setup_logging()
    message = create_quiz_seeder(Period.R7, Section.AM1, PageRange(4, 16))
    print("レスポンス↓")
    print(message)
    
    
if __name__ == "__main__":
    main()
