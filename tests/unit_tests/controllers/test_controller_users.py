import pytest

from src.containers.container_controllers import ContainerControllers
from src.schemas.routers.users import UserInfosOutputKey, UserInfos
from src.schemas.models.users import UserCreate, UserUpdate


class TestControllerUsers:

    @pytest.fixture(autouse=True)
    def setup(self, fake_db_session):
        """
        init controller_users and change service_users's repo_users's db

        Args:
            fake_db_session: fake_session, no influence real database.

        Returns:

        """
        self.controller_users = ContainerControllers().controller_users()
        self.controller_users.service_users.repo_users.db = fake_db_session

    @pytest.mark.asyncio
    async def test_get_all_users(self):
        """
        GIVEN an controller_users
        WHEN controller_users.get_all_users
        THEN assert isinstance(output, UserInfos)

        Returns:

        """
        output = await self.controller_users.get_all_users(
            output_key=UserInfosOutputKey.id
        )

        assert isinstance(output, UserInfos)

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
        GIVEN an controller_users
        WHEN controller_users.get_users_by_ids
        THEN assert isinstance(output, UserInfos)

        Args:
            test_case:

        Returns:

        """
        output = await self.controller_users.get_users_by_ids(
            user_ids=test_case['user_ids'],
            output_key=UserInfosOutputKey.id
        )

        assert isinstance(output, UserInfos)

    @pytest.mark.parametrize(
        "test_case", [
            pytest.param(
                {
                    'create_data': [
                        UserCreate(
                            email='test_1_email',
                            hashed_password='test_1_pwd'
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
        GIVEN an controller_users
        WHEN controller_users.create_users
        THEN assert isinstance(output, UserInfos)

        Args:
            test_case:

        Returns:

        """
        output = await self.controller_users.create_users(
            create_data=test_case['create_data'],
            output_key=UserInfosOutputKey.id
        )

        assert isinstance(output, UserInfos)

    @pytest.mark.parametrize(
        "test_case", [
            pytest.param(
                {
                    'user_ids': [19],
                    'update_data': UserUpdate(is_active=0)
                },
                id='update user id: 4, is_active: 0'
            ),
        ]
    )
    @pytest.mark.asyncio
    async def test_update_users_by_ids(self, test_case):
        """
        GIVEN an controller_users
        WHEN controller_users.update_users_by_ids
        THEN assert isinstance(output, UserInfos)

        Args:
            test_case:

        Returns:

        """
        output = await self.controller_users.update_users_by_ids(
            user_ids=test_case['user_ids'],
            update_data=test_case['update_data'],
            output_key=UserInfosOutputKey.id
        )

        assert isinstance(output, UserInfos)

    @pytest.mark.parametrize(
        "test_case", [
            pytest.param(
                {
                    'user_ids': [4],
                },
                id='users delete'
            ),
        ]
    )
    @pytest.mark.asyncio
    async def test_delete_by_ids(self, test_case):
        """
        GIVEN an controller_users
        WHEN controller_users.delete_users_by_ids
        THEN assert isinstance(output, UserInfos)

        Args:
            test_case:

        Returns:

        """
        output = await self.controller_users.delete_users_by_ids(
            user_ids=test_case['user_ids'],
            output_key=UserInfosOutputKey.id
        )

        assert isinstance(output, UserInfos)


