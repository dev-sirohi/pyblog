import os
from datetime import datetime, timedelta, UTC

from fastapi import HTTPException, Depends
from jose import JWTError, jwt

from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database_service import get_db
from models.user import User

_SECRET_KEY: str = os.getenv("SECRET_KEY") or ""
_ALGORITHM_KEY: str = os.getenv("ALGORITHM_KEY") or ""
_ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES") or "")
for s in [_SECRET_KEY, _ALGORITHM_KEY]:
    if len(s.strip()) == 0:
        raise Exception("Invalid authentication environment variables")
if _ACCESS_TOKEN_EXPIRE_MINUTES == 0:
    raise Exception("Invalid authentication environment variables")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    to_encode["exp"] = datetime.now(UTC) + timedelta(minutes=_ACCESS_TOKEN_EXPIRE_MINUTES)
    return jwt.encode(to_encode, _SECRET_KEY, algorithm=_ALGORITHM_KEY)


def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, _SECRET_KEY, algorithms=[_ALGORITHM_KEY])
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")


async def register_user(db: AsyncSession,
                        username=None,
                        email=None,
                        password=None) -> tuple[User, str]:
    if username is None or email is None or password is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    result = await db.execute(select(User).where((User.email == email) | (User.username == username)))
    existing_user: User | None = result.scalar_one_or_none()
    if existing_user:
        raise HTTPException(status_code=401, detail="User already exists")

    user: User = User(username=username, email=email, password=hash_password(password))
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return await login_user(db, user.username, user.email, user.password)


async def login_user(db: AsyncSession,
                     username=None,
                     email=None,
                     password=None) -> tuple[User, str]:
    if username is None and email is None:
        raise HTTPException(status_code=401, detail="Username or email required")
    if password is None:
        raise HTTPException(status_code=401, detail="Password required")
    result = await db.execute(select(User).where(User.email == email))
    user: User | None = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=401, detail="User does not exist")
    if not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect password")

    token: str = create_access_token(data={"sub": user.id})

    return user, token
