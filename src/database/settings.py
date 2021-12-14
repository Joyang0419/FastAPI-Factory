import pymysql
from sqlalchemy.ext.declarative import declarative_base

from src.SharedLibrary.db_manager.tool_async_sqlalchemy import \
    ToolAsyncSqlalchemy
from src.SharedLibrary.db_manager.tool_sqlalchemy import ToolSqlalchemy
from src.core.config import DatabaseConfig

pymysql.install_as_MySQLdb()

Base = declarative_base()
database_config = DatabaseConfig()

tool_async_sqlalchemy = ToolAsyncSqlalchemy(
    db_dialect=database_config.DB_DIALECT,
    db_driver=database_config.ASYNC_DB_DRIVER,
    db_user=database_config.DB_USER,
    db_password=database_config.DB_PWD,
    db_host=database_config.DB_HOST,
    db_port=database_config.DB_PORT,
    db_name=database_config.DB_NAME,
    echo=database_config.DB_ECHO_LOG
)


# here for migration and seeder
tool_sqlalchemy = ToolSqlalchemy(
    db_dialect=database_config.DB_DIALECT,
    db_driver=database_config.DB_DRIVER,
    db_user=database_config.DB_USER,
    db_password=database_config.DB_PWD,
    db_host=database_config.DB_HOST,
    db_port=database_config.DB_PORT,
    db_name=database_config.DB_NAME,
    echo=database_config.DB_ECHO_LOG
)

SQLALCHEMY_DATABASE_URL = tool_sqlalchemy.db_url

