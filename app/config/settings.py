from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Global application settings.

    All configuration is loaded from .env.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    APP_NAME: str = Field(default="AI Router")
    APP_ENV: str = Field(default="development")

    APP_HOST: str = Field(default="0.0.0.0")
    APP_PORT: int = Field(default=8000)

    LOG_LEVEL: str = Field(default="INFO")

    OLLAMA_HOST: str = Field(default="http://localhost:11434")
    DEFAULT_MODEL: str = Field(default="qwen3-coder")

    REQUEST_TIMEOUT: int = Field(default=300)

    MAX_RETRY: int = Field(default=2)
    OLLAMA_HOST: str = Field(default="http://127.0.0.1:11434")
    OLLAMA_TIMEOUT: int = Field(default=300)


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
