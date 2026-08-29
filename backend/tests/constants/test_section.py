import pytest

from constants.section import Section


@pytest.mark.parametrize(
    ["value", "quiz_count"],
    [("am1", 30), ("am2", 25), ("pm1", None), ("pm2", None)],
    ids=[
        "When value is am1, it should return 30 as quiz_count.",
        "When value is am2, it should return 25 as quiz_count.",
        "When value is pm1, it should return None as quiz_count.",
        "When value is pm2, it should return None as quiz_count.",
    ],
)
def test_get_quiz_count(value: str, quiz_count: int | None) -> None:
    section = Section(value)
    assert section.quiz_count == quiz_count


@pytest.mark.parametrize(
    "value",
    ["pm3", "", None],
    ids=[
        "When value is 'pm3', it should raise ValueError.",
        "When value is Empty, it should raise ValueError.",
        "When value is None, it should raise ValueError.",
    ],
)
def test_invalid_value(value: str | None) -> None:
    with pytest.raises(ValueError):
        Section(value)


def test_values_are_lower_case() -> None:
    """
    valueが小文字であることを確認するテスト。（ディレクトリ名に使用される。）
    """
    for section in Section:
        assert isinstance(section.value, str)
        assert section.value == section.value.lower()
