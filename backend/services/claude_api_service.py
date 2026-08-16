from anthropic import Anthropic, types
from dotenv import load_dotenv
from services.exceptions.claude_api_response_exception import ClauadeApiResponseException

class ClaudeApiService:
    _client: Anthropic
    _default_model = "claude-opus-5"
    _default_max_tokens = 1024
    
    def __init__(self) -> None:
        load_dotenv()
        self._client = Anthropic()
    
    def create_message(self, messages: list, **keyargs) -> None:
        """
        Todo: 後から使う可能性が高いので残しておく。
        """
        pass

    def create_parse_message(self, messages: list, **keyargs) -> types.ParsedMessage:
        """
        output_formatなどの簡易パラメータを使う場合に使用する。
        create_messageが使用可能な場合はそちらを使用する。
        """
        response =  self._client.messages.parse(
            model = self._default_model,
            max_tokens = self._default_max_tokens,
            messages = messages,
            **keyargs
        )

        if response.stop_reason != "end_turn":
            raise ClauadeApiResponseException(stop_reason=response.stop_reason, usage=response.usage)

        return response