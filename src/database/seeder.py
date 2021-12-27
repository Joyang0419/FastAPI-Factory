from sqlalchemyseeder import ResolvingSeeder

from settings import tool_sqlalchemy
from src.models import modules

models = modules

with tool_sqlalchemy.get_db() as session:
    seeder = ResolvingSeeder(session=session)
    new_entities = seeder.load_entities_from_json_file(
        "./data.json"
    )
    session.commit()
