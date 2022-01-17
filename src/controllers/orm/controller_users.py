import typing

from src.controllers.interface.controller_users import IFControllerUsers
from src.schemas.models.users import (
    UserCreate,
    UserUpdate
)
from src.schemas.routers.users import (
    UserInfos,
    UserInfosOutputKey
)
from src.services.orm.service_users import IMPServiceUsers


class IMPControllerUsers(IFControllerUsers):

    def __init__(
            self,
            service_users: IMPServiceUsers,
    ):
        self.service_users = service_users

    async def get_all_users(self, output_key: UserInfosOutputKey) -> UserInfos:
        """

        Args:
            output_key: enum_data: UserInfosOutputKey

        Returns:

        """
        data = await self.service_users.get_all_users(output_key=output_key)
        output = UserInfos(data=data)

        return output

    async def get_users_by_ids(
            self,
            user_ids: [int],
            output_key: UserInfosOutputKey
    ) -> UserInfos:
        """

        Args:
            user_ids: get users condition by this attribute.
            output_key: enum_data: UserInfosOutputKey

        Returns:

        """
        data = await self.service_users.get_users_by_ids(
            user_ids=user_ids,
            output_key=output_key
        )
        output = UserInfos(data=data)

        return output

    async def create_users(
            self,
            create_data: typing.List[UserCreate],
            output_key: UserInfosOutputKey
    ) -> UserInfos:
        """

        Args:
            create_data: pydantic model
            output_key: enum_data: UserInfosOutputKey

        Returns:

        """
        data = await self.service_users.create_users(
            create_data=create_data,
            output_key=output_key
        )
        output = UserInfos(data=data)

        return output

    async def update_users_by_ids(
            self,
            user_ids: [int],
            update_data: UserUpdate,
            output_key: UserInfosOutputKey
    ) -> UserInfos:
        """

        Args:
            user_ids: get users condition by this attribute.
            update_data: pydantic model
            output_key: enum_data: UserInfosOutputKey

        Returns:

        """

        data = await self.service_users.update_users_by_ids(
            user_ids=user_ids,
            update_data=update_data,
            output_key=output_key
        )
        output = UserInfos(data=data)

        return output

    async def delete_users_by_ids(
            self,
            user_ids: [int],
            output_key: UserInfosOutputKey
    ) -> UserInfos:
        """
        handled input_data for router: user, endpoint: delete_user_by_ids use.

        Args:
            user_ids: get users condition by this attribute.
            output_key: enum_data: UserInfosOutputKey

        Returns:

        """

        data = await self.service_users.delete_users_by_ids(
            user_ids=user_ids,
            output_key=output_key
        )
        output = UserInfos(data=data)

        return output
