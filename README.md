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


# To add current dir to python path, 
export PYTHONPATH=`pwd`

# feed default data to database
python ./src/database/seeder.py

```
### Active DEV server, auto check changes and reload
```
uvicorn src.application:app --reload
```

# Explanation
[Notion-note](https://nonchalant-mozzarella-71d.notion.site/FastAPI-SQLalchemy-alembic-Async-Await-e5626665abcd4940b2537f1fe0edd2bb)

# Future work
- tests structure.