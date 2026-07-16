from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    app_name: str = "AI Router"

    log_level: str = "INFO"

    ollama_base_url: str = "http://localhost:11434"

    default_model: str = "qwen2.5-coder:7b"

    ollama_timeout: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()