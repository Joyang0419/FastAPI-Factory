from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class UserAuthenticate(UserBase):
    password: str


class UserUpdate(UserBase):
    email: Optional[str]
    password: Optional[str]
    is_active: Optional[bool]


class User(UserBase):
    id: int
    password: str
    is_active: bool

    class Config:
        orm_mode = True
