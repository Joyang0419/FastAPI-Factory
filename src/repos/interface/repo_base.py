import abc
from typing import List


class IFRepoBase(abc.ABC):

    @abc.abstractmethod
    def get_all(self) -> list:
        return NotImplemented

    @abc.abstractmethod
    def get_by_ids(self, primary_ids: list) -> list:
        return NotImplemented

    @abc.abstractmethod
    def delete_by_ids(self, primary_ids: list):
        return NotImplemented

    @abc.abstractmethod
    def update_by_ids(self, primary_ids: list, data: dict):
        return NotImplemented

    @abc.abstractmethod
    def insert(self, data: List[dict]):
        return NotImplemented
