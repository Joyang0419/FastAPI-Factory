from typing import Callable, Optional

from sqlalchemy.ext.asyncio import (
    AsyncSession,
)

from src.models.roles import Role
from src.repos.interface.repo_roles import IFRepoRole
from src.configs.permissions import Permissions


class IMPRepoRole(IFRepoRole):

    def __init__(
            self,
            db: Callable[..., AsyncSession],
    ):
        self.db = db
        self.events = []

    async def get_role_by_permission(self, permissions: Permissions) \
            -> Optional[Role]:
        pass


