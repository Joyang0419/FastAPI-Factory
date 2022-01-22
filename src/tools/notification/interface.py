import abc


class IFNotificationManager(abc.ABC):

    @abc.abstractmethod
    def send_notification(self, message: str):
        return NotImplemented
