from pydantic import BaseModel


class UpdateUserProfileDto(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    phone: str | None = None
    instagram: str | None = None
    facebook: str | None = None
    twitter: str | None = None
    linkedin: str | None = None
