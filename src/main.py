from fastapi import FastAPI
from src.routes.route import router
import uvicorn


app = FastAPI()

app.include_router(router)
