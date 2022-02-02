from datetime import datetime, timedelta

from pydantic import BaseModel

from src.configs.config import (
    TokenConfig,
    ApplicationConfig
)


class JWTTokenPayload(BaseModel):
    iss: str = ApplicationConfig().title
    sub: str
    exp: datetime = datetime.utcnow() + timedelta(
        minutes=TokenConfig().access_token_expire_minutes
    )
    nbf: datetime = datetime.utcnow()
    iat: datetime = datetime.utcnow()


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'
