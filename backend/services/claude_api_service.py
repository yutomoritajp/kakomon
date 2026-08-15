from anthropic import Anthropic
from dotenv import load_dotenv

class ClaudeApiService:
    _client: Anthropic
    _default_model = "claude-opus-5"
    _default_max_tokens = 1024
    
    def __init__(self) -> None:
        load_dotenv()
        self._client = Anthropic()
    
    def create_message(self, messages: list, output_config):
        return self._client.messages.create(
            model = self._default_model,
            max_tokens = self._default_max_tokens,
            messages = messages,
            output_config = output_config
        )
