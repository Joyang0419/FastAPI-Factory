import asyncio

from src.SharedLibrary.db_manager.tool_async_sqlalchemy import \
    ToolAsyncSqlalchemy
from src.database.models.users import User
from src.database.settings import tool_async_sqlalchemy
from src.repos.abstract import AbstractRepository
from src.schemas.models.users import UserCreate


class RepoUser(AbstractRepository):

    def __init__(self, db: ToolAsyncSqlalchemy.get_db, model: User = User):
        super().__init__(db=db, model=model)


if __name__ == "__main__":
    async def example():
        repo_user = RepoUser(db=tool_async_sqlalchemy.get_db)

        # insert
        user_1 = UserCreate(email='test_107@gmail.com', hashed_password='123')
        user_2 = UserCreate(email='test_108@gmail.com', hashed_password='123')
        result = await repo_user.insert(pydantic_models=[user_1, user_2])
        print(result)
        primary_ids = [each.id for each in result]

        # get_all
        output = await repo_user.get_all()
        print(output)

        # get_by_ids
        output = await repo_user.get_by_ids(primary_ids=primary_ids)
        print(output)

        # delete
        # await repo_user.delete_by_ids(primary_ids=primary_ids)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(example())
