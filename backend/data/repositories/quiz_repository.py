from sqlmodel import Session

from data.models import Quiz
from dtos.quiz_input import QuizInput


class QuizRepository:
    _session: Session

    def __init__(self, session: Session):
        self._session = session

    def add_all(self, quizzes: list[QuizInput]) -> None:

        with self._session as session:
            session.add_all(
                [
                    Quiz(
                        exam_id=quiz.exam_id,
                        number=quiz.quiz_number,
                        content=quiz.quiz_content,
                        correct_option=quiz.correct_option.number,
                        status=quiz.status,
                    )
                    for quiz in quizzes
                ]
            )
