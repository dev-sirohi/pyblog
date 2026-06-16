from pydantic import BaseModel

class CreatePostDto(BaseModel):
    title: str
    body: str
