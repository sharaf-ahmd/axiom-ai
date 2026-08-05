from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
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
            raise ValueError("Email already registerd")

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
            raise ValueError("Invalid email or password")

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

        return token
    

        
