from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from database_service import get_db
from services import feed_service

feed_router = APIRouter()


@feed_router.get("/")
async def get_feed(request: Request, db: AsyncSession = Depends(get_db)):
    return await feed_service.get_feed(db)
