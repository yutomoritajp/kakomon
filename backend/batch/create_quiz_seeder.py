import argparse
from services.values.page_range import PageRange
from services.constants.period import Period
from services.constants.section import Section
from services.quiz_seeder_service import create_quiz_seeder, _get_collect_options
from batch.setup_logging import setup_logging

def main() -> None:
    setup_logging()
    message = _get_collect_options(Period.R7, Section.AM1)
    print("レスポンス↓")
    print(message)
    
    
if __name__ == "__main__":
    main()
