import abc
from typing import Callable, List

from pydantic import BaseModel
from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base

# import all models for sqlalchemy mapping class(required)
from src.database.models import *


class AbstractRepository(abc.ABC):

    def __init__(self,
                 db: Callable[..., AsyncSession],
                 model: declarative_base()
                 ):

        self.model = model
        self.db = db

    async def get_all(self):
        stmt = select(self.model)
        result = await self._db_execute_stmt(stmt)
        return result.all()

    async def get_by_ids(self, primary_ids: list) -> list:
        stmt = select(self.model).where(
            self.model.id.in_(primary_ids)
        )
        result = await self._db_execute_stmt(stmt)
        return result.all()

    async def delete_by_ids(self, primary_ids: list) -> None:
        stmt = delete(self.model)\
            .where(self.model.id.in_(primary_ids))

        await self._db_execute_stmt(stmt)

    async def update_by_ids(self, primary_ids: list, pydantic_model: BaseModel):
        stmt = update(self.model)\
            .where(self.model.id.in_(primary_ids))\
            .values(**(pydantic_model.dict(exclude_defaults=True)))\
            .execution_options(synchronize_session="fetch")\

        return await self._db_execute_stmt(stmt=stmt)

    async def insert(self, pydantic_models: List[BaseModel]):
        """
        Args:
            pydantic model: UserCreate, ItemCreate etc.
        Returns:

        """
        model_objects = [self.model(**each.dict()) for each in pydantic_models]
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
