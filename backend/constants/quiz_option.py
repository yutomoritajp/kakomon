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
    A = ("ア", 0)

    ## イ
    B = ("イ", 1)
    
    ## ウ
    C = ("ウ", 2)
    
    ## エ
    D = ("エ", 3)
