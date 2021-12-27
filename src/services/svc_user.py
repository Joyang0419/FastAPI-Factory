from typing import List, Dict

from src.repos.orm.repo_user import IMPRepoUser
from src.resolvers.orm.resolver_user import IMPResolverRepoUser
from src.schemas.models.users import UserCreate, UserUpdate
from src.schemas.routers.users import UserInfosOutputKey


class SVCUser:

    def __init__(
            self,
            repo: IMPRepoUser,
            resolver: IMPResolverRepoUser
    ):
        self.repo = repo
        self.resolver = resolver

    async def get_all_users(self):

        db_result = await self.repo.get_all()

        return self.resolver.resolve_get_all(
            input_data=db_result,
            output_key=UserInfosOutputKey.email
        )

    async def get_user_by_ids(self, user_ids: list):

        db_result = await self.repo.get_by_ids(primary_ids=user_ids)

        return self.resolver.resolve_get_by_ids(
            input_data=db_result,
            output_key=UserInfosOutputKey.email
        )

    async def create_user(self, data: List[UserCreate]):

        db_result = await self.repo.insert(data=data)

        return self.resolver.resolve_insert(
            input_data=db_result,
            output_key=UserInfosOutputKey.email
        )

    async def delete_user_by_ids(self, user_ids: list):

        db_result = await self.repo.delete_by_ids(user_ids)

        return self.resolver.resolve_delete_by_ids(
            input_data=db_result,
            output_key=UserInfosOutputKey.id

        )

    async def update_user_by_ids(
            self,
            user_ids: list,
            data: Dict[str, UserUpdate]
    ):
        db_result = await self.repo.update_by_ids(
            primary_ids=user_ids,
            data=data
        )

        return self.resolver.resolve_update_by_ids(
            input_data=db_result,
            output_key=UserInfosOutputKey.id
        )
