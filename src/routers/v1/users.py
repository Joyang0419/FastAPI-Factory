from typing import List

from fastapi import APIRouter, Query, Depends, status, Response

from src.domains.users import commands, events, handlers
from src.schemas.models.users import UserCreate, UserUpdate
from src.schemas.routers.users import UserInfos
from src.schemas.routers.users import UserInfosOutputKey

router = APIRouter(
    prefix="/v1/users",
    tags=["v1/users"],
    responses={404: {"description": "Not found"}}
)


@router.get("/get_all_users", response_model=UserInfos)
async def get_all_users(
        output_key: UserInfosOutputKey,
        handler=Depends(handlers.UsersHandler),
):
    event = events.GetAllUsers(output_key=output_key)
    results = await handler.handle(event)
    data = results.pop(0)
    return UserInfos(data=data)


@router.get("/get_user_by_ids", response_model=UserInfos)
async def get_users_by_ids(
        output_key: UserInfosOutputKey,
        user_ids: List[int] = Query(
            default=None,
            example=[19]
        ),
        handler=Depends(handlers.UsersHandler)
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
async def create_users(
        output_key: UserInfosOutputKey,
        data: List[UserCreate],
        handler=Depends(handlers.UsersHandler)
):

    command = commands.CreateUsers(
        output_key=output_key,
        create_data=data
    )
    results = await handler.handle(command)
    data = results.pop(0)
    return UserInfos(data=data)


@router.delete(
    "/delete_users_by_ids",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_users_by_ids(
        output_key: UserInfosOutputKey,
        user_ids: List[int],
        handler=Depends(handlers.UsersHandler)
):
    command = commands.DeleteUsersByIDs(
        output_key=output_key,
        user_ids=user_ids,
    )
    results = await handler.handle(command)
    data: list = results.pop(0)

    if not data:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/update_users_by_ids", response_model=UserInfos)
async def update_users_by_ids(
        output_key: UserInfosOutputKey,
        user_ids: List[int],
        data: UserUpdate,
        handler=Depends(handlers.UsersHandler)
):
    command = commands.UpdateUsersByIDS(
        output_key=output_key,
        user_ids=user_ids,
        update_data=data
    )
    results = await handler.handle(command)
    data = results.pop(0)
    return UserInfos(data=data)
