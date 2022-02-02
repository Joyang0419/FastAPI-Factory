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
    async def test_create_access_token(
            self,
            test_event: events.AuthenticateUser,
            test_client
    ):
        """
        GIVEN
            - test_client.
            - payload setting

        WHEN test_client.post endpoint: /v1/auth/token

        THEN
            - assert response status code 200 or 401.
            - if response is 200, assert data isinstance token
        """
        payload = {
            'username': test_event.authenticate_data.email,
            'password': test_event.authenticate_data.password
        }

        async with test_client as ac:
            response = await ac.request(
                url="/v1/auth/token",
                method='POST',
                data=payload,
                headers={
                    'accept': 'application/json',
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            )

        assert response.status_code is status.HTTP_200_OK or \
               response.status_code is status.HTTP_401_UNAUTHORIZED

        if response.status_code is status.HTTP_200_OK:
            response_data = response.json()
            assert isinstance(response_data, dict)

    @pytest.mark.asyncio
    @pytest.mark.parametrize('token', [
        'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJGYXN0QVBJIEZhY3RvcnkiL'
        'CJzdWIiOiJKb3lhbmcwNDE5QGdtYWlsLmNvbSIsImV4cCI6MjI0MzY3MjU1NywibmJmIjo'
        'xNjQzNjcyNTU3LCJpYXQiOjE2NDM2NzI1NTd9.Bxn0ngH_e63zWO2FtlJpBSZY12PyHQ2k'
        'z_F7XYWGBEE'
    ])
    async def test_get_token_decode_data(self, test_client, token: str):
        """
        GIVEN
            - test_client.

        WHEN test_client.post endpoint: /v1/auth/get_token_user_data

        THEN
            - assert response status code 200 or 401.
            - if response is 200, assert data isinstance dict
        """
        async with test_client as ac:
            response = await ac.request(
                url="/v1/auth/get_token_user_data",
                method='GET',
                headers={
                    'accept': 'application/json',
                    'Authorization': f'Bearer {token}'
                }
            )

            assert response.status_code is status.HTTP_200_OK or \
                   response.status_code is status.HTTP_401_UNAUTHORIZED or \
                   response.status_code is status.HTTP_403_FORBIDDEN

            if response.status_code is status.HTTP_200_OK:
                response_data = response.json()
                assert isinstance(response_data, dict)
