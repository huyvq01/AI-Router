from pydantic import BaseModel


class OllamaConfig(BaseModel):
    """
    Ollama connection configuration.
    """

    base_url: str = "http://localhost:11434"
    timeout: float = 60.0


ollama_config = OllamaConfig()
