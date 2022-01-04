from sqlalchemyseeder import ResolvingSeeder

from src.container import Container
from src.core.config import Settings
from src.models import modules

models = modules

container = Container()

with container.imp_sqlalchemy().get_db() as session:
    seeder = ResolvingSeeder(session=session)
    new_entities = seeder.load_entities_from_json_file(
        "./data.json"
    )
    session.commit()
