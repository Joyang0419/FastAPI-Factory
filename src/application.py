from fastapi import FastAPI

from src.containers.container_configs import ContainerConfigs
from src.containers.container_repos import ContainerRepos
from src.containers.container_services import ContainerServices
from src.containers.container_tools import ContainerTools
from src.routers.v1 import users


def create_app() -> FastAPI:

    # containers
    container_services = ContainerServices()
    container_tools = ContainerTools()
    container_repos = ContainerRepos()
    container_configs = ContainerConfigs()

    # create FastAPI
    application = FastAPI(
        title=container_configs.config.app_config.title(),
        version=container_configs.config.app_config.version(),
        debug=container_configs.config.app_config.debug()
    )

    application.container_services = container_services
    application.container_tools = container_tools
    application.container_repos = container_repos

    # add router to application
    application.include_router(users.router)

    return application


app = create_app()
