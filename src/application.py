from fastapi import FastAPI

from src.container import Container
from src.routers.v1 import users


def create_app() -> FastAPI:
    container = Container()

    # create FastAPI
    application = FastAPI(
        title=container.config.app_config.title(),
        version=container.config.app_config.version(),
        debug=container.config.app_config.debug()
    )

    application.container = container

    # add router to application
    application.include_router(users.router)

    return application


app = create_app()
