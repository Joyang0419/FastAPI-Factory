from enum import Enum
from typing import Dict

from pydantic import BaseModel

from src.schemas.models.users import User


class UserInfos(BaseModel):
    data: Dict[str, User]


class UserInfosOutputKey(str, Enum):
    email = 'email'
    id = 'id'
