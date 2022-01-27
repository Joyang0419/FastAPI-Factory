from sqlalchemy import Boolean, Column, String, LargeBinary

from src.models.base import Base


class User(Base):
    __tablename__ = "users"

    email = Column(String(20), unique=True, index=True)
    password = Column(String(60))
    is_active = Column(Boolean, default=True)
