import abc


class IFResolverBase(abc.ABC):

    @abc.abstractmethod
    def resolve_get_all(
            self,
            input_data: list,
            output_key: str
    ) -> dict:
        return NotImplemented

    @abc.abstractmethod
    def resolve_get_by_ids(
            self,
            input_data: list,
            output_key: str
    ) -> dict:
        return NotImplemented

    @abc.abstractmethod
    def resolve_delete_by_ids(
            self,
            input_data: list,
            output_key: str
    ) -> dict:
        return NotImplemented

    @abc.abstractmethod
    def resolve_update_by_ids(
            self,
            input_data: list,
            output_key: str
    ) -> dict:
        return NotImplemented

    @abc.abstractmethod
    def resolve_insert(
            self,
            input_data: list,
            output_key: str
    ) -> dict:
        return NotImplemented
