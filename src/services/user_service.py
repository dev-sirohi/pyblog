from fastapi import HTTPException
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from dtos.user_profile_dto import UserProfileDto
from dtos.update_user_profile_dto import UpdateUserProfileDto
from models.post import Post
from models.user import User
from models.user_user_follow_map import UserUserFollowMap


async def get_user_by_id(db: AsyncSession, user_id: int) -> User:
    result = await db.execute(select(User).where(User.id == user_id))
    user: User | None = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


async def _build_profile(db: AsyncSession, user: User) -> UserProfileDto:
    followers_count: int = await db.scalar(
        select(func.count()).select_from(UserUserFollowMap).where(UserUserFollowMap.followee_id == user.id)) or 0
    following_count: int = await db.scalar(
        select(func.count()).select_from(UserUserFollowMap).where(UserUserFollowMap.follower_id == user.id)) or 0
    post_count: int = await db.scalar(
        select(func.count()).select_from(Post).where(Post.user_id == user.id)) or 0
    # nullable columns are coerced to empty strings since the DTO fields are required
    return UserProfileDto(
        username=user.username,
        first_name=user.first_name or "",
        last_name=user.last_name or "",
        email=user.email,
        phone=user.phone or "",
        instagram=user.instagram or "",
        facebook=user.facebook or "",
        twitter=user.twitter or "",
        linkedin=user.linkedin or "",
        followers_count=followers_count,
        following_count=following_count,
        post_count=post_count,
        member_since=user.created_at,
    )


async def get_user_profile(db: AsyncSession, user_id: int) -> UserProfileDto:
    user: User = await get_user_by_id(db, user_id)
    return await _build_profile(db, user)


async def update_user_profile(db: AsyncSession, user: User, payload: UpdateUserProfileDto) -> UserProfileDto:
    # only apply fields the client actually sent so omitted fields keep their value
    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(user, field, value)
    await db.commit()
    await db.refresh(user)
    return await _build_profile(db, user)


async def delete_user(db: AsyncSession, user: User) -> UserProfileDto:
    # build the profile before deletion so it can be returned in the response
    profile: UserProfileDto = await _build_profile(db, user)
    await db.delete(user)
    await db.commit()
    return profile
