import abc


class IFJWTTokenManager(abc.ABC):

    @abc.abstractmethod
    def create_access_token(self, data: dict) -> str:
        return NotImplemented

    @abc.abstractmethod
    def validate_token(self, token: str) -> bool:
        return NotImplemented

    @abc.abstractmethod
    def get_token_payload(self, token: str) -> dict:
        return NotImplemented
