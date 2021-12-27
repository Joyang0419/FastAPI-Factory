from typing import Callable
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base

from src.models.items import Item
from src.repos.interface.repo_user import IFRepoUser
from src.repos.orm.repo_base import RepoBase
from src.schemas.models.users import UserUpdate, UserCreate


class IMPRepoUser(RepoBase, IFRepoUser):

    def __init__(
            self,
            db: Callable[..., AsyncSession],
            model: declarative_base
    ):
        super().__init__(db=db, model=model)

    async def user_create_item(self, user_id: int, item: Item):
        sql_result = await self.get_by_ids(primary_ids=[user_id])
        user = sql_result[0]
        user.items.append(item)
        model_objects = [user]
        await self._db_complete_commit(model_objects)

    async def update_by_ids(
            self,
            primary_ids: list,
            data: UserUpdate.dict
    ):
        return await super().update_by_ids(
            primary_ids=primary_ids,
            data=data
        )

    async def insert(self, data: List[UserCreate.dict]):
        return await super().insert(data=data)

    async def delete_by_ids(self, primary_ids: list):
        return await super().delete_by_ids(primary_ids=primary_ids)
