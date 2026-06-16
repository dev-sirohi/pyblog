from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from database_service import ModelBase
import uuid


class PostMediaMap(ModelBase):
    __tablename__ = "post_media_map"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
