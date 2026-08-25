import pytest
from usecases.create_quiz import create_quiz_data, _get_correct_options
from constants.period import Period
from constants.section import Section


@pytest.mark.parametrize(["period", "section", "expected"], [
    (Period.R7, Section.AM1, {
        1: "イ", 5: "イ", 11: "ア", 17: "エ", 21: "エ", 25: "ウ", 28: "イ", 30: "ア"
    }),
    (Period.R6, Section.AM1, {
        1: "エ", 3: "イ", 8: "ウ", 13: "ア", 19: "エ", 20: "エ", 24: "イ", 30: "ア"
    })
], ids=[
    "When R7-AM1 is selected, iit should return the expected correct_options.",
    "When R6-AM1 is selected, iit should return the expected correct_options.",
])
def test_get_correct_options(period: Period, section: Section, expected: dict[int, str]):
    """
    実データを用いて、正しい解答が取得できることを確認する。
    正解結果はランダムな問題番号をスポットチェックする。
    新しいPeriod, Sectionに対応したらこのUTにパターンを追加する。
    """
    correct_options = _get_correct_options(period, section)
    
    ## 問題数が正しいこと。
    assert len(correct_options) == section.quiz_count
    
    ## 正しい答えが取得できていること。
    for number, option in expected.items():
        assert correct_options[number] == option
