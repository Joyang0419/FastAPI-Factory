from typing import Union, Optional
from functools import wraps

from src.containers.container_utilities import ContainerUtilities
from src.domains.auth import commands, events
from src.repos.orm.repo_users import IMPRepoUsers
from src.schemas.jwt_token import Token
from src.services.interface.service_auth import IFServiceAuth
from src.services.orm.service_users import IMPServiceUsers
from src.schemas.jwt_token import JWTTokenPayload
from src.models.users import User
from fastapi import Response, status

container_utilities = ContainerUtilities()
crypt_manager = container_utilities.crypt_manager()
jwt_manager = container_utilities.jwt_manager()


class IMPServiceAuth(IFServiceAuth):

    def __init__(self, repo_users: IMPRepoUsers):
        self.repo_users = repo_users
        self.events = []

    async def authenticate_user(self, event: events.AuthenticateUser) \
            -> Union[dict, bool]:
        """
        get event include account, password, to certificate user table

        Args:
            event: handlers's events.UserAuthenticate

        Returns:
            User object or False
        """
        user = await self._get_current_user(event_or_command=event)

        if not user:
            return False

        output = IMPServiceUsers.packing_be_output_dict(
            input_data=[user],
            output_key=event.output_key
        )

        return output

    async def _get_current_user(
            self,
            event_or_command:
            Union[events.AuthenticateUser, commands.CreateAccessToken]
    ) -> Union[User, bool]:
        user = await self.repo_users.get_user_by_email(
            email=event_or_command.authenticate_data.email
        )

        if not user:
            return False

        if not crypt_manager.verify_pwd(
            plain_pwd=event_or_command.authenticate_data.password,
            hashed_pwd=user.password
        ):
            return False

        return user

    async def create_access_token(
            self,
            command: commands.CreateAccessToken
    ) -> Optional[Token]:

        user = await self._get_current_user(event_or_command=command)

        if not user:
            return None

        jwt_token_payload = JWTTokenPayload(sub=user.email)
        token = jwt_manager.create_access_token(data=jwt_token_payload)
        return Token(access_token=token)

    def collect_new_events(self):
        while self.events:
            yield self.events.pop(0)

    @staticmethod
    def get_token_decode_data(event: events.GetTokenDecodeData) \
            -> Optional[dict]:

        jwt_payload = jwt_manager.get_token_payload(token=event.token)

        if not jwt_payload:
            return None

        return jwt_payload

    def permissions_required_decorator(self, permissions):
        def decorator(function):
            @wraps(function)
            async def wrappers(*args, **kwargs):
                token_payload = await jwt_manager.get_token_payload(
                    token=kwargs['token']
                )
                user_email = token_payload['sub']
                current_user = await self.repo_users.get_user_by_email(
                    email=user_email
                )

                if current_user.roles.permissions < permissions:
                    return Response(
                        status_code=status.HTTP_403_FORBIDDEN
                    )

                return await function(*args, **kwargs)

            return wrappers

        return decorator
