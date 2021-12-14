from typing import List, Optional

from pydantic import BaseModel

from src.schemas.models.items import Item


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    hashed_password: str


class UserUpdate(UserBase):
    email: Optional[str]
    hashed_password: Optional[str]
    is_active: Optional[bool]


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
