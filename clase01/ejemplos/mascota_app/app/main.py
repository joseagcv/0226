from fastapi import FastAPI
from app.db import models, database
from app.api.routes import router as pets_router
from app.config import settings

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="FastAPI Pets")

app.include_router(pets_router)

@app.get("/")

def root():
    return {"message": settings.WELCOME_MESSAGE}