from typing import List

from pydantic import BaseModel

from src.schemas.routers.users import UserInfosOutputKey
from src.schemas.models.users import (
    UserUpdate as SchemaUserUpdate,
    UserCreate as SchemaUserCreate
)


class Event(BaseModel):
    pass


class GetAllUsers(Event):
    output_key: UserInfosOutputKey


class GetUsersByIDs(Event):
    output_key: UserInfosOutputKey
    user_ids: List[int]


class UpdateUsersByIDS(Event):
    user_ids: List[int]
    update_data: SchemaUserUpdate
    output_key: UserInfosOutputKey


class DeleteUsersByIDs(Event):
    output_key: UserInfosOutputKey
    user_ids: List[int]


class CreateUsers(Event):
    create_data: List[SchemaUserCreate]
    output_key: UserInfosOutputKey


class Notification(Event):
    message: str
