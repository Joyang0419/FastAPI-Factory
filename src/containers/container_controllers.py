from dependency_injector import providers, containers

from src.containers.container_services import ContainerServices
from src.controllers.orm.controller_users import IMPControllerUsers

container_services = ContainerServices()


class ContainerControllers(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        packages=['src.routers'],
    )

    controller_users = providers.Factory(
        IMPControllerUsers,
        service_users=container_services.service_users
    )
