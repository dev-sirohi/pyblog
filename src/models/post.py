from sqlalchemy import Column, Integer, String, DateTime, func, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship

from database_service import ModelBase


class Post(ModelBase):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    title = Column(String, index=True, nullable=False)
    body = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True, nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), index=True, nullable=False)

    user = relationship("User", back_populates="posts")