from enum import Enum
from typing import Dict, Union

from pydantic import BaseModel

from src.schemas.models.users import User


class UserInfosError(BaseModel):
    message: str


class UserInfos(BaseModel):
    data: Dict[
        str,
        Union[User, UserInfosError]
    ]


class UserInfosOutputKey(str, Enum):
    email = 'email'
    id = 'id'
