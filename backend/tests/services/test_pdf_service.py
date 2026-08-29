import pytest


@pytest.mark.skip(reason="後ほど作成予定")
def test_get_target_doc():
    """
    Todo:
    _get_target_docの正常系のテストを書く。
    page_ranageを変えた時に1始まりの期待通りのページ範囲のpymupdf.Documentが作られることを
    確認する。
    """


@pytest.mark.skip(reason="後ほど作成予定")
def test_get_target_doc_in_appropriate_page_range():
    """
    Todo:
    PageRangeが不適切な場合に例外を出すテストを書く。
    PageRangeで弾けるパターンは書かない。
    具体的には、ページの最後が超えているパターン
    """


@pytest.mark.skip(reason="後ほど作成予定")
def test_create_path():
    """
    正しいパスが作成されることを確認するテストを作成する。
    """
