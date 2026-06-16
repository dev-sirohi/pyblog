from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.post import Post
from models.user_post_like_map import UserPostLikeMap


async def get_post_by_id(db: AsyncSession, post_id: int) -> Post:
    result = await db.execute(select(Post).where(Post.id == post_id))
    post: Post | None = result.scalar_one_or_none()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


async def create_post(db: AsyncSession, user_id: int, title: str, body: str) -> Post:
    post: Post = Post(user_id=user_id, title=title, body=body)
    db.add(post)
    await db.commit()
    await db.refresh(post)
    return post


async def update_post(db: AsyncSession, post_id: int, user_id: int, title: str, body: str) -> Post:
    post: Post = await get_post_by_id(db, post_id)
    # only the author may edit their own post
    if post.user_id != user_id:
        raise HTTPException(status_code=403, detail="Not allowed to edit this post")
    post.title = title
    post.body = body
    await db.commit()
    await db.refresh(post)
    return post


async def delete_post(db: AsyncSession, post_id: int, user_id: int) -> None:
    post: Post = await get_post_by_id(db, post_id)
    if post.user_id != user_id:
        raise HTTPException(status_code=403, detail="Not allowed to delete this post")
    await db.delete(post)
    await db.commit()


async def like_post(db: AsyncSession, post_id: int, user_id: int) -> None:
    await get_post_by_id(db, post_id)
    result = await db.execute(select(UserPostLikeMap).where(
        (UserPostLikeMap.post_id == post_id) & (UserPostLikeMap.user_id == user_id)))
    existing: UserPostLikeMap | None = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=409, detail="Post already liked")
    like: UserPostLikeMap = UserPostLikeMap(post_id=post_id, user_id=user_id)
    db.add(like)
    await db.commit()


async def unlike_post(db: AsyncSession, post_id: int, user_id: int) -> None:
    result = await db.execute(select(UserPostLikeMap).where(
        (UserPostLikeMap.post_id == post_id) & (UserPostLikeMap.user_id == user_id)))
    like: UserPostLikeMap | None = result.scalar_one_or_none()
    if not like:
        raise HTTPException(status_code=404, detail="Like not found")
    await db.delete(like)
    await db.commit()
