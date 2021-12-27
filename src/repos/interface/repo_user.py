import abc
from src.repos.interface.repo_base import IFRepoBase


class IFRepoUser(IFRepoBase, abc.ABC):

    @abc.abstractmethod
    def user_create_item(self, user_id: int, item: dict):
        return NotImplemented
