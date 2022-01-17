import abc
import typing


class IFRepoUser(abc.ABC):

    @abc.abstractmethod
    def get_all_users(self) -> list:
        return NotImplemented

    @abc.abstractmethod
    def get_users_by_ids(self, user_ids: list) -> list:
        return NotImplemented

    @abc.abstractmethod
    def delete_users_by_ids(self, user_ids: list):
        return NotImplemented

    @abc.abstractmethod
    def update_users_by_ids(self, user_ids: list, data: dict):
        return NotImplemented

    @abc.abstractmethod
    def create_users(self, data: typing.List[dict]):
        return NotImplemented
