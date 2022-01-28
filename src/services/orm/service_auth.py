from typing import Union

from src.containers.container_utilities import ContainerUtilities
from src.message_bus.auth import events
from src.repos.orm.repo_users import IMPRepoUsers
from src.services.interface.service_auth import IFServiceAuth
from src.services.orm.service_users import IMPServiceUsers

crypt_manager = ContainerUtilities().crypt_manager()


class IMPServiceAuth(IFServiceAuth):

    def __init__(self, repo_users: IMPRepoUsers):
        self.repo_users = repo_users
        self.events = []

    async def authenticate_user(self, event: events.AuthenticateUser) \
            -> Union[dict, bool]:
        """
        get event include account, password, to certificate user table

        Args:
            event: message_bus's events.UserAuthenticate

        Returns:
            User object or False
        """
        user = await self.repo_users.get_user_by_email(
            email=event.authenticate_data.email
        )

        if not user:
            return False

        if not crypt_manager.verify_pwd(
            plain_pwd=event.authenticate_data.password,
            hashed_pwd=user.password
        ):
            return False

        output = IMPServiceUsers.packing_be_output_dict(
            input_data=[user],
            output_key=event.output_key
        )

        return output

    def collect_new_events(self):
        while self.events:
            yield self.events.pop(0)



# def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt

