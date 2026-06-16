from fastapi import Request, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database_service import get_db
from models.user import User
from services.authentication_service import decode_token


async def get_current_user(request: Request, db: AsyncSession = Depends(get_db)) -> User:
    token: str = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    payload: dict = decode_token(token)
    user_id: int = int(payload.get("sub"))
    result = await db.execute(select(User).where(User.id == user_id))
    user: User | None = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user