from fastapi import (
    APIRouter,
    Depends,
    status,
    HTTPException
)

from src.message_bus.auth import events
from src.message_bus.auth.handler import AuthHandler
from src.schemas.models.users import UserAuthenticate
from src.schemas.routers.users import (
    UserInfos,
    UserInfosOutputKey,
)

router = APIRouter(
    prefix="/v1/auth",
    tags=["v1/auth"],
    responses={404: {"description": "Not found"}}
)


@router.post('/authenticate_user')
async def authenticate_user(
        output_key: UserInfosOutputKey,
        data: UserAuthenticate,
        handler=Depends(AuthHandler)
):
    event = events.AuthenticateUser(
        output_key=output_key,
        authenticate_data=data
    )
    results = await handler.handle(event)
    data = results.pop(0)

    if not data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

    return UserInfos(data=data)
