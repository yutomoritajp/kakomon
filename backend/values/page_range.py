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
            raise ValueError(f"ページ番号は1以上を指定してください。start={self.start}, end={self.end}")
        if self.start > self.end:
            raise ValueError(f"開始ページは終了ページ以下を指定してください。start={self.start}, end={self.end}")
