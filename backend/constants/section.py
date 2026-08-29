from enum import Enum


class Section(Enum):
    """
    試験区分
    """

    ### 問題数
    quiz_count: int | None

    def __new__(cls, code, quiz_count):
        obj = object.__new__(cls)
        obj._value_ = code
        obj.quiz_count = quiz_count
        return obj

    ## 午前Ⅰ
    AM1 = ("am1", 30)

    ## 午前Ⅱ
    AM2 = ("am2", 25)

    ## 午後Ⅰ
    PM1 = ("pm1", None)

    ## 午後Ⅱ
    PM2 = ("pm2", None)
