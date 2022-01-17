import pathlib

from sqlalchemyseeder import ResolvingSeeder

from src.containers import Containers
from src.models import modules

models = modules

container_tools = Containers().container_tools()

orm_session = container_tools.db_manager().get_db


def create_fake_data(session):
    with session() as session:
        seeder = ResolvingSeeder(session=session)
        seeder.load_entities_from_json_file(
            pathlib.Path(__file__).parent.resolve().joinpath('data.json')
        )
        session.commit()


if __name__ == '__main__':
    create_fake_data(session=orm_session)
