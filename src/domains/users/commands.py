from typing import List

from src.domains.base import Command
from src.schemas.models.users import (
    UserUpdate as SchemaUserUpdate,
    UserCreate as SchemaUserCreate
)
from src.schemas.routers.users import UserInfosOutputKey


class UpdateUsersByIDS(Command):
    user_ids: List[int]
    update_data: SchemaUserUpdate
    output_key: UserInfosOutputKey


class DeleteUsersByIDs(Command):
    output_key: UserInfosOutputKey
    user_ids: List[int]


class CreateUsers(Command):
    create_data: List[SchemaUserCreate]
    output_key: UserInfosOutputKey
