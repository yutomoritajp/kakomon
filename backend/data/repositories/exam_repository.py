from sqlmodel import Session, select

from constants.period import Period
from constants.section import Section
from data.models import Exam


class ExamRepository:
    _session: Session

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_exam_id(self, period: Period, section: Section) -> Exam:
        """
        試験回と試験区分を受け取り、examを1件返す。
        0件または2件以上取得できる場合は例外を返す。
        """

        with self._session as session:
            statement = (
                select(Exam)
                .where(Exam.period_code == period.value)
                .where(Exam.section_code == section.value)
            )
            
            return session.exec(statement).one()
