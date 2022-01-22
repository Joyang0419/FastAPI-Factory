from typing import Callable
from typing import List, Union

from sqlalchemy import select, delete, update
from sqlalchemy.exc import ArgumentError
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.users import User
from src.repos.interface.repo_users import IFRepoUser
from src.schemas.models.users import (
    UserUpdate,
    UserCreate
)


class IMPRepoUsers(IFRepoUser):

    def __init__(
            self,
            db: Callable[..., AsyncSession],
    ):
        self.db = db
        self.events = []

    async def _db_execute_stmt(self, stmt: str):
        """
        execute sql statement.

        Args:
            stmt: sql's syntax
        Returns:
            sql executed result
        """
        async with self.db() as db:
            result = await db.execute(statement=stmt)

        return result

    async def get_all_users(self) -> list:
        """
        get all users

        Returns:
            [sqlalchemy object]

        """
        try:
            stmt = select(User)
            result = await self._db_execute_stmt(stmt)
            return result.scalars().all()
        except ArgumentError:
            print('SQL error.')

    async def get_users_by_ids(self, user_ids: list) -> list:
        """
        get_users_by_ids


        Args:
            user_ids: [primary key: id]

        Returns:
            [sqlalchemy object]
        """

        stmt = select(User).where(
            User.id.in_(user_ids)
        )
        result = await self._db_execute_stmt(stmt)

        return result.scalars().all()

    async def create_users(self, data: List[UserCreate]):
        """
        create users

        Args:
            data: [UserCreate(pydantic).dict]

        Returns:
            [sqlalchemy object]
        """

        model_objects = [User(**each.dict()) for each in data]

        async with self.db() as db:
            db.add_all(model_objects)
            result = [await db.merge(each) for each in model_objects]

        return result

    async def delete_users_by_ids(
            self,
            user_ids: list
    ) -> List[User]:
        """
        delete users by ids

        Args:
            user_ids: [primary key: id]

        Returns:
            [] or [sqlalchemy's obj]

        """

        delete_rows = await self.get_users_by_ids(user_ids)

        if not delete_rows:
            return []

        stmt = delete(User) \
            .where(User.id.in_(user_ids))

        await self._db_execute_stmt(stmt)

        return delete_rows

    async def update_users_by_ids(
            self,
            user_ids: list,
            data: UserUpdate
    ) -> Union[list, List[User]]:
        """
        update_users_by_ids

        Args:
            user_ids: [primary key: id]
            data: UserUpdate(pydantic).dict

        Returns:
            [] or [sqlalchemy's obj]

        """
        update_rows = await self.get_users_by_ids(user_ids)

        if not update_rows:
            return []

        stmt = update(User) \
            .where(User.id.in_(user_ids)) \
            .values(**data.dict(exclude_none=True)) \
            .execution_options(synchronize_session="fetch")

        await self._db_execute_stmt(stmt=stmt)

        update_rows = await self.get_users_by_ids(user_ids)

        return update_rows
