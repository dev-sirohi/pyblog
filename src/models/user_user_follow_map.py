from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint
from database_service import ModelBase


class UserUserFollowMap(ModelBase):
    __tablename__ = "user_user_follow_map"

    followee_id = Column(Integer, ForeignKey('user.id'), index=True, nullable=False)
    follower_id = Column(Integer, ForeignKey('user.id'), index=True, nullable=False)

    __table_args__ = (PrimaryKeyConstraint('followee_id', 'follower_id'),)