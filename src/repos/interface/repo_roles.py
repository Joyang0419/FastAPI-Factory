import abc
from typing import Optional
from src.models.roles import Role
from src.configs.permissions import Permissions


class IFRepoRole(abc.ABC):

    @abc.abstractmethod
    def get_role_by_permission(
            self,
            permissions: Permissions
    ) -> Optional[Role]:
        return NotImplemented
