from sqlmodel import Session, select

from constants.period import Period
from constants.section import Section
from data.models import Exam


class ExamRepository:
    _session: Session

    def __init__(self, session: Session) -> None:
        self._session = session

    def get_exam_id(self, period: Period, section: Section) -> int:
        """
        試験回と試験区分を受け取り、exam_id(試験ID)を1件返す。
        0件または2件以上取得できる場合は例外を返す。
        """

        statement = (
            select(Exam)
            .where(Exam.period_code == period.value)
            .where(Exam.section_code == section.value)
        )

        exam_id = self._session.exec(statement).one().id

        if exam_id is None:
            raise ValueError(
                f"exam_idが取得できませんでした。period: {period}, section: {section}"
            )

        return exam_id
