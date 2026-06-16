from pydantic import BaseModel

class LoginRequestDto(BaseModel):
    username: str | None
    email: str | None
    password: str