from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from database_service import get_db
from dtos.user_profile_dto import UserProfileDto
from dtos.update_user_profile_dto import UpdateUserProfileDto
from services import user_service
from services.auth_deps import get_current_user
from models.user import User

user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.get("/me", response_model=UserProfileDto)
async def get_user_profile(request: Request, db: AsyncSession = Depends(get_db),
                           current_user: User = Depends(get_current_user)):
    return await user_service.get_user_profile(db, current_user.id)


@user_router.get("/{user_id}", response_model=UserProfileDto)
async def get_user_profile_by_id(user_id: int, request: Request, db: AsyncSession = Depends(get_db)):
    return await user_service.get_user_profile(db, user_id)


@user_router.put("/me", response_model=UserProfileDto)
async def update_user_profile(payload: UpdateUserProfileDto, request: Request, db: AsyncSession = Depends(get_db),
                              current_user: User = Depends(get_current_user)):
    return await user_service.update_user_profile(db, current_user, payload)


@user_router.delete("/me", response_model=UserProfileDto)
async def delete_user(request: Request, db: AsyncSession = Depends(get_db),
                      current_user: User = Depends(get_current_user)):
    return await user_service.delete_user(db, current_user)
