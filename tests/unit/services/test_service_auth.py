import pytest

from src.containers.container_services import ContainerServices
from src.schemas.routers.users import UserInfosOutputKey
from src.message_bus.auth import events
from src.schemas.models.users import UserAuthenticate
from src.schemas.jwt_token import Token


class TestServiceAuth:

    def setup(self):
        self.service_auth = ContainerServices().service_auth()

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        'event',
        [
            pytest.param(
                events.AuthenticateUser(
                    output_key=UserInfosOutputKey.email,
                    authenticate_data=UserAuthenticate(
                        email='sss',
                        password='sss'
                    )
                ),
                id='exist user'
            ),
            pytest.param(
                events.AuthenticateUser(
                    output_key=UserInfosOutputKey.email,
                    authenticate_data=UserAuthenticate(
                        email='aa',
                        password='aaa'
                    )
                ),
                id='no exist user'
            )
        ]
    )
    async def test_authenticate_user(self, event):
        """
        GIVEN an service_auth()

        WHEN service_auth().authenticate_user

        THEN assert isinstance(result, (bool, dict))
        """
        result = await self.service_auth.authenticate_user(event=event)
        assert isinstance(
            result,
            (bool, dict)
        )
