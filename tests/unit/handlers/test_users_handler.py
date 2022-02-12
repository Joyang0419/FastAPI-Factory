import pytest

from src.containers.container_services import ContainerServices
# from src.message_bus.users.handler import UsersHandler
# from src.message_bus.users import events
from src.domains.users import events, commands, handlers
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
            events.GetUsersByIDs
        ],
        id='test_key'
    ),
])
def test_events(request):
    yield request.param


@pytest.fixture(scope='function', params=[
    pytest.param(
        [
            commands.UpdateUsersByIDS,
            commands.DeleteUsersByIDs,
            commands.CreateUsers,
        ],
        id='test_key'
    ),
])
def test_commands(request):
    yield request.param


class TestUsersHandler:

    @pytest.fixture(autouse=True)
    def setup(self, test_events, test_commands):
        self.handler = handlers.UsersHandler()
        self.test_events = test_events
        self.test_commands = test_commands

    def test_event_handlers(self):
        assert all(
            [
                each_key in self.handler.EVENT_HANDLERS
                for each_key in self.test_events
            ]
        )

    def test_command_handlers(self):
        assert all(
            [
                each_key in self.handler.COMMAND_HANDLERS
                for each_key in self.test_commands
            ]
        )

    @pytest.mark.parametrize(
        "test_message", [
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
                commands.UpdateUsersByIDS(
                    user_ids=[1, 2],
                    output_key=UserInfosOutputKey.id,
                    update_data=UserUpdate(is_active=False)
                )
            ),
            pytest.param(
                commands.DeleteUsersByIDs(
                    user_ids=[1, 2],
                    output_key=UserInfosOutputKey.id
                )
            ),
            pytest.param(
                commands.CreateUsers(
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
    async def test_handle(self, test_message):
        result = await self.handler.handle(message=test_message)
        assert isinstance(result, list)
