import pytest

from src.containers.container_services import ContainerServices
from src.domains.auth import events, commands, handlers
from src.schemas.models.users import UserAuthenticate
from src.schemas.routers.users import UserInfosOutputKey

service_auth = ContainerServices().service_auth()


@pytest.fixture(scope='function', params=[
    pytest.param(
        [
            events.AuthenticateUser,
            events.GetTokenDecodeData,
        ],
        id='test_key'
    ),
])
def test_events(request):
    yield request.param


@pytest.fixture(scope='function', params=[
    pytest.param(
        [
            commands.CreateAccessToken
        ],
        id='test_key'
    ),
])
def test_commands(request):
    yield request.param


class TestAuthHandler:

    @pytest.fixture(autouse=True)
    def setup(self, test_events, test_commands):
        self.handler = handlers.AuthHandler()
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
                events.AuthenticateUser(
                    output_key=UserInfosOutputKey.id,
                    authenticate_data=UserAuthenticate(
                        email='sss',
                        password='sss'
                    )
                ),
                id='events.AuthenticateUse'
            ),
            pytest.param(
                commands.CreateAccessToken(
                    authenticate_data=UserAuthenticate(
                        email='sss',
                        password='sss'
                    )
                ),
                id='commands.CreateAccessToken'
            ),
            pytest.param(
                events.GetTokenDecodeData(
                    token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJGYXN'
                          '0QVBJIEZhY3RvcnkiLCJzdWIiOiJKb3lhbmcwNDE5QGdtYWlsLmN'
                          'vbSIsImV4cCI6MjI0MzY3MjA3MywibmJmIjoxNjQzNjcyMDczLCJ'
                          'pYXQiOjE2NDM2NzIwNzN9.mBCk6FX-MZBWljFuOcMYSUTNQYOzta'
                          '0YRmms5ehd8fo'
                ),
                id='events.GetTokenDecodeData'
            ),

        ]
    )
    @pytest.mark.asyncio
    async def test_handle(self, test_message):
        result = await self.handler.handle(message=test_message)
        assert isinstance(result, list)
