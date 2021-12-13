from sqlalchemyseeder import ResolvingSeeder

from settings import db_service
from src.database.models import modules

models = modules

with db_service.get_db() as session:
    seeder = ResolvingSeeder(session=session)
    new_entities = seeder.load_entities_from_json_file("./data.json")
    session.commit()
