from typing import List

from src.database.settings import tool_async_sqlalchemy
from src.repos.repo_user import RepoUser
from src.schemas.models.users import UserItem, UserCreate, User, UserUpdate
from src.schemas.routers.users import UserItemInfos, UserInfos


class ServiceUser:

    def __init__(self, repo: RepoUser = RepoUser(
        db=tool_async_sqlalchemy.get_db
    )):
        self.repo = repo

    async def get_user_by_ids(self, user_ids: list):

        result = await self.repo.get_by_ids(primary_ids=user_ids)
        users_dict = {}

        for each in result:
            user_pydantic_model = UserItem.from_orm(each)
            users_dict[user_pydantic_model.email] = user_pydantic_model

        return UserItemInfos(data=users_dict)

    async def get_all_users(self):

        result = await self.repo.get_all()

        users_dict = {}
        for each in result:
            user_pydantic_model = UserItem.from_orm(each)
            users_dict[user_pydantic_model.email] = user_pydantic_model

        return UserItemInfos(data=users_dict)

    async def create_user(self, pydantic_models: List[UserCreate]):

        result = await self.repo.insert(pydantic_models=pydantic_models)

        users_dict = {}
        for each in result:
            user_pydantic_model = User.from_orm(each)
            users_dict[user_pydantic_model.email] = user_pydantic_model

        return UserInfos(data=users_dict)

    async def update_user_by_ids(self, user_ids: list,
                                 pydantic_model: UserUpdate):

        result = await self.repo.update_by_ids(
            primary_ids=user_ids,
            pydantic_model=pydantic_model
        )

        users_dict = {}
        for each in result:
            user_pydantic_model = User.from_orm(each)
            users_dict[user_pydantic_model.email] = user_pydantic_model

        return UserInfos(data=users_dict)

    async def delete_user_by_ids(self, user_ids: list):

        result = await self.repo.delete_by_ids(user_ids)

        users_dict = {}
        for each in result:
            user_pydantic_model = User.from_orm(each)
            users_dict[user_pydantic_model.email] = user_pydantic_model

        return UserInfos(data=users_dict)
