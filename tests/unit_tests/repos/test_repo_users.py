import pytest

from src.containers.container_repos import ContainerRepos
from src.models.users import User
from src.schemas.models.users import UserCreate, UserUpdate


class TestRepoUser:

    @pytest.fixture(autouse=True)
    def setup(self, fake_db_session):
        """

        Args:
            fake_db_session: fake_session, never commit, therefore no influence real
            database.

        Returns:

        """
        self.repo_user = ContainerRepos().repo_users()
        self.repo_user.db = fake_db_session

    @pytest.mark.asyncio
    async def test_get_all_users(self):
        """
        GIVEN an self.repo_user,
        WHEN repo_user.get_all_users(),
        THEN assert db_result instance is list

        Returns:

        """
        db_result = await self.repo_user.get_all_users()
        assert isinstance(db_result, list)

    @pytest.mark.parametrize(
        "test_case", [
            pytest.param(
                {
                    'user_ids': [None],
                },
                id='no users delete'
            ),
            pytest.param(
                {
                    'user_ids': [4],
                },
                id='users delete'
            ),
        ]
    )
    @pytest.mark.asyncio
    async def test_delete_users_by_ids(self, test_case):
        """
        GIVEN an self.repo_user,
        WHEN repo_user.delete_users_by_ids(),
        THEN assert for each db_result is isinstance is User or db_result is []

        Args:
            test_case:

        Returns:

        """
        db_result = await self.repo_user.delete_users_by_ids(test_case['user_ids'])
        if db_result:
            assert all(isinstance(each, User) for each in db_result)
        else:
            assert not db_result

    @pytest.mark.parametrize(
        "test_case", [
            pytest.param(
                {
                    'user_ids': [3, 4],
                },
                id='get user id: 4'
            ),
        ]
    )
    @pytest.mark.asyncio
    async def test_get_users_by_ids(self, test_case):
        """
        GIVEN an self.repo_user,
        WHEN repo_user.get_users_by_ids(),
        THEN assert each_db_result's id in test_case['users_id']

        Args:
            test_case:

        Returns:

        """
        db_result = await self.repo_user.get_users_by_ids(
            user_ids=test_case['user_ids']
        )

        assert all(each.id in test_case['user_ids'] for each in db_result)

    @pytest.mark.parametrize(
        "test_case", [
            pytest.param(
                {
                    'user_ids': [19],
                    'updated_data': UserUpdate(is_active=0)
                },
                id='update user id: 19, is_active: 0'
            ),
        ]
    )
    @pytest.mark.asyncio
    async def test_update_users_by_ids(self, test_case):
        """
        GIVEN an self.repo_user,
        WHEN repo_user.update_users_by_ids(),
        THEN assert db_results's each data == test_case['updated_data']

        Args:
            test_case:

        Returns:

        """
        db_result = await self.repo_user.update_users_by_ids(
            user_ids=test_case['user_ids'],
            data=test_case['updated_data']
        )

        updated_data_key = test_case['updated_data'].dict(exclude_none=True).\
            keys()

        print(updated_data_key)

        for each in db_result:
            for each_key in updated_data_key:
                assert (getattr(each, each_key) ==
                        getattr(test_case['updated_data'], each_key))

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
        GIVEN an self.repo_user,
        WHEN repo_user.create_users(),
        THEN assert db_results's each data isinstance Model User.

        Args:
            test_case:

        Returns:

        """
        db_result = await self.repo_user.create_users(
            data=test_case['insert_data']
        )

        for each in db_result:
            assert isinstance(each, User)
