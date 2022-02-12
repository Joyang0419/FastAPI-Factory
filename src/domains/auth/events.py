from src.domains.base import Event
from src.schemas.models.users import (
    UserAuthenticate
)
from src.schemas.routers.users import UserInfosOutputKey


class AuthenticateUser(Event):
    output_key: UserInfosOutputKey
    authenticate_data: UserAuthenticate


class GetTokenDecodeData(Event):
    token: str
