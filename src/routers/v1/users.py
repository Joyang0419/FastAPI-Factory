from typing import List

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Query, Depends

from src.container import Container
from src.schemas.models.users import UserCreate, UserUpdate
from src.schemas.routers.users import UserInfos
from src.services.svc_user import SVCUser

router = APIRouter(
    prefix="/v1/users",
    tags=["v1/users"],
    responses={404: {"description": "Not found"}}
)


@router.get("/get_all_users", response_model=UserInfos)
@inject
async def get_all_users(
        svc_user: SVCUser = Depends(Provide[Container.svc_user])
):

    return await svc_user.get_all_users()


@router.get("/get_user_by_ids", response_model=UserInfos)
@inject
async def get_user_by_ids(
        user_ids: List[int] = Query(
            default=None,
            example=[1, 2]
        ),
        svc_user: SVCUser = Depends(Provide[Container.svc_user])
):

    return await svc_user.get_user_by_ids(user_ids=user_ids)


@router.post("/create_user", response_model=UserInfos)
@inject
async def create_user(
        data: List[UserCreate],
        svc_user: SVCUser = Depends(Provide[Container.svc_user])
):

    return await svc_user.create_user(data=data)


@router.delete("delete_users", response_model=UserInfos)
@inject
async def delete_user_by_ids(
        user_ids: List[int],
        svc_user: SVCUser = Depends(Provide[Container.svc_user])
):

    return await svc_user.delete_user_by_ids(user_ids)


@router.put("/update_user", response_model=UserInfos)
@inject
async def update_user_by_ids(
        user_ids: List[int],
        data: UserUpdate,
        svc_user: SVCUser = Depends(Provide[Container.svc_user])
):

    return await svc_user.update_user_by_ids(
        user_ids=user_ids,
        data=data.dict()
    )
