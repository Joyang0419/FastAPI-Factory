from typing import Dict

from pydantic import BaseModel

from src.schemas.models.items import Item


class ItemInfos(BaseModel):
    data: Dict[str, Item]
