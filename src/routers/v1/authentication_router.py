from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from database_service import get_db
from dtos.login_request_dto import LoginRequestDto
from dtos.sign_up_request_dto import SignUpRequestDto
from dtos.auth_response_dto import AuthResponseDto
from services.authentication_service import register_user, login_user
from rate_limiter import rate_limiter

authentication_router = APIRouter(prefix="/auth", tags=["auth"])

@authentication_router.post("/login", response_model=AuthResponseDto)
@rate_limiter.limit("10/hour")
async def login(request: LoginRequestDto, response: Response, db: AsyncSession = Depends(get_db)):
    user, token = await login_user(db, request.username, request.email, request.password)
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        samesite="lax",
        secure=True,
        max_age=60 * 60 * 24,
    )
    return user


@authentication_router.post("/signup", response_model=AuthResponseDto)
@rate_limiter.limit("10/day")
async def signup(request: SignUpRequestDto, response: Response, db: AsyncSession = Depends(get_db)):
    user, token = await register_user(db, request.username, request.email, request.password)
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
