import pytest

from src.containers.container_services import ContainerServices
from src.message_bus.auth.handler import AuthHandler
from src.message_bus.auth import events
from src.schemas.routers.users import UserInfosOutputKey
from src.schemas.models.users import UserAuthenticate


service_auth = ContainerServices().service_auth()


@pytest.fixture(scope='function', params=[
    pytest.param(
        [
            events.AuthenticateUser,
        ],
        id='test_key'
    ),
])
def test_case(request):
    yield request.param


class TestAuthHandler:

    @pytest.fixture(autouse=True)
    def setup(self, test_case):
        self.handler = AuthHandler()
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
                events.AuthenticateUser(
                    output_key=UserInfosOutputKey.id,
                    authenticate_data=UserAuthenticate(
                        email='sss',
                        password='sss'
                    )
                ),
                id='events.AuthenticateUse'
            )
        ]
    )
    @pytest.mark.asyncio
    async def test_handle(self, test_event):
        result = await self.handler.handle(event=test_event)
        assert isinstance(result, list)
