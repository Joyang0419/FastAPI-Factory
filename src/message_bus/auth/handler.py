from typing import Type, List, Callable, Dict

from src.containers.container_services import ContainerServices
from src.message_bus.auth import events

container_service = ContainerServices()

from src.message_bus.interface_handler import IFHandler


class AuthHandler(IFHandler):

    def __init__(self):
        self.service_auth = container_service.service_auth()
        IFHandler.__init__(self, service=self.service_auth)

    @property
    def handlers(self) -> Dict[Type[events.Event], List[Callable]]:
        return {
            events.AuthenticateUser: [self.service_auth.authenticate_user],
            events.CreateAccessToken: [self.service_auth.create_access_token],
            events.GetTokenDecodeData: [self.service_auth.get_token_decode_data]
        }


