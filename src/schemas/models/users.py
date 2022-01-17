from typing import Optional

from pydantic import BaseModel


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
    hashed_password: str
    is_active: bool

    class Config:
        orm_mode = True
