from pydantic import BaseModel

from src.schemas.models.users import (
    UserAuthenticate
)
from src.schemas.routers.users import UserInfosOutputKey


class Event(BaseModel):
    pass


class AuthenticateUser(Event):
    output_key: UserInfosOutputKey
    authenticate_data: UserAuthenticate


class CreateAccessToken(Event):
    authenticate_data: UserAuthenticate


class GetTokenDecodeData(Event):
    token: str
