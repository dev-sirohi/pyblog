from pydantic import BaseModel


class AuthResponseDto(BaseModel):
    id: int
    username: str
    email: str
