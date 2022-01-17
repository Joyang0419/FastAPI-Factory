from dependency_injector import providers, containers

from src.containers.container_repos import ContainerRepos
from src.services.orm.service_users import IMPServiceUsers


class ContainerServices(containers.DeclarativeContainer):

    service_users = providers.Factory(
        IMPServiceUsers,
        repo_users=ContainerRepos.repo_users,
    )
