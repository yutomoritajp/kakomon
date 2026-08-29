from enum import Enum


class QuizOption(Enum):
    """
    Quizの選択肢
    """

    ## コード
    code: int

    def __new__(cls, value, code):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.code = code
        return obj

    ## ア
    FIRST = ("ア", 0)

    ## イ
    SECOND = ("イ", 1)

    ## ウ
    THIRD = ("ウ", 2)

    ## エ
    FOURTH = ("エ", 3)
