from sqlalchemy import (
    Boolean,
    Column,
    String,
    Integer
)
from sqlalchemy.orm import relationship, backref

from src.models.base import Base


class Role(Base):
    __tablename__ = "roles"

    name = Column(String(64), unique=True)
    permissions = Column(Integer)
    is_active = Column(Boolean, default=True, index=True)

    # relationship
    users = relationship(
        "User",
        lazy='subquery',
        backref=backref("roles", lazy="joined")
    )
