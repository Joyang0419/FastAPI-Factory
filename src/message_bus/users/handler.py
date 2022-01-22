from typing import Type, List, Callable, Dict

from src.containers.container_services import ContainerServices
from src.message_bus.users import events

container_service = ContainerServices()


class UsersHandler:

    def __init__(self):
        self.service_user = container_service.service_users()

    @property
    def handlers(self) -> Dict[Type[events.Event], List[Callable]]:
        return {
            events.GetAllUsers: [self.service_user.get_all_users],
            events.Notification: [self.service_user.send_notification],
            events.GetUsersByIDs: [self.service_user.get_users_by_ids],
            events.UpdateUsersByIDS: [self.service_user.update_users_by_ids],
            events.DeleteUsersByIDs: [self.service_user.delete_users_by_ids],
            events.CreateUsers: [self.service_user.create_users]
        }

    async def handle(self, event: events.Event):
        results = []
        queue = [event]
        while queue:
            event = queue.pop(0)
            for handler in self.handlers[type(event)]:
                result = await handler(event)
                results.append(result)
                queue.extend(self.service_user.collect_new_events())
        return results
