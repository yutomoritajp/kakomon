from anthropic import Anthropic, types
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)

class ClaudeApiService:
    _client: Anthropic
    _model: str
    _max_tokens: int
    
    _DEFAULT_MODEL = "claude-opus-5"
    _DEFAULT_MAX_TOKENS = 5000
    
    def __init__(self, model: str|None = None, max_tokens: int|None = None) -> None:
        load_dotenv()
        self._client = Anthropic()
        self._model = model if model is not None else self._DEFAULT_MODEL
        self._max_tokens = max_tokens if max_tokens is not None else self._DEFAULT_MAX_TOKENS
        
    def create_message(self, messages: list, **kwargs) -> None:
        """
        Todo: 後から使う可能性が高いので残しておく。
        """
        pass

    def create_parse_message(self, messages: list, **kwargs) -> types.ParsedMessage:
        """
        output_formatなどの簡易パラメータを使う場合に使用する。
        create_messageが使用可能な場合はそちらを使用する。
        """
        
        logger.info("ClaudeAPIリクエスト開始 model=%s, max_tokens=%s", self._model, self._max_tokens)
        
        response =  self._client.messages.parse(
            model = self._model,
            max_tokens = self._max_tokens,
            messages = messages,
            **kwargs
        )
        
        logger.info("ClaudeAPIリクエスト終了 stop_reason=%s, usage=%s", response.stop_reason, response.usage)

        return response
    