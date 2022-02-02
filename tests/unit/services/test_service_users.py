import pytest

from src.containers.container_services import ContainerServices
from src.message_bus.users import events
from src.schemas.models.users import UserCreate, UserUpdate
from src.schemas.routers.users import UserInfosOutputKey


class TestServiceUsers:

    def setup(self):
        self.service_users = ContainerServices().service_users()

    @pytest.mark.asyncio
    async def test_get_all_users(self):
        """
        GIVEN an service_users()

        WHEN service_users().get_all_users()

        THEN assert isinstance(output, dict)
        """
        event = events.GetAllUsers(output_key=UserInfosOutputKey.id)
        output = await self.service_users.get_all_users(
            event=event
        )

        assert isinstance(output, dict)

    @pytest.mark.parametrize(
        "test_case", [
            pytest.param(
                {
                    'user_ids': [4],
                },
                id='get user id: 4'
            ),
        ]
    )
    @pytest.mark.asyncio
    async def test_get_users_by_ids(self, test_case):
        """
        GIVEN an service_users()
        WHEN service_users().get_users_by_ids()
        THEN assert isinstance(output, dict)

        Args:
            test_case:

        Returns:

        """

        event = events.GetUsersByIDs(
            output_key=UserInfosOutputKey.id,
            user_ids=test_case['user_ids']

        )

        output = await self.service_users.get_users_by_ids(
            event=event
        )

        assert isinstance(output, dict)

    @pytest.mark.parametrize(
        "test_case", [
            pytest.param(
                {
                    'insert_data': [
                        UserCreate(
                            email='test_1_email',
                            password='test_1_pwd'
                        )
                    ]
                },
                id='insert user: test_1_email'
            ),
        ]
    )
    @pytest.mark.asyncio
    async def test_create_users(self, test_case):
        """
        GIVEN an service_users()
        WHEN service_users().create_users
        THEN assert isinstance(output, dict)

        Args:
            test_case:

        Returns:

        """

        event = events.CreateUsers(
            create_data=test_case['insert_data'],
            output_key=UserInfosOutputKey.email
        )

        output = await self.service_users.create_users(
            event=event
        )

        assert isinstance(output, dict)

    @pytest.mark.parametrize(
        "test_case", [
            pytest.param(
                {
                    'user_ids': [4],
                    'update_data': UserUpdate(is_active=False)
                },
                id='update user id: 4, is_active: 0'
            ),
        ]
    )
    @pytest.mark.asyncio
    async def test_update_users_by_ids(self, test_case):
        """
        GIVEN an service_users()
        WHEN service_users().update_users_by_ids
        THEN assert isinstance(output, dict)

        Args:
            test_case:

        Returns:

        """

        event = events.UpdateUsersByIDS(
            user_ids=test_case['user_ids'],
            update_data=test_case['update_data'],
            output_key=UserInfosOutputKey.id
        )

        output = await self.service_users.update_users_by_ids(event)

        assert isinstance(output, dict)

    @pytest.mark.parametrize(
        "test_case", [
            pytest.param(
                {
                    'user_ids': [4]
                },
                id='users delete'
            ),
        ]
    )
    @pytest.mark.asyncio
    async def test_delete_users_by_ids(self, test_case):
        """
        GIVEN an service_users()
        WHEN service_users().delete_users_by_ids
        THEN assert isinstance(output, dict)

        Args:
            test_case:

        Returns:

        """
        event = events.DeleteUsersByIDs(
            output_key=UserInfosOutputKey.id,
            user_ids=test_case['user_ids']
        )
        output = await self.service_users.delete_users_by_ids(
            event=event
        )

        assert isinstance(output, dict)
