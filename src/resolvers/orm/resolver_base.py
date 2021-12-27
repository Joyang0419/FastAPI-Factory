from typing import Type

from pydantic import BaseModel

from src.resolvers.interface.resolver_base import IFResolverBase


class IMPResolverBase(IFResolverBase):

    def __init__(self,
                 pydantic_model: Type[BaseModel],
                 output_schema: Type[BaseModel]
                 ):
        self.pydantic_model = pydantic_model
        self.output_schema = output_schema

    def resolve_get_all(
            self,
            input_data: list,
            output_key: str
    ) -> dict:

        return self._packing(input_data=input_data, output_key=output_key)

    def resolve_get_by_ids(
            self,
            input_data: list,
            output_key: str
    ) -> dict:

        return self._packing(input_data=input_data, output_key=output_key)

    def resolve_insert(
            self,
            input_data: list,
            output_key: str
    ) -> dict:

        return self._packing(input_data=input_data, output_key=output_key)

    def resolve_delete_by_ids(
            self,
            input_data: list,
            output_key: str
    ) -> dict:

        return self._packing(input_data=input_data, output_key=output_key)

    def resolve_update_by_ids(
            self,
            input_data: list,
            output_key: str
    ) -> dict:

        return self._packing(input_data=input_data, output_key=output_key)

    def _packing(
            self,
            input_data: list,
            output_key: str
    ) -> dict:
        output_data_dict = {}

        for each in input_data:
            each_data = self.pydantic_model(**each.__dict__)
            output_data_dict_key = getattr(each_data, output_key)
            output_data_dict[output_data_dict_key] = each_data

        return self.output_schema(data=output_data_dict).dict()

