from pathlib import Path

from pydantic import BaseSettings


class ReadEnv(BaseSettings):

    class Config:
        env_file = Path(__file__)\
            .resolve().parent.parent.parent.joinpath(".env")
        env_file_encoding = 'utf-8'


class DatabaseConfig(ReadEnv):
    """Database Config"""
    db_dialect: str
    async_db_driver: str
    db_driver: str
    db_host: str
    db_port: int
    db_user: str
    db_pwd: str
    db_name: str
    echo: bool


class ApplicationConfig(ReadEnv):
    """Application Config"""
    title: str
    version: str
    debug: bool


class Settings(BaseSettings):
    """Pydantic Base Settings"""
    app_config: ApplicationConfig = ApplicationConfig()
    db_config: DatabaseConfig = DatabaseConfig()

