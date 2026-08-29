from pydantic import BaseModel

from constants.quiz_option import QuizOption


class QuizInput(BaseModel):
    exam_id: int
    quiz_number: int
    quiz_content: str
    correct_option: QuizOption
    status: str