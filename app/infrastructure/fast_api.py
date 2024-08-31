from fastapi import FastAPI
from app.infrastructure.handlers import Handlers


def create_app():
    fast_api = FastAPI()
    for handler in Handlers.iterator():
        fast_api.include_router(handler.router)
    return fast_api
