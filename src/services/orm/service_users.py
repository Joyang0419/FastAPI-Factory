import typing

from src.models.users import User as ModelUser
from src.repos.orm.repo_users import IMPRepoUsers
from src.schemas.models.users import (
    User as SchemaUser,
    UserUpdate as SchemaUserUpdate,
    UserCreate as SchemaUserCreate
)
from src.schemas.routers.users import (
    UserInfosOutputKey
)
from src.services.interface.service_users import IFServiceUsers


class IMPServiceUsers(IFServiceUsers):
    """
    Purpose: Handle repo_user return, let Controller_users use.
    """

    def __init__(
            self,
            repo_users: IMPRepoUsers,
    ):
        self.repo_users = repo_users

    async def get_all_users(
            self,
            output_key: UserInfosOutputKey
    ) -> dict:

        repo_result = await self.repo_users.get_all_users()
        output = self._packing_be_output_dict(
            input_data=repo_result,
            output_key=output_key
        )

        return output

    async def get_users_by_ids(
            self,
            user_ids: [int],
            output_key: UserInfosOutputKey
    ) -> dict:

        repo_result = await self.repo_users.get_users_by_ids(
            user_ids=user_ids
        )
        output = self._packing_be_output_dict(
            output_key=output_key,
            input_data=repo_result
        )

        return output

    async def update_users_by_ids(
            self,
            user_ids: [int],
            update_data: SchemaUserUpdate,
            output_key: UserInfosOutputKey
    ) -> dict:

        repo_result = await self.repo_users.update_users_by_ids(
            user_ids=user_ids,
            data=update_data
        )

        output = self._packing_be_output_dict(
            output_key=output_key,
            input_data=repo_result
        )

        return output

    async def create_users(
            self,
            create_data: typing.List[SchemaUserCreate.dict],
            output_key: UserInfosOutputKey.id
    ) -> dict:

        repo_result = await self.repo_users.create_users(
            data=create_data
        )

        output = self._packing_be_output_dict(
            output_key=output_key,
            input_data=repo_result
        )

        return output

    async def delete_users_by_ids(
            self,
            user_ids: [int],
            output_key: UserInfosOutputKey) -> dict:

        repo_result = await self.repo_users.delete_users_by_ids(
            user_ids=user_ids,
        )

        output = self._packing_be_output_dict(
            output_key=output_key,
            input_data=repo_result
        )

        return output

    @staticmethod
    def _packing_be_output_dict(
            input_data: typing.List[ModelUser],
            output_key: str
    ) -> dict:

        """
        handle input_data be pydantic UserInfos.

        Args:
            input_data: [ModelUser, ModelUser]
            output_key: user_output data's key.

        Returns:
            {'test': User(email='test', id=4, hashed_password='test',
            is_active=False)}

        """

        output_data_dict = {}

        for each in input_data:
            each_data = SchemaUser(**each.__dict__)
            output_data_dict_key = getattr(each_data, output_key)
            output_data_dict[output_data_dict_key] = each_data

        return output_data_dict


