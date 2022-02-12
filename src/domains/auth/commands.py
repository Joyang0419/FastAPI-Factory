from src.domains.base import Command
from src.schemas.models.users import (
    UserAuthenticate
)


class CreateAccessToken(Command):
    authenticate_data: UserAuthenticate
