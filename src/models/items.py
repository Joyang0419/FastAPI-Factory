from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from src.models.base import Base


class Item(Base):
    __tablename__ = "items"

    title = Column(String(20), index=True)
    description = Column(String(20), index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    user = relationship("User", back_populates="items", lazy='joined')
