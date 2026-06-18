from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from database_service import get_db
from dtos.create_post_dto import CreatePostDto
from models.user import User
from rate_limiter import rate_limiter
from services import post_service
from services.auth_deps import get_current_user

post_router = APIRouter(prefix="/v1/post", tags=["post"])


@post_router.get("/{post_id}")
@rate_limiter.limit("100/second")
async def get_post_by_post_id(post_id: int, request: Request, db: AsyncSession = Depends(get_db)):
    return await post_service.get_post_by_id(db, post_id)


@post_router.post("/")
@rate_limiter.limit("1/minute")
async def create_post(payload: CreatePostDto, request: Request, db: AsyncSession = Depends(get_db),
                      current_user: User = Depends(get_current_user)):
    return await post_service.create_post(db, current_user.id, payload.title, payload.body)


@post_router.put("/{post_id}")
@rate_limiter.limit("1/minute")
async def update_post(post_id: int, payload: CreatePostDto, request: Request, db: AsyncSession = Depends(get_db),
                      current_user: User = Depends(get_current_user)):
    return await post_service.update_post(db, post_id, current_user.id, payload.title, payload.body)


@post_router.delete("/{post_id}")
@rate_limiter.limit("10/minute")
async def delete_post_by_id(post_id: int, request: Request, db: AsyncSession = Depends(get_db),
                            current_user: User = Depends(get_current_user)):
    await post_service.delete_post(db, post_id, current_user.id)
    return {"message": "Post deleted"}


@post_router.post("/{post_id}/like")
@rate_limiter.limit("5/second")
async def like_post(post_id: int, request: Request, db: AsyncSession = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    await post_service.like_post(db, post_id, current_user.id)
    return {"message": "Post liked"}


@post_router.delete("/{post_id}/like")
@rate_limiter.limit("5/second")
async def unlike_post(post_id: int, request: Request, db: AsyncSession = Depends(get_db),
                      current_user: User = Depends(get_current_user)):
    await post_service.unlike_post(db, post_id, current_user.id)
    return {"message": "Post unliked"}
