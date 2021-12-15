from typing import Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    user_id: int


class ItemUpdate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
