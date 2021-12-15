from typing import Dict

from pydantic import BaseModel

from src.schemas.models.users import UserItem, User


class UserItemInfos(BaseModel):
    data: Dict[str, UserItem]


class UserInfos(BaseModel):
    data: Dict[str, User]
