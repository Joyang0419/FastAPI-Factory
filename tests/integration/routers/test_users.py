import pytest
from fastapi import status
from httpx import AsyncClient

from src.schemas.models.users import UserCreate, UserUpdate
from src.schemas.routers.users import UserInfosOutputKey


class TestUsers:

    @pytest.fixture(autouse=True)
    def setup(self, test_client: AsyncClient):
        """
        Args:
            test_client:

        Returns:

        """
        self.client = test_client

    @pytest.mark.parametrize(
        "test_case", [
            pytest.param(
                UserInfosOutputKey.id.value,
                id="Normal Case"
            )
        ]
    )
    @pytest.mark.asyncio
    async def test_get_all_users(
            self,
            test_case: UserInfosOutputKey,
            test_client
    ):
        """
        GIVEN test_client.

        WHEN test_client.get endpoint: /v1/users/get_all_users.

        THEN
            - assert response status code.
            - assert data in response_data.
        Args:
            test_case:

        Returns:

        """

        async with test_client as ac:
            response = await ac.request(
                url="/v1/users/get_all_users",
                method='GET',
                params={'output_key': test_case}
            )
        assert response.status_code == status.HTTP_200_OK
        response_data = response.json()
        assert 'data' in response_data

    @pytest.mark.parametrize(
        "test_case", [
            pytest.param(
                {
                    'output_key': UserInfosOutputKey.id.value,
                    'user_ids': [1, 2]
                },
                id="Normal Case"
            )
        ]
    )
    @pytest.mark.asyncio
    async def test_get_users_by_ids(self, test_case, test_client):
        """
        GIVEN test_client.

        WHEN test_client.get endpoint: /v1/users/get_users_by_ids.

        THEN
            - assert response status code.
            - assert data in response_data.
        Args:
            test_case:

        Returns:

        """
        async with test_client as ac:
            response = await ac.request(
                url="/v1/users/get_user_by_ids",
                method='GET',
                params={
                    'output_key': test_case['output_key'],
                    'user_ids': test_case['user_ids']
                }
            )
        assert response.status_code == status.HTTP_200_OK

        response_data = response.json()

        assert 'data' in response_data

    @pytest.mark.parametrize(
        "test_case", [
            pytest.param(
                {
                    'output_key': UserInfosOutputKey.id.value,
                    'user_ids': [19]
                },
                id="Normal Case1"
            )
        ]
    )
    @pytest.mark.asyncio
    async def test_delete_users_by_ids(self, test_case):
        """
        GIVEN test_client.

        WHEN test_client.get endpoint: /v1/users/delete_users_by_ids.

        THEN
            - assert response status code.
        Args:
            test_case:

        Returns:

        """
        async with self.client as ac:
            response = await ac.request(
                url="/v1/users/delete_users_by_ids",
                method='DELETE',
                params={
                    'output_key': test_case['output_key'],
                },
                json=test_case['user_ids']
            )

        assert response.status_code in [
            status.HTTP_204_NO_CONTENT,
            status.HTTP_404_NOT_FOUND
        ]

    @pytest.mark.parametrize(
        "test_case", [
            pytest.param(
                {
                    'output_key': UserInfosOutputKey.id.value,
                    'data': [
                        UserCreate(
                            email='test_email1',
                            password='test_pwd'
                        ).dict()
                    ]
                },
                id="Normal Case"
            )
        ]
    )
    @pytest.mark.asyncio
    async def test_create_users(self, test_case):
        """
        GIVEN test_client.

        WHEN test_client.get endpoint: v1/users/create_users.

        THEN
            - assert response status code.
            - assert data in response_data.
        Args:
            test_case:

        Returns:

        """
        async with self.client as ac:
            response = await ac.request(
                url='v1/users/create_users',
                params={
                    'output_key': test_case['output_key'],
                },
                method='POST',
                json=test_case['data']
            )

        assert response.status_code is status.HTTP_201_CREATED

        response_data = response.json()

        assert 'data' in response_data

    @pytest.mark.parametrize(
        "test_case", [
            pytest.param(
                {
                    'output_key': UserInfosOutputKey.id.value,
                    'user_ids': [96],
                    'data': UserUpdate(
                            hashed_password='test_pwd1'
                        ).dict(exclude_none=True)
                },
                id="Normal Case"
            )
        ]
    )
    @pytest.mark.asyncio
    async def test_update_users_by_ids(self, test_case):
        """
        GIVEN test_client.

        WHEN test_client.get endpoint: /v1/users/update_users_by_ids.

        THEN
            - assert response status code.
            - assert data in response_data.
        """
        payload = {
            'user_ids': test_case['user_ids'],
            'data': test_case['data']
        }
        async with self.client as ac:
            response = await ac.request(
                url='v1/users/update_users_by_ids',
                params={
                    'output_key': test_case['output_key'],
                },
                method='PATCH',
                json=payload
            )

        assert response.status_code is status.HTTP_200_OK

        response_data = response.json()

        assert 'data' in response_data

        assert response.status_code is status.HTTP_200_OK

        response_data = response.json()

        assert 'data' in response_data
