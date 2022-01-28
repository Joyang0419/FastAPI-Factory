import pytest

from src.containers.container_services import ContainerServices
from src.message_bus.users.handler import UsersHandler
from src.message_bus.users import events
from src.schemas.routers.users import UserInfosOutputKey
from src.schemas.models.users import (
    UserCreate,
    UserUpdate
)

service_users = ContainerServices().service_users()


@pytest.fixture(scope='function', params=[
    pytest.param(
        [
            events.GetAllUsers,
            events.Notification,
            events.GetUsersByIDs,
            events.UpdateUsersByIDS,
            events.DeleteUsersByIDs,
            events.CreateUsers,
        ],
        id='test_key'
    ),
])
def test_case(request):
    yield request.param


class TestUsersHandler:

    @pytest.fixture(autouse=True)
    def setup(self, test_case):
        self.handler = UsersHandler()
        self.test_case = test_case

    def test_handlers(self):
        assert all(
            [
                each_key in self.handler.handlers
                for each_key in self.test_case
            ]
        )

    @pytest.mark.parametrize(
        "test_event", [
            pytest.param(
                    events.GetAllUsers(
                        output_key=UserInfosOutputKey.id
                    )
            ),
            pytest.param(
                events.Notification(
                    message='test'
                )
            ),
            pytest.param(
                events.GetUsersByIDs(
                    user_ids=[1, 2],
                    output_key=UserInfosOutputKey.id
                )
            ),
            pytest.param(
                events.UpdateUsersByIDS(
                    user_ids=[1, 2],
                    output_key=UserInfosOutputKey.id,
                    update_data=UserUpdate(is_active=False)
                )
            ),
            pytest.param(
                events.DeleteUsersByIDs(
                    user_ids=[1, 2],
                    output_key=UserInfosOutputKey.id
                )
            ),
            pytest.param(
                events.CreateUsers(
                    create_data=[
                        UserCreate(
                            email='test_1_email',
                            password='test_1_pwd'
                        )
                    ],
                    output_key=UserInfosOutputKey.id
                )
            )
        ]
    )
    @pytest.mark.asyncio
    async def test_handle(self, test_event):
        result = await self.handler.handle(event=test_event)
        assert isinstance(result, list)
