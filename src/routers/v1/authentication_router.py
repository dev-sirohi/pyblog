from fastapi import APIRouter, Depends, Response, Request
from sqlalchemy.ext.asyncio import AsyncSession

from database_service import get_db
from dtos.auth_response_dto import AuthResponseDto
from dtos.login_request_dto import LoginRequestDto
from dtos.sign_up_request_dto import SignUpRequestDto
from rate_limiter import rate_limiter
from services.authentication_service import register_user, login_user

authentication_router = APIRouter(prefix="/v1/auth", tags=["auth"])


@authentication_router.post("/login", response_model=AuthResponseDto)
@rate_limiter.limit("10/hour")
async def login(payload: LoginRequestDto, request: Request, response: Response, db: AsyncSession = Depends(get_db)):
    user, token = await login_user(db, payload.username, payload.email, payload.password)
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        samesite="lax",
        secure=True,
        max_age=60 * 60 * 24,
    )
    return user


@authentication_router.post("/register", response_model=AuthResponseDto)
@rate_limiter.limit("10/day")
async def signup(payload: SignUpRequestDto, request: Request, response: Response, db: AsyncSession = Depends(get_db)):
    user, token = await register_user(db, payload.username, payload.email, payload.password)
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        samesite="lax",
        secure=True,
        max_age=60 * 60 * 24,
    )
    return user


@authentication_router.post("/logout")
async def logout(response: Response):
    response.delete_cookie(key="access_token")
    return {"message": "Logged out"}
