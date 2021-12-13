from fastapi import FastAPI
from src.routers.v1 import users, items


def create_app() -> FastAPI:
    application = FastAPI()

    # routers
    application.include_router(users.router)
    application.include_router(items.router)

    return application


app = create_app()
