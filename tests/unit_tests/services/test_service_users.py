import pytest

from src.containers.container_repos import ContainerRepos
from src.containers.container_services import ContainerServices
from src.schemas.routers.users import UserInfos
from src.schemas.models.users import UserCreate, UserUpdate
from src.schemas.routers.users import UserInfosOutputKey


class TestServiceUsers:

    @pytest.fixture(autouse=True)
    def setup(self, fake_db_session):
        """
        repo_user(); change repo user use fake_db,
        change service_user's repo_user, use fake user_repo.


        Args:
            fake_db_session: fake_session, never commit, therefore no influence
            real database.

        Returns:

        """
        repo_users = ContainerRepos().repo_users()
        repo_users.db = fake_db_session
        self.service_users = ContainerServices().service_users()
        self.service_users.repo_users = repo_users

    @pytest.mark.asyncio
    async def test_get_all_users(self):
        """
        GIVEN an service_users()
        WHEN service_users().get_all_users()
        THEN assert isinstance(output, dict)

        Returns:

        """
        output = await self.service_users.get_all_users(
            output_key=UserInfosOutputKey.email
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

        output = await self.service_users.get_users_by_ids(
            user_ids=test_case['user_ids'],
            output_key=UserInfosOutputKey.id
        )

        assert isinstance(output, dict)

    @pytest.mark.parametrize(
        "test_case", [
            pytest.param(
                {
                    'insert_data': [
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
        GIVEN an service_users()
        WHEN service_users().create_users
        THEN assert isinstance(output, dict)

        Args:
            test_case:

        Returns:

        """

        output = await self.service_users.create_users(
            create_data=test_case['insert_data'],
            output_key=UserInfosOutputKey.email
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

        output = await self.service_users.update_users_by_ids(
            user_ids=test_case['user_ids'],
            update_data=test_case['update_data'].dict(),
            output_key=UserInfosOutputKey.id
        )

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
        output = await self.service_users.delete_users_by_ids(
            user_ids=test_case['user_ids'],
            output_key=UserInfosOutputKey.id
        )

        assert isinstance(output, dict)
