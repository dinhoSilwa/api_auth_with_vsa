from pydantic import BaseSettings, SettingsConfigDict
import os
from functools import lru_cache

# configuraçoes de variaveis de ambiente

class Settings(BaseSettings):
  model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
  PROJECT_NAME: str = os.getenv("PROJECT_NAME")
  SUPABASE_URL: str =  os.getenv("SUPABASE_URL")
  SUPABASE_SECRET_KEY: str = os.getenv("SUPABASE_SECRET_KEY")

  class Config:
    env_file = ".env"
    env_file_encoding = "utf-8"
    
@lru_cache
def get_settings() -> Settings:
  return Settings()

