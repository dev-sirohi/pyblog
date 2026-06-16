from datetime import datetime

from pydantic import BaseModel


class UserProfileDto(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    phone: str
    instagram: str
    facebook: str
    twitter: str
    linkedin: str
    followers_count: int
    following_count: int
    post_count: int
    member_since: datetime
