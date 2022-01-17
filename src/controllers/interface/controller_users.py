import abc
import pydantic
import typing


class IFControllerUsers(abc.ABC):

    @abc.abstractmethod
    def get_all_users(
            self,
            output_key: str
    ) -> typing.Type[pydantic.BaseModel]:

        return NotImplemented

    @abc.abstractmethod
    def get_users_by_ids(
            self,
            user_ids: [int],
            output_key: str
    ) -> typing.Type[pydantic.BaseModel]:

        return NotImplemented

    @abc.abstractmethod
    def create_users(
            self,
            create_data: typing.Type[pydantic.BaseModel],
            output_key: str
    ) -> typing.Type[pydantic.BaseModel]:

        return NotImplemented

    @abc.abstractmethod
    def update_users_by_ids(
            self,
            user_ids: [int],
            update_data: typing.Type[pydantic.BaseModel],
            output_key: str
    ) -> typing.Type[pydantic.BaseModel]:

        return NotImplemented

    @abc.abstractmethod
    def delete_users_by_ids(
            self,
            user_ids: [int],
            output_key: str
    ) -> typing.Type[pydantic.BaseModel]:

        return NotImplemented
