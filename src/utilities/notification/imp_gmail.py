from src.utilities.notification.interface import IFNotificationManager
from src.message_bus.users import events


class IMPGmail(IFNotificationManager):

    async def send_notification(self, message):
        print(f"Notification Message:{message}")
        is_send = True
        return is_send
