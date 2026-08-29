import pytest

from values.page_range import PageRange


@pytest.mark.parametrize(
    ["start", "end"],
    [(1, 5), (3, 3)],
    ids=[
        "When start > 0, end > 0 and start < end, it should take the positive path.",
        "When start > 0, end > 0 and start == end, it should take the positive path.",
    ],
)
def test_positive(start, end):
    """
    正常系のテスト
    """
    page_range = PageRange(start, end)

    assert page_range.start == start
    assert page_range.end == end


@pytest.mark.parametrize(
    ["start", "end", "message"],
    [
        (0, 2, "ページ番号は1以上を指定してください。start=0, end=2"),
        (1, 0, "ページ番号は1以上を指定してください。start=1, end=0"),
        (-1, 3, "ページ番号は1以上を指定してください。start=-1, end=3"),
        (2, -1, "ページ番号は1以上を指定してください。start=2, end=-1"),
        (0, -1, "ページ番号は1以上を指定してください。start=0, end=-1"),
        (5, 4, "開始ページは終了ページ以下を指定してください。start=5, end=4"),
    ],
    ids=[
        "When start == 0, it should raise 'ValueError'.",
        "When end == 0, it should raise 'ValueError'.",
        "When start < 0, it should raise 'ValueError'.",
        "When end < 0, it should raise 'ValueError'.",
        "When start < 1 and end < 1, it should raise 'ValueError'.",
        "When start > end, it should raise 'ValueError'.",
    ],
)
def test_negative(start, end, message):
    """
    異常系のテスト
    ValueErrorが出ることを確認する。また、エラーメッセージが期待通りに表示されることを確認する。
    """
    with pytest.raises(ValueError) as e:
        PageRange(start, end)
    assert str(e.value) == message
