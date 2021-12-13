import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.SharedLibrary.db_manager.tool_sqlalchemy import ToolSqlalchemy
from src.SharedLibrary.db_manager.tool_async_sqlalchemy import \
    ToolAsyncSqlalchemy

pymysql.install_as_MySQLdb()

Base = declarative_base()

async_db_service = ToolAsyncSqlalchemy(
    db_dialect='mysql', db_driver='aiomysql', db_user='test',
    db_password='test', db_host='0.0.0.0', db_port=3306,
    db_name='dev_db', echo=True
)


# here for migration and seeder
db_service = ToolSqlalchemy(
    db_dialect='mysql', db_driver='mysqldb', db_user='test',
    db_password='test', db_host='0.0.0.0', db_port=3306,
    db_name='dev_db', echo=True
)
SQLALCHEMY_DATABASE_URL = db_service.db_url
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
