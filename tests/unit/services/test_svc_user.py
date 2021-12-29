import pytest

from src.application import app
from src.schemas.routers.users import UserInfos


class TestSvcUser:

    @pytest.mark.asyncio
    async def test_get_all_users(self):
        output = await app.container.svc_user().get_all_users()

        assert UserInfos(**output)






