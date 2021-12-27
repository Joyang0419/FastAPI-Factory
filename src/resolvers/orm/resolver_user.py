from typing import Type

from src.resolvers.orm.resolver_base import IMPResolverBase
from src.schemas.models.users import User
from src.schemas.routers.users import UserInfos
from src.schemas.routers.users import UserInfosOutputKey
from src.repos.orm.repo_user import IMPRepoUser


class IMPResolverRepoUser(IMPResolverBase):

    def __init__(
            self,
            pydantic_model: Type[User],
            output_schema=Type[UserInfos]
    ):
        super(IMPResolverRepoUser, self).__init__(
            pydantic_model=pydantic_model,
            output_schema=output_schema
        )

    def resolve_get_all(
            self,
            input_data: IMPRepoUser.get_all,
            output_key: UserInfosOutputKey.email
    ) -> UserInfos.dict:

        return super(IMPResolverRepoUser, self).resolve_get_all(
            input_data=input_data,
            output_key=output_key
        )

    def resolve_get_by_ids(
            self,
            input_data: IMPRepoUser.get_by_ids,
            output_key: UserInfosOutputKey.id
    ) -> UserInfos.dict:

        return super(IMPResolverRepoUser, self).resolve_get_by_ids(
            input_data=input_data,
            output_key=output_key
        )

    def resolve_insert(
            self,
            input_data: IMPRepoUser.insert,
            output_key: UserInfosOutputKey.email
    ) -> UserInfos.dict:

        return super(IMPResolverRepoUser, self).resolve_insert(
            input_data=input_data,
            output_key=output_key
        )

    def resolve_delete_by_ids(
            self,
            input_data: IMPRepoUser.delete_by_ids,
            output_key: UserInfosOutputKey.id
    ) -> UserInfos.dict:

        return super(IMPResolverRepoUser, self).resolve_delete_by_ids(
            input_data=input_data,
            output_key=output_key
        )

    def resolve_update_by_ids(
            self,
            input_data: IMPRepoUser.update_by_ids,
            output_key: UserInfosOutputKey.id
    ) -> UserInfos.dict:

        return super(IMPResolverRepoUser, self).resolve_update_by_ids(
            input_data=input_data,
            output_key=output_key
        )
