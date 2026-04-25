import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from fastapi import FastAPI

from api.core.config import get_settings

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
  config = get_settings()
  logging.info(f"Iniciando Projeto {config.PROJECT_NAME}")
  yield
  logging.info(f"Encerrando Projeto {config.PROJECT_NAME}")