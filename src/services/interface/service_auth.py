import abc
from typing import Union

from src.message_bus.auth import events
from src.schemas.models.users import User


class IFServiceAuth(abc.ABC):

    @abc.abstractmethod
    def authenticate_user(self, event: events.AuthenticateUser) \
            -> Union[User, bool]:
        return NotImplemented
