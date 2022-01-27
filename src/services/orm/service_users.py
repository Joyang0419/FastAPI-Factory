import typing

from src.containers.container_utilities import ContainerUtilities
from src.message_bus.users import events
from src.models.users import User as ModelUser
from src.repos.orm.repo_users import IMPRepoUsers
from src.schemas.models.users import (
    User as SchemaUser
)
from src.services.interface.service_users import IFServiceUsers

container_utilities = ContainerUtilities()
crypt_manager = container_utilities.crypt_manager()


class IMPServiceUsers(IFServiceUsers):
    """
    Purpose: Handle repo_user return, let Controller_users use.
    """

    def __init__(
            self,
            repo_users: IMPRepoUsers,
    ):
        self.repo_users = repo_users
        self.events = []

    async def get_all_users(
            self,
            event: events.GetAllUsers
    ) -> dict:

        repo_result = await self.repo_users.get_all_users()
        if repo_result:
            handled_data = self._packing_be_output_dict(
                input_data=repo_result,
                output_key=event.output_key
            )
            return handled_data
        else:
            return {}

    async def get_users_by_ids(
            self,
            event: events.GetUsersByIDs
    ) -> dict:

        repo_result = await self.repo_users.get_users_by_ids(
            user_ids=event.user_ids
        )
        handled_data = self._packing_be_output_dict(
            output_key=event.output_key,
            input_data=repo_result
        )

        return handled_data

    async def update_users_by_ids(
            self,
            event: events.UpdateUsersByIDS
    ) -> dict:
        output = {}

        if event.update_data.password:
            event.update_data.password = self._hash_pwd(
                event.update_data.password
            )

        repo_result = await self.repo_users.update_users_by_ids(
            user_ids=event.user_ids,
            data=event.update_data
        )

        if repo_result:

            output = self._packing_be_output_dict(
                output_key=event.output_key,
                input_data=repo_result
            )

            for each_user in output.values():
                event = events.Notification(
                    message=f"User id: {each_user.id}, data updated."
                )
                self.events.append(event)

        return output

    async def create_users(
            self,
            event: events.CreateUsers
    ) -> dict:

        for each in event.create_data:
            each.password = self._hash_pwd(each.password)

        repo_result = await self.repo_users.create_users(
            data=event.create_data
        )

        output = self._packing_be_output_dict(
            output_key=event.output_key,
            input_data=repo_result
        )

        for each_user in output.values():
            event = events.Notification(
                message=f"User id: {each_user.id}, created."
            )
            self.events.append(event)

        return output

    @staticmethod
    def _hash_pwd(pwd: str) -> str:
        return crypt_manager.get_pwd_hash(pwd=pwd)

    async def delete_users_by_ids(
            self,
            event: events.DeleteUsersByIDs
    ) -> dict:
        output = {}

        repo_result = await self.repo_users.delete_users_by_ids(
            user_ids=event.user_ids,
        )

        if repo_result:
            output = self._packing_be_output_dict(
                output_key=event.output_key,
                input_data=repo_result
            )

            for each_user in output.values():
                event = events.Notification(
                    message=f"User id: {each_user.id}, deleted."
                )
                self.events.append(event)

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

    def collect_new_events(self):
        while self.events:
            yield self.events.pop(0)

    def send_notification(self, event: events.Notification) -> bool:
        return container_utilities.notification_manager().send_notification(
            message=event.message
        )
