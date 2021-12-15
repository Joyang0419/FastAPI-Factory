# FastAPI-Factory
Provide every project init FastAPI

## Active server

### create venv
```
pip install -r requirements.txt
```
### Active Database
```
cd docker

# create mysql server(port: 3306, user: test, password: test, database: dev_db)

docker-compose up -d

# back to FastAPI-Factory path & update latest db schema.

cd ..
alembic upgrade head

# feed default data to database
run database/seeder.py

```
### Active DEV server, auto check changes and reload
```
uvicorn src.application:app --reload
```
