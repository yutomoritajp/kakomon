

class ClauadeApiResponseException(Exception):
    """
    Claude APIの応答が異常だった場合の例外
    """

    def __init__(self, stop_reason: str, usage: dict | None) -> None:
        self.stop_reason = stop_reason
        self.usage = usage

        super().__init__(f"ClaudeAPIの応答が正しく終了しませんでした。stop_reason: {stop_reason}")
