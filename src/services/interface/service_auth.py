import abc
from typing import Union

from src.message_bus.auth import events
from src.schemas.jwt_token import Token
from src.schemas.models.users import User


class IFServiceAuth(abc.ABC):

    @abc.abstractmethod
    def authenticate_user(self, event: events.AuthenticateUser) \
            -> Union[User, bool]:
        return NotImplemented

    @abc.abstractmethod
    def create_access_token(self, event: events.CreateAccessToken) -> Token:
        return NotImplemented

    @staticmethod
    @abc.abstractmethod
    def get_token_decode_data(event: events.GetTokenDecodeData):
        return NotImplemented

    @staticmethod
    @abc.abstractmethod
    def permissions_required_decorator(permissions):
        return NotImplemented



