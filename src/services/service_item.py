from typing import List

from src.database.settings import tool_async_sqlalchemy
from src.repos.repo_item import RepoItem
from src.schemas.models.items import ItemCreate, Item, ItemUpdate
from src.schemas.routers.items import ItemInfos


class ServiceItem:

    def __init__(self, repo: RepoItem = RepoItem(
        db=tool_async_sqlalchemy.get_db
    )):
        self.repo = repo

    async def create_item(self, pydantic_models: List[ItemCreate]):

        result = await self.repo.insert(pydantic_models=pydantic_models)

        items_dicts = {}
        for each in result:
            item_pydantic_model = Item.from_orm(each)
            items_dicts[item_pydantic_model.id] = item_pydantic_model

        return ItemInfos(data=items_dicts)

    async def get_all_items(self):

        result = await self.repo.get_all()

        items_dicts = {}
        for each in result:
            item_pydantic_model = Item.from_orm(each)
            items_dicts[item_pydantic_model.id] = item_pydantic_model

        return ItemInfos(data=items_dicts)

    async def get_item_by_ids(self, item_ids: list):

        result = await self.repo.get_by_ids(primary_ids=item_ids)

        items_dicts = {}
        for each in result:
            item_pydantic_model = Item.from_orm(each)
            items_dicts[item_pydantic_model.id] = item_pydantic_model

        return ItemInfos(data=items_dicts)

    async def update_item_by_ids(self, item_ids: list,
                                 pydantic_model: ItemUpdate):

        result = await self.repo.update_by_ids(
            primary_ids=item_ids,
            pydantic_model=pydantic_model
        )

        items_dicts = {}
        for each in result:
            item_pydantic_model = Item.from_orm(each)
            items_dicts[item_pydantic_model.id] = item_pydantic_model

        return ItemInfos(data=items_dicts)

    async def delete_item_by_ids(self, item_ids: list):

        result = await self.repo.delete_by_ids(item_ids)

        items_dicts = {}
        for each in result:
            item_pydantic_model = Item.from_orm(each)
            items_dicts[item_pydantic_model.id] = item_pydantic_model

        return ItemInfos(data=items_dicts)
