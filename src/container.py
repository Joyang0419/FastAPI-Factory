"""Containers module."""

from dependency_injector import containers, providers

from src.database.manager.imp_sqlalchemy import IMPSqlalchemy
from src.models.users import User
from src.repos.orm.repo_user import IMPRepoUser
from src.resolvers.orm.resolver_user import IMPResolverRepoUser
from src.schemas.models.users import User as UserSchema
from src.schemas.routers.users import UserInfos
from src.services.svc_user import SVCUser


class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    imp_sqlalchemy = providers.Singleton(
        IMPSqlalchemy,
        db_dialect=config.db_config.db_dialect,
        async_db_driver=config.db_config.async_db_driver,
        db_driver=config.db_config.db_driver,
        db_user=config.db_config.db_user,
        db_pwd=config.db_config.db_pwd,
        db_host=config.db_config.db_host,
        db_port=config.db_config.db_port,
        db_name=config.db_config.db_name,
        echo=config.db_config.echo
    )

    repo_user = providers.Factory(
        IMPRepoUser,
        db=imp_sqlalchemy.provided.get_async_db,
        model=User
    )

    resolver_repo_user = providers.Factory(
        IMPResolverRepoUser,
        pydantic_model=UserSchema,
        output_schema=UserInfos
    )

    svc_user = providers.Factory(
        SVCUser,
        repo=repo_user,
        resolver=resolver_repo_user
    )



if __name__ == '__main__':
    container = Container()
    # container.config.from_pydantic(Settings())

    import asyncio
    async def example():
        a = await container.svc_user().get_all_users()
        print(a)



    loop = asyncio.get_event_loop()
    loop.run_until_complete(example())

