from src.SharedLibrary.db_manager.tool_async_sqlalchemy import \
    ToolAsyncSqlalchemy
from src.database.models.users import User
from src.repos.base import BaseRepository
from src.schemas.models.items import ItemBase
from src.database.models.items import Item


class RepoUser(BaseRepository):

    def __init__(self, db: ToolAsyncSqlalchemy.get_db, model: User = User):
        super().__init__(db=db, model=model)

    async def user_create_item(self, user_id: int, item: ItemBase):
        sql_result = await self.get_by_ids(primary_ids=[user_id])
        user = sql_result[0]
        item = Item(**item.dict())
        user.items.append(item)
        model_objects = [user]
        await self._db_complete_commit(model_objects)


if __name__ == "__main__":
    async def example():
        from src.database.settings import tool_async_sqlalchemy
        repo = RepoUser(db=tool_async_sqlalchemy.get_db)
        item = ItemBase(title="test_title", description="test_desc")
        await repo.user_create_item(user_id=65, item=item)


    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(example())