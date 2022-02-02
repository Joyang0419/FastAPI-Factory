from dependency_injector import providers, containers
from passlib.context import CryptContext

from src.containers.container_configs import ContainerConfigs
from src.utilities.db_manager.imp_sqlalchemy import IMPSqlalchemy
from src.utilities.encrypt_pwd.imp_crypt_context import IMPCryptManager
from src.utilities.notification.imp_gmail import IMPGmail
from src.utilities.jwt_token.imp_jwt import IMPJWTManager

container_configs = ContainerConfigs()


class ContainerUtilities(containers.DeclarativeContainer):

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

    crypt_context = providers.Singleton(
        CryptContext,
        schemes=container_configs.config.pwd_crypt_config.schemes,
        deprecated=container_configs.config.pwd_crypt_config.deprecated
    )

    crypt_manager = providers.Factory(
        IMPCryptManager,
        crypt_context=crypt_context
    )

    jwt_manager = providers.Factory(
        IMPJWTManager
    )
