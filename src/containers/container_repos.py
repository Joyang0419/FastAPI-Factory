from dependency_injector import providers, containers

from src.containers.container_utilities import ContainerUtilities
from src.repos.orm.repo_users import IMPRepoUsers

container_tools = ContainerUtilities()


class ContainerRepos(containers.DeclarativeContainer):

    db = providers.Resource(
        container_tools.db_manager.provided.get_async_db
    )

    repo_users = providers.Factory(
        IMPRepoUsers,
        db=db,
    )
