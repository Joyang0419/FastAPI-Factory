from typing import List

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Query, Depends, status, Response

from src.containers.container_controllers import ContainerControllers
from src.controllers.orm.controller_users import IMPControllerUsers
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
        controller_users: IMPControllerUsers = Depends(
            Provide[ContainerControllers.controller_users]
        )
):

    return await controller_users.get_all_users(output_key=output_key)


@router.get("/get_user_by_ids", response_model=UserInfos)
@inject
async def get_users_by_ids(
        output_key: UserInfosOutputKey,
        user_ids: List[int] = Query(
            default=None,
            example=[19]
        ),
        controller_users: IMPControllerUsers = Depends(
            Provide[ContainerControllers.controller_users]
        )
):

    return await controller_users.get_users_by_ids(
        user_ids=user_ids,
        output_key=output_key
    )


@router.post(
    "/create_users",
    response_model=UserInfos,
    status_code=status.HTTP_201_CREATED
)
@inject
async def create_users(
        output_key: UserInfosOutputKey,
        data: List[UserCreate],
        controller_users: IMPControllerUsers = Depends(
            Provide[ContainerControllers.controller_users]
        )
):

    return await controller_users.create_users(
        create_data=data,
        output_key=output_key
    )


@router.delete(
    "/delete_users_by_ids",
    status_code=status.HTTP_204_NO_CONTENT
)
@inject
async def delete_users_by_ids(
        output_key: UserInfosOutputKey,
        user_ids: List[int],
        controller_users: IMPControllerUsers = Depends(
            Provide[ContainerControllers.controller_users]
        )
):
    delete_users = await controller_users.delete_users_by_ids(
        user_ids=user_ids,
        output_key=output_key
    )

    if not delete_users:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/update_users_by_ids", response_model=UserInfos)
@inject
async def update_users_by_ids(
        output_key: UserInfosOutputKey,
        user_ids: List[int],
        data: UserUpdate,
        controller_users: IMPControllerUsers = Depends(
            Provide[ContainerControllers.controller_users]
        )
):
    return await controller_users.update_users_by_ids(
        output_key=output_key,
        user_ids=user_ids,
        update_data=data
    )
