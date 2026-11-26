from fastapi import FastAPI
from api.routers import api_router

app = FastAPI(title="User CRUD API")
app.include_router(api_router)