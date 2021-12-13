# FastAPI-Factory
Provide every project init FastAPI

## Active server
### Active Database
```
cd docker

# create mysql server(port: 3306, user: test, password: test, database: dev_db)

docker-compose up -d

# back to FastAPI-Factory path & update latest db schema.

cd ..
alembic upgrade head

```
### Active DEV server, auto check changes and reload
```
uvicorn src.application:app --reload
```
