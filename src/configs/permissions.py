from enum import Enum


class Permissions(int, Enum):
    Read = 1
    Create = 2
    Update = 4
    Delete = 8


class RolePermissions(str, Enum):
    User = 'User'
    Admin = 'Admin'

    @property
    def permissions(self):
        permissions_mapper = {
            self.User: sum([Permissions.Read]),
            self.Admin: sum([
                Permissions.Read,
                Permissions.Create,
                Permissions.Update,
                Permissions.Delete]
            )
        }

        return permissions_mapper[self.value]
