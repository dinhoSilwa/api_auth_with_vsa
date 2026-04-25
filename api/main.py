from fastapi import FastAPI
from .core.lifespan import lifespan

app = FastAPI(
    title="API de Autenticação",
    description="API de Autenticação para o projeto",
    version="0.1.0",
    contact={
        "name": "Claudio Silva",
        "email": "claudiosilva@gmail.com"
    },
    lifespan=lifespan
)

@app.get("/health")
async def health_check():
    return {"status": "ok"}