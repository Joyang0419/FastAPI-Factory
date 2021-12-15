from typing import List

from fastapi import APIRouter, Query

from src.schemas.models.items import ItemCreate, ItemUpdate
from src.schemas.routers.items import ItemInfos
from src.services.service_item import ServiceItem

router = APIRouter(
    prefix="/v1/items",
    tags=["v1/items"],
    responses={404: {"description": "Not found"}},
)


@router.post("/create_item", response_model=ItemInfos)
async def create_item(pydantic_models: List[ItemCreate]):
    service = ServiceItem()

    return await service.create_item(pydantic_models)


@router.get("/get_all_items", response_model=ItemInfos)
async def get_all_items():
    service = ServiceItem()

    return await service.get_all_items()


@router.get("/get_item_by_ids", response_model=ItemInfos)
async def get_user_by_ids(
        item_ids: List[int] = Query(
            default=None,
            example=[1, 2]
        )
):
    service = ServiceItem()

    return await service.get_item_by_ids(item_ids=item_ids)


@router.put("/update_item", response_model=ItemInfos)
async def update_item_by_ids(item_ids: List[int], pydantic_model: ItemUpdate):
    service = ServiceItem()

    return await service.update_item_by_ids(
        item_ids=item_ids,
        pydantic_model=pydantic_model
    )


@router.delete("delete_items", response_model=ItemInfos)
async def delete_user_by_ids(item_ids: List[int]):
    service = ServiceItem()

    return await service.delete_item_by_ids(item_ids)
