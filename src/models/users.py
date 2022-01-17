from sqlalchemy import Boolean, Column, String

from src.models.base import Base


class User(Base):
    __tablename__ = "users"

    email = Column(String(20), unique=True, index=True)
    hashed_password = Column(String(20))
    is_active = Column(Boolean, default=True)
