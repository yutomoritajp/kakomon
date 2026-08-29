from dataclasses import dataclass


@dataclass(frozen=True)
class PageRange:
    """
    PDFのページ範囲。ページ番号は1始まり
    """

    start: int
    end: int

    def __post_init__(self) -> None:
        if self.start < 1 or self.end < 1:
            raise ValueError(
                "ページ番号は1以上を指定してください。"
                f"start={self.start}, end={self.end}"
            )
        if self.start > self.end:
            raise ValueError(
                "開始ページは終了ページ以下を指定してください。"
                f"start={self.start}, end={self.end}"
            )
