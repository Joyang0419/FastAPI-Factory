from pydantic import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    """Pydantic Base Settings"""

    class Config:
        env_file = Path(__file__)\
            .resolve().parent.parent.parent.joinpath(".env")
        env_file_encoding = 'utf-8'


class DatabaseConfig(Settings):
    """Database Config"""
    DB_DIALECT: str
    DB_DRIVER: str
    ASYNC_DB_DRIVER: str
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PWD: str
    DB_NAME: str
    DB_ECHO_LOG: bool
