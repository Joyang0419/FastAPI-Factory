from dependency_injector import providers, containers

from src.configs.config import Settings


class ContainerConfigs(containers.DeclarativeContainer):

    config = providers.Configuration(pydantic_settings=[Settings()])
