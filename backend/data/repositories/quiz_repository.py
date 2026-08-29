from sqlmodel import Session

from data.models import Quiz


class QuizRepository:
    _session: Session

    def __init__(self, session: Session):
        self._session = session

    def add_all(self, quizzes: list[Quiz]) -> None:
        self._session.add_all(quizzes)
