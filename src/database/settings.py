from sqlalchemy.ext.declarative import declarative_base
from src.SharedLibrary.db_manager import AsyncSqlalchemy
import pymysql
pymysql.install_as_MySQLdb()

Base = declarative_base()

db_service = AsyncSqlalchemy(
    db_dialect='mysql', db_driver='aiomysql', db_user='test',
    db_password='test', db_host='0.0.0.0', db_port=3306,
    db_name='dev_db', echo=True
)

SQLALCHEMY_DATABASE_URL = db_service.migrate_url
