import abc


class IFCryptManager(abc.ABC):

    @abc.abstractmethod
    def get_pwd_hash(self, pwd: str) -> str:
        return NotImplemented

    @abc.abstractmethod
    def verify_pwd(
            self,
            plain_pwd: str,
            hashed_pwd: str
    ) -> bool:
        return NotImplemented
