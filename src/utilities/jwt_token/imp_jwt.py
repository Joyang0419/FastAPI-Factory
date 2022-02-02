import jwt
from src.schemas.jwt_token import JWTTokenPayload
from src.utilities.jwt_token.interface import IFJWTTokenManager
from src.configs.config import TokenConfig
from typing import Optional

token_config = TokenConfig()


class IMPJWTManager(IFJWTTokenManager):
    secret_key = token_config.secret_key
    algorithm = token_config.algorithm

    @classmethod
    def create_access_token(cls, data: JWTTokenPayload) -> str:
        token = jwt.encode(
            payload=data.dict(),
            key=cls.secret_key,
            algorithm=cls.algorithm
        )
        return token

    @classmethod
    def validate_token(cls, token: str) -> bool:
        try:
            token_payload = jwt.decode(
                jwt=token,
                key=cls.secret_key,
                algorithms=[cls.algorithm]
            )
        except jwt.exceptions.PyJWTError:
            return False

        return bool(token_payload)

    @classmethod
    async def get_token_payload(cls, token: str) -> Optional[dict]:
        try:
            token_payload = jwt.decode(
                jwt=token,
                key=cls.secret_key,
                algorithms=[cls.algorithm]
            )
        except jwt.exceptions.PyJWTError as error:
            raise error

        return token_payload


if __name__ == '__main__':
    a = IMPJWTManager()
    data = JWTTokenPayload(sub='Joyang0419@gmail.com')
    print(a.create_access_token(data))

