from typing import Callable, List

from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base

from src.repos.interface.repo_base import IFRepoBase


# import all models for sqlalchemy mapping class(required)
from src.models import items, users

models = [users.User, items.Item]


class RepoBase(IFRepoBase):

    def __init__(self,
                 db: Callable[..., AsyncSession],
                 model: declarative_base
                 ):

        self.model = model
        self.db = db

    async def get_all(self) -> list:

        stmt = select(self.model)
        result = await self._db_execute_stmt(stmt)

        return result.scalars().all()

    async def get_by_ids(self, primary_ids: list) -> list:

        stmt = select(self.model).where(
            self.model.id.in_(primary_ids)
        )
        result = await self._db_execute_stmt(stmt)

        return result.scalars().all()

    async def delete_by_ids(self, primary_ids: list):

        delete_rows = await self.get_by_ids(primary_ids)

        if not delete_rows:
            return []

        stmt = delete(self.model)\
            .where(self.model.id.in_(primary_ids))

        await self._db_execute_stmt(stmt)

        return delete_rows

    async def update_by_ids(
            self,
            primary_ids: list,
            data: dict
    ):

        update_rows = await self.get_by_ids(primary_ids)

        if not update_rows:
            return []

        stmt = update(self.model) \
            .where(self.model.id.in_(primary_ids)) \
            .values(**data) \
            .execution_options(synchronize_session="fetch")
        await self._db_execute_stmt(stmt=stmt)

        update_rows = await self.get_by_ids(primary_ids)

        return update_rows

    async def insert(self, data: List[dict]):
        """
        Args:
            pydantic model: UserCreate, ItemCreate etc.
        Returns:

        """

        model_objects = [self.model(**each.__dict__) for each in data]
        result = await self._db_complete_commit(model_objects=model_objects)

        return result

    async def _db_execute_stmt(self, stmt: str):
        """

        Args:
            stmt: sql's syntax
        Returns:
            execute_result
        """

        async with self.db() as db:
            result = await db.execute(statement=stmt)

        return result

    async def _db_complete_commit(self, model_objects):
        """

        Args:
            model_objects:
        Returns:
            execute_result
        """
        async with self.db() as db:
            db.add_all(model_objects)
            await db.commit()

        return model_objects
