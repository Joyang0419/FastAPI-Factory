import contextlib
from typing import Callable

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, Session

from src.tools.tool_db_manager.interface import IFDBManager


class IMPSqlalchemy(IFDBManager):

    def __init__(
            self,
            db_dialect: str,
            async_db_driver: str,
            db_driver,
            db_user: str,
            db_pwd: str,
            db_host: str,
            db_port: int,
            db_name: str,
            echo: bool
    ):
        """

        Args:
            db_dialect: database name such as mysql, oracle, postgresql.
            async_db_driver: driver the name of a DB_API,
                such as psycopg2, pyodbc, cx_oracle, aiomysql etc.
            db_driver: driver the name of a DB_API,
                such as psycopg2, pyodbc, cx_oracle, aiomysql etc.
            db_user: user
            db_pwd: password
            db_host: host
            db_port: port
            db_name: database's name
            echo: if True, the Engine will log all statements as well as a repr.
        """
        self.async_db_url = f"{db_dialect}+{async_db_driver}" \
                            f"://{db_user}:{db_pwd}" \
                            f"@{db_host}:{db_port}/{db_name}"

        self.db_url = f"{db_dialect}+{db_driver}" \
                      f"://{db_user}:{db_pwd}" \
                      f"@{db_host}:{db_port}/{db_name}"

        self.echo = echo

        self._initialize()

    def _initialize(self):
        """
        Configure class for creating scoped session.
        :return:
        """
        self._engine = create_engine(
            url=self.db_url,
            echo=self.echo,
        )

        session_factory = sessionmaker(
            bind=self._engine,
            autocommit=False,
            autoflush=False
        )
        self._session = session_factory()

        self._async_engine = create_async_engine(
            url=self.async_db_url,
            echo=self.echo,
            future=True
        )

        async_session_factory = sessionmaker(
            bind=self._async_engine,
            expire_on_commit=False,
            class_=AsyncSession
        )
        self._async_session = async_session_factory()

    def connection(self):
        return self._engine.connect()

    @contextlib.asynccontextmanager
    async def get_async_db(self) -> Callable[..., AsyncSession]:
        """contextmanager will create and teardown a async session"""
        try:
            yield self._async_session
            await self._async_session.commit()

        except Exception:
            await self._async_session.rollback()
            raise

        finally:
            await self._async_session.close()

    @contextlib.contextmanager
    def get_db(self) -> Callable[..., Session]:
        """contextmanager will create and teardown a session"""
        try:
            yield self._session
            self._session.commit()

        except Exception:
            self._session.rollback()
            raise

        finally:
            self._session.close()

    @contextlib.asynccontextmanager
    async def get_fake_async_db(self) -> Callable[..., AsyncSession]:
        """
        create fake session to run test case.
        References:
            - async_session: https://github.com/sqlalchemy/sqlalchemy/issues/5811,
            - pytest session create step: https://stackoverflow.com/questions/58660378/how-use-pytest-to-unit-test-sqlalchemy-orm-classes

        Args:

        Returns:

        """
        async with self._async_engine.connect() as conn:
            await conn.begin()

            await conn.begin_nested()

            async_session = AsyncSession(conn)

            yield async_session

            await conn.close()
