from dependency_injector import providers, containers

from src.containers.container_configs import ContainerConfigs
from src.tools.db_manager.imp_sqlalchemy import IMPSqlalchemy
from src.tools.notification.imp_gmail import IMPGmail


container_configs = ContainerConfigs()


class ContainerTools(containers.DeclarativeContainer):

    db_manager = providers.Singleton(
        IMPSqlalchemy,
        db_dialect=container_configs.config.db_config.db_dialect,
        async_db_driver=container_configs.config.db_config.async_db_driver,
        db_driver=container_configs.config.db_config.db_driver,
        db_user=container_configs.config.db_config.db_user,
        db_pwd=container_configs.config.db_config.db_pwd,
        db_host=container_configs.config.db_config.db_host,
        db_port=container_configs.config.db_config.db_port,
        db_name=container_configs.config.db_config.db_name,
        echo=container_configs.config.db_config.echo
    )
    notification_manager = providers.Factory(
        IMPGmail
    )
