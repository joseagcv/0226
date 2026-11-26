from fastapi import FastAPI
from api.routers import api_router
import uvicorn

app = FastAPI(title="Character CRUD API")
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")