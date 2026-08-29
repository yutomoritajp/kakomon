from sqlmodel import Session

from data.models import Quiz

# from dtos.quiz_input import QuizInput →いったん使わなくなったので、、、消す予定だけど、もしレビューで指摘された時のため残しておく。


class QuizRepository:
    _session: Session

    def __init__(self, session: Session):
        self._session = session

    def add_all(self, quizzes: list[Quiz]) -> None:
        self._session.add_all(quizzes)
