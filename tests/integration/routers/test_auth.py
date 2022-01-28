import pytest
from fastapi import status
from httpx import AsyncClient

from src.message_bus.auth import events
from src.schemas.models.users import UserAuthenticate
from src.schemas.routers.users import UserInfosOutputKey


class TestAuth:

    @pytest.fixture(autouse=True)
    def setup(self, test_client: AsyncClient):
        """
        Args:
            test_client:

        Returns:

        """
        self.client = test_client

    @pytest.mark.parametrize(
        "test_event", [
            pytest.param(
                events.AuthenticateUser(
                    output_key=UserInfosOutputKey.id.value,
                    authenticate_data=UserAuthenticate(
                        email='sss',
                        password='sss'
                    )
                ),
                id='events.AuthenticateUse'
            ),
            pytest.param(
                events.AuthenticateUser(
                    output_key=UserInfosOutputKey.id.value,
                    authenticate_data=UserAuthenticate(
                        email='incorrect email',
                        password='sss'
                    )
                ),
                id='incorrect email got 401 response code'
            )
        ]
    )
    @pytest.mark.asyncio
    async def test_authenticate_user(
            self,
            test_event: events.AuthenticateUser,
            test_client
    ):
        """
        GIVEN
            - test_client.
            - payload setting

        WHEN test_client.post endpoint: /v1/auth/authenticate_user.

        THEN
            - assert response status code 200 or 401.
            - if response is 200, assert data in response_data.
        """
        payload = {
            'email': test_event.authenticate_data.email,
            'password': test_event.authenticate_data.password
        }

        async with test_client as ac:
            response = await ac.request(
                url="/v1/auth/authenticate_user",
                method='POST',
                params={'output_key': test_event.output_key.value},
                json=payload
            )

        assert response.status_code is status.HTTP_200_OK or \
               response.status_code is status.HTTP_401_UNAUTHORIZED

        if response.status_code is status.HTTP_200_OK:
            response_data = response.json()
            assert 'data' in response_data
