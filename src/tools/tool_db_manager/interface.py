import abc


class IFDBManager(abc.ABC):

    @abc.abstractmethod
    def get_db(self) -> list:
        return NotImplemented
