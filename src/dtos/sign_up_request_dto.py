from pydantic import BaseModel

class SignUpRequestDto(BaseModel):
    username: str | None
    email: str | None
    password: str