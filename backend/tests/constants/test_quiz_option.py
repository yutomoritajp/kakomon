import pytest

from constants.quiz_option import QuizOption


@pytest.mark.parametrize(
    ["value", "code"],
    [("ア", 0), ("イ", 1), ("ウ", 2), ("エ", 3)],
    ids=[
        "When value is 'ア', it should return 0 as code.",
        "When value is 'イ', it should return 1 as code.",
        "When value is 'ウ', it should return 2 as code.",
        "When value is 'エ', it should return 3 as code.",
    ],
)
def test_get_code(value: str, code: int) -> None:
    option = QuizOption(value)
    assert option.code == code


@pytest.mark.parametrize(
    "value",
    ["オ", "あ", "", None],
    ids=[
        "When value is 'オ', it should raise ValueError.",
        "When value is 'あ', it should raise ValueError.",
        "When value is Empty, it should raise ValueError.",
        "When value is None, it should raise ValueError.",
    ],
)
def test_invalid_value(value: str | None) -> None:
    with pytest.raises(ValueError):
        QuizOption(value)


def test_code_between_0_and_3() -> None:
    """
    quizzes.correct_option のCHECK制約（between 0 and 3）と整合していることを確認する。
    選択肢を増減させる場合は、data/models.py のCHECK制約も合わせて変更する必要がある。
    """
    sorted_codes = sorted([option.code for option in QuizOption])

    assert sorted_codes == list(range(0, 4))
