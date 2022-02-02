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
from src.schemas.jwt_token import Token, JWTTokenPayload
from fastapi.security import OAuth2PasswordRequestForm
from src.dependencies import (
    get_security,
    get_permissions_required_decorator
)
from src.configs.permissions import RolePermissions

router = APIRouter(
    prefix="/v1/auth",
    tags=["v1/auth"],
    responses={404: {"description": "Not found"}}
)


@router.post('/authenticate_user', response_model=UserInfos)
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


@router.post('/token', response_model=Token)
async def create_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        handler=Depends(AuthHandler)
):
    event = events.CreateAccessToken(
        authenticate_data=UserAuthenticate(
            email=form_data.username,
            password=form_data.password
        )
    )
    results = await handler.handle(event)
    data = results.pop(0)

    if not data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return data


@router.get('/get_token_user_data', response_model=JWTTokenPayload)
@get_permissions_required_decorator(RolePermissions.Admin.permissions)
async def get_token_decode_data(
        token: str = Depends(get_security()),
        handler=Depends(AuthHandler),
):
    event = events.GetTokenDecodeData(
        token=token
    )
    results = await handler.handle(event)
    data = results.pop(0)

    if not data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return data


