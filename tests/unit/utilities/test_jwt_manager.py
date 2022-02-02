from datetime import (
    datetime,
    timedelta
)

import jwt
import pytest

from src.containers.container_utilities import ContainerUtilities
from src.schemas.jwt_token import JWTTokenPayload


class TestJWTManager:

    def setup(self):
        """
        set attribute:
            jwt_manager()
        """
        self.jwt_manager = ContainerUtilities().jwt_manager()

    @pytest.mark.parametrize(
        'test_payload', [
            JWTTokenPayload(sub=1)
        ]
    )
    def test_create_access_token(self, test_payload: JWTTokenPayload):
        """
        GIVEN an jwt_manager()

        WHEN jwt_manager().create_access_token()

        THEN assert instance str
        """
        result = self.jwt_manager.create_access_token(
            data=test_payload
        )
        assert isinstance(result, str)

    @pytest.mark.parametrize(
        'test_payload', [
            pytest.param(
                JWTTokenPayload(
                    sub=1,
                    exp=datetime.utcnow() + timedelta(minutes=1)
                ),
                id='Normal case'
            ),
            pytest.param(
                JWTTokenPayload(
                    sub=1,
                    exp=datetime.utcnow() - timedelta(minutes=1)
                ),
                id='Fail case'
            ),
        ]
    )
    def test_validate_token(self, test_payload):
        """
        GIVEN jwt_manager()

        WHEN
            - jwt_manager.create_token
            - jwt_manager.validate_toke

        THEN assert validate_token is bool
        """
        token = self.jwt_manager.create_access_token(
            data=test_payload
        )

        is_token = self.jwt_manager.validate_token(token=token)

        assert isinstance(is_token, bool)

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        'token_payload', [
            pytest.param(
                JWTTokenPayload(
                    sub=1,
                    exp=datetime.utcnow() + timedelta(minutes=1)
                ),
                id='Normal case'
            ),
        ]
    )
    async def test_get_token_payload(self, token_payload: JWTTokenPayload):
        """
        GIVEN jwt_manager()

        WHEN
            - jwt_manager
            - jwt_manager.get_token_payload

        THEN assert result is dict
        """
        token = self.jwt_manager.create_access_token(data=token_payload)

        payload = await self.jwt_manager.get_token_payload(token=token)

        assert isinstance(payload, dict)

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        'test_token', [
            pytest.param(
                'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3Mi'
                'OiJGYXN0QVBJIEZhY3RvcnkiLCJzdWIiOiIxIiwiZXhwI'
                'joxNjQzNDcyMTc5LCJuYmYiOjE2NDMzODU3NzksImlhdC'
                'I6MTY0MzM4NTc3OX0.uC1dQXNYe0AT9Ear5HJsnsJZSu-Q27j4avR2a6n13f3',
                id='Fail case'
            ),
        ]
    )
    async def test_get_token_payload_failed(self, test_token: str):
        """
        GIVEN jwt_manager()

        WHEN
            - jwt_manager.get_token_payload

        THEN
            - assert result is error
        """
        with pytest.raises(jwt.exceptions.PyJWTError):
            await self.jwt_manager.get_token_payload(token=test_token)
