from sqlalchemy import Column, Integer, String, DateTime, func, Boolean, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from database_service import ModelBase


class UserPostLikeMap(ModelBase):
    __tablename__ = "user_post_like_map"

    post_id = Column(Integer, ForeignKey('posts.id'), index=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), index=True, nullable=False)

    __table_args__ = (PrimaryKeyConstraint('post_id', 'user_id'),)