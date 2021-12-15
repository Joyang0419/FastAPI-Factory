from src.SharedLibrary.db_manager.tool_async_sqlalchemy import \
    ToolAsyncSqlalchemy
from src.database.models.items import Item
from src.repos.base import BaseRepository


class RepoItem(BaseRepository):

    def __init__(self, db: ToolAsyncSqlalchemy.get_db, model: Item = Item):
        super().__init__(db=db, model=model)
