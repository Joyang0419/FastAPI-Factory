from typing import List

from dependency_injector.wiring import inject
from fastapi import APIRouter, Query, Depends, status, Response

from src.message_bus.users import events
from src.message_bus.users.handler import UsersHandler
from src.schemas.models.users import UserCreate, UserUpdate
from src.schemas.routers.users import UserInfos
from src.schemas.routers.users import UserInfosOutputKey

router = APIRouter(
    prefix="/v1/users",
    tags=["v1/users"],
    responses={404: {"description": "Not found"}}
)


@router.get("/get_all_users", response_model=UserInfos)
@inject
async def get_all_users(
        output_key: UserInfosOutputKey,
        handler=Depends(UsersHandler)
):
    event = events.GetAllUsers(output_key=output_key)
    results = await handler.handle(event)
    data = results.pop(0)
    return UserInfos(data=data)


@router.get("/get_user_by_ids", response_model=UserInfos)
@inject
async def get_users_by_ids(
        output_key: UserInfosOutputKey,
        user_ids: List[int] = Query(
            default=None,
            example=[19]
        ),
        handler=Depends(UsersHandler)
):
    event = events.GetUsersByIDs(
        output_key=output_key,
        user_ids=user_ids
    )
    results = await handler.handle(event)
    data = results.pop(0)
    return UserInfos(data=data)


@router.post(
    "/create_users",
    response_model=UserInfos,
    status_code=status.HTTP_201_CREATED
)
@inject
async def create_users(
        output_key: UserInfosOutputKey,
        data: List[UserCreate],
        handler=Depends(UsersHandler)
):

    event = events.CreateUsers(
        output_key=output_key,
        create_data=data
    )
    results = await handler.handle(event)
    data = results.pop(0)
    return UserInfos(data=data)


@router.delete(
    "/delete_users_by_ids",
    status_code=status.HTTP_204_NO_CONTENT
)
@inject
async def delete_users_by_ids(
        output_key: UserInfosOutputKey,
        user_ids: List[int],
        handler=Depends(UsersHandler)
):
    event = events.DeleteUsersByIDs(
        output_key=output_key,
        user_ids=user_ids,
    )
    results = await handler.handle(event)
    data: list = results.pop(0)

    if not data:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/update_users_by_ids", response_model=UserInfos)
@inject
async def update_users_by_ids(
        output_key: UserInfosOutputKey,
        user_ids: List[int],
        data: UserUpdate,
        handler=Depends(UsersHandler)
):
    event = events.UpdateUsersByIDS(
        output_key=output_key,
        user_ids=user_ids,
        update_data=data
    )
    results = await handler.handle(event)
    data = results.pop(0)
    return UserInfos(data=data)
