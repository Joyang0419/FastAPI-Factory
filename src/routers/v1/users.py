from typing import List

from fastapi import APIRouter, Query

from src.schemas.models.users import UserCreate, UserUpdate
from src.schemas.routers.users import UserItemInfos, UserInfos
from src.services.service_user import ServiceUser

router = APIRouter(
    prefix="/v1/users",
    tags=["v1/users"],
    responses={404: {"description": "Not found"}}
)


@router.get("/get_user_by_ids", response_model=UserItemInfos)
async def get_user_by_ids(
        user_ids: List[int] = Query(
            default=None,
            example=[43, 44]
        )
):
    service = ServiceUser()

    return await service.get_user_by_ids(user_ids=user_ids)


@router.get("/get_all_users", response_model=UserItemInfos)
async def get_all_users():
    service = ServiceUser()

    return await service.get_all_users()


@router.post("/create_user", response_model=UserInfos)
async def create_user(pydantic_models: List[UserCreate]):
    service = ServiceUser()

    return await service.create_user(pydantic_models=pydantic_models)


@router.put("/update_user", response_model=UserInfos)
async def update_user_by_ids(user_ids: List[int], pydantic_model: UserUpdate):
    service = ServiceUser()

    return await service.update_user_by_ids(
        user_ids=user_ids,
        pydantic_model=pydantic_model
    )


@router.delete("delete_users", response_model=UserInfos)
async def delete_user_by_ids(user_ids: List[int]):
    service = ServiceUser()

    return await service.delete_user_by_ids(user_ids)
