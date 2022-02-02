from sqlalchemy import Boolean, Column, String, ForeignKey, Integer

from src.models.base import Base

from src.models.roles import Role


class User(Base):
    __tablename__ = "users"

    email = Column(String(20), unique=True, index=True)
    password = Column(String(60))
    is_active = Column(Boolean, default=True)

    # ForeignKey
    role_id = Column(Integer, ForeignKey(Role.id), default=1)
