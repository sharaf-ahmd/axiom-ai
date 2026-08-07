from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.exceptions import( 
    EmailAlreadyExists,
    InvalidCredentials,
    UserNotFound
    )

from app.models import User
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
    hash_refresh_token,
    decode_access_token,
    verify_refresh_token
)
from app.schemas.auth import(
    RegisterRequest,
    LoginRequest
)

class AuthService:

    @staticmethod
    async def register(
        db: AsyncSession,
        user_data: RegisterRequest,
    )-> User:

        result = await db.execute(
            select(User).where(User.email == user_data.email)
        )
        existing_user= result.scalar_one_or_none()

        if existing_user:
            raise EmailAlreadyExists()

        hashed = hash_password(user_data.password)

        user=User(
            email=user_data.email,
            hashed_password=hashed,
            full_name=user_data.full_name
        )

        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user

    @staticmethod
    async def login(
        db:AsyncSession,
        credentials:LoginRequest,
    ) -> str:

        result = await db.execute(
            select(User).where(User.email==credentials.email)
        )
        user = result.scalar_one_or_none()

        if user is None:
            raise InvalidCredentials

        if not verify_password(
            credentials.password,
            user.hashed_password,
        ):
            raise ValueError("Invalid email or password")

        if not user.is_active:
            raise ValueError(
            "User account disabled"
            )
        
        token = create_access_token(
            {
                "sub":str(user.id)
            }
        )

        refresh_token = create_refresh_token({
            "sub":str(user.id)
        })

        user.refresh_token = hash_refresh_token(refresh_token)

        await db.commit()

        return {
            "access_token":token,
            "refresh_token":refresh_token
            }

    @staticmethod
    async def refresh(db: AsyncSession,refresh_token: str,):
        payload = decode_access_token(refresh_token)

        if payload is None:
            raise InvalidCredentials()

        user_id = payload.get("sub")

        if user_id is None:
            raise InvalidCredentials()

        if payload.get("type")!= "refresh":
            raise InvalidCredentials()

        result = await db.execute(select(User).where(User.id == user_id))
        user=result.scalar_one_or_none()
        if user is None:
            raise UserNotFound()

        if not verify_refresh_token(refresh_token,user.refresh_token):
            raise InvalidCredentials()

        new_access_token = create_access_token({
            "sub": str(user.id)
        })

        new_refresh_token = create_refresh_token({
            "sub": str(user.id)
            })

        user.refresh_token = hash_refresh_token(new_refresh_token)
        await db.commit()

        return{
            "access_token": new_access_token,
            "refresh_token": new_refresh_token
        }

    @staticmethod
    async def logout(db: AsyncSession, refresh_token:str):

        payload = decode_access_token(refresh_token)
        if payload is None:
            raise InvalidCredentials()

        user_id = payload.get("sub")
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()

        if user is None:
            raise UserNotFound()

        user.refresh_token = None
        await db.commit()
    