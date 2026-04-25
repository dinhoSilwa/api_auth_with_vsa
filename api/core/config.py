from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

    PROJECT_NAME: str
    SUPABASE_URL: str
    SUPABASE_SECRET_KEY: str


@lru_cache
def get_settings() -> Settings:
    return Settings()