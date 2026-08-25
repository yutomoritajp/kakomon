import argparse
from values.page_range import PageRange
from constants.period import Period
from constants.section import Section
from usecases.create_quiz import 
from scripts.setup_logging import setup_logging

def main() -> None:
    setup_logging()
    message = create_quiz_seeder(Period.R7, Section.AM1, PageRange(1, 3))
    print("レスポンス↓")
    print(message)
    
    
if __name__ == "__main__":
    main()
