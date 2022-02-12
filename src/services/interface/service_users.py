import abc
from src.domains.users import events, commands


class IFServiceUsers(abc.ABC):

    @abc.abstractmethod
    def get_all_users(
            self,
            event: events.GetAllUsers
    ) -> dict:

        return NotImplemented

    @abc.abstractmethod
    def get_users_by_ids(
            self,
            event: events.GetUsersByIDs
    ) -> dict:

        return NotImplemented

    @abc.abstractmethod
    def update_users_by_ids(
            self,
            command: commands.UpdateUsersByIDS
    ) -> dict:

        return NotImplemented

    @abc.abstractmethod
    def create_users(
            self,
            command: commands.CreateUsers
    ) -> dict:

        return NotImplemented

    @abc.abstractmethod
    def delete_users_by_ids(
            self,
            command: commands.DeleteUsersByIDs
    ) -> dict:

        return NotImplemented

    @abc.abstractmethod
    def send_notification(self, event: events.Event):
        return NotImplemented
