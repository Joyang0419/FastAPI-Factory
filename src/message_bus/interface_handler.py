from typing import Type, List, Callable, Dict
from pydantic import BaseModel
import abc


class Event(BaseModel):
    pass


class IFHandler(abc.ABC):

    def __init__(self, service):
        self.service = service

    @property
    @abc.abstractmethod
    def handlers(self) -> Dict[Type[Event], List[Callable]]:
        return NotImplemented

    async def handle(self, event: Event):
        results = []
        queue = [event]
        while queue:
            event = queue.pop(0)
            for handler in self.handlers[type(event)]:
                result = await handler(event)
                results.append(result)
                queue.extend(self.service.collect_new_events())
        return results
