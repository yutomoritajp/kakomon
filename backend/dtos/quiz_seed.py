from pydantic import BaseModel

class QuizSeed(BaseModel):
    number: int
    content: str
    has_image: bool
    correct_option: str