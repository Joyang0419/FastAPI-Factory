import pymysql

pymysql.install_as_MySQLdb()

from sqlalchemy import Column, Integer

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.declarative import declarative_base
from src import models

models = models


class Base(object):
    @classmethod
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)
