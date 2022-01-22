import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from src.containers.container_tools import ContainerTools


class TestDBManager:

    def setup(self):
        """
        set attribute:
            db_manager()
        Returns:

        """
        self.db_manager = ContainerTools().db_manager()

    def test_connection(self):
        """
        GIVEN an db_manager
        WHEN db_manager.connection()
        THEN assert db_manager.connection()

        Returns:

        """
        assert self.db_manager.connection()

    @pytest.mark.asyncio
    async def test_get_async_db(self):
        """
        GIVEN an db_manager
        WHEN db_manager.get_async_db()
        THEN assert isinstance(async_db, AsyncSession)

        Returns:

        """
        async with self.db_manager.get_async_db() \
                as async_db:
            assert isinstance(async_db, AsyncSession)

    def test_get_db(self):
        """
        GIVEN an db_manager
        WHEN db_manager.get_db()
        THEN assert isinstance(async_db, Session)

        Returns:

        """

        with self.db_manager.get_db() as db:
            assert isinstance(db, Session)

    @pytest.mark.asyncio
    async def test_get_fake_async_db(self):
        """
        GIVEN an db_manager
        WHEN db_manager.get_fake_db()
        THEN assert isinstance(async_db, AsyncSessio)

        Returns:

        """

        async with self.db_manager.get_fake_async_db() as fake_async_db:
            assert isinstance(fake_async_db, AsyncSession)
