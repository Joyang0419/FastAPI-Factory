from typing import List

from src.domains.base import Event
from src.schemas.routers.users import UserInfosOutputKey


class GetAllUsers(Event):
    output_key: UserInfosOutputKey


class GetUsersByIDs(Event):
    output_key: UserInfosOutputKey
    user_ids: List[int]


class Notification(Event):
    message: str
