from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.post import Post


async def get_feed(db: AsyncSession) -> list[Post]:
    result = await db.execute(select(Post).order_by(Post.created_at.desc()))
    return list(result.scalars().all())
