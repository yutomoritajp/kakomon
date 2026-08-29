from enum import Enum


class QuizOption(Enum):
    """
    Quizの選択肢
    """

    ### 数値
    number: int

    def __new__(cls, value, number):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.number = number
        return obj

    ## ア
    FIRST = ("ア", 0)

    ## イ
    SECOND = ("イ", 1)

    ## ウ
    THIRD = ("ウ", 2)

    ## エ
    FOURTH = ("エ", 3)
