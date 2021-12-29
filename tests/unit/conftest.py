import pytest
from src.models.users import User


@pytest.fixture(scope="session")
def fake_users(tmpdir_factory):
    users = [
        User(
            id=1,
            email='test_1@gmail.com',
            hashed_password='test',
            is_active=1
        ),
        User(
            id=2,
            email='test_2@gmail.com',
            hashed_password='test',
            is_active=1
        )
    ]
