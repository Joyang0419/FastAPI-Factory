import abc


class IFServiceUsers(abc.ABC):

    @abc.abstractmethod
    def get_all_users(
            self,
            output_key: str
    ) -> dict:

        return NotImplemented

    @abc.abstractmethod
    def get_users_by_ids(
            self,
            user_ids: [int],
            output_key: str
    ) -> dict:

        return NotImplemented

    @abc.abstractmethod
    def update_users_by_ids(
            self,
            user_ids: [int],
            update_data: dict,
            output_key: str
    ) -> dict:

        return NotImplemented

    @abc.abstractmethod
    def create_users(
            self,
            create_data: dict,
            output_key: str
    ) -> dict:

        return NotImplemented

    @abc.abstractmethod
    def delete_users_by_ids(
            self,
            user_ids: [int],
            output_key: str
    ) -> dict:

        return NotImplemented

