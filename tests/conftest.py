import asyncio
import typing

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from src.application import app
from src.containers.container_tools import ContainerTools
from src.tools.db_manager.imp_sqlalchemy import IMPSqlalchemy

db_manager = ContainerTools().db_manager()


@pytest.fixture(scope="session")
def event_loop() -> typing.Generator:
    """
    Create an instance of the default event loop for each test case.
    References: https://github.com/pytest-dev/pytest-asyncio/issues/207

    Returns:

    """
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def fake_db_session() -> AsyncSession:
    """
    create fake session to run test case.
    References:
        - async_session: https://github.com/sqlalchemy/sqlalchemy/issues/5811,
        - pytest session create step: https://stackoverflow.com/
        questions/58660378/how-use-pytest-to-unit-test-sqlalchemy-orm-classes

    Args:

    Returns:

    """
    yield db_manager.get_fake_async_db


@pytest.fixture(scope='function', autouse=True)
@pytest.mark.asyncio
async def test_client(monkeypatch) -> AsyncClient:
    """
    Provide TestClient
    References: https://github.com/encode/starlette/issues/1315
    """
    async_client = AsyncClient(app=app, base_url="http://test")
    monkeypatch.setattr(
        target=IMPSqlalchemy,
        name='get_async_db',
        value=db_manager.get_fake_async_db
    )
    yield async_client
