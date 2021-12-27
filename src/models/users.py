from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from src.models.base import Base


class User(Base):
    __tablename__ = "users"

    email = Column(String(20), unique=True, index=True)
    hashed_password = Column(String(20))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="user", cascade="all, delete",
                         passive_deletes=True, lazy='immediate')
