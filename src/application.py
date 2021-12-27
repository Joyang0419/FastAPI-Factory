from fastapi import FastAPI

from src.container import Container
from src.routers.v1 import users

from src.core.config import Settings


def create_app() -> FastAPI:
    container = Container()
    # config setting
    container.config.from_pydantic(Settings())

    # wire configuration
    container.wire(packages=['src.routers'])

    # create FastAPI
    application = FastAPI(
        title=container.config.app_config.title(),
        version=container.config.app_config.version(),
        debug=container.config.app_config.debug()
    )

    # add router to application
    application.include_router(users.router)

    return application


app = create_app()
