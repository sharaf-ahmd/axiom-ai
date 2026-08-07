import uuid
from sqlalchemy import (
    String,
    Boolean,
    DateTime,
    Enum as SQLEnum
)

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from app.models.base import Base
from enum import Enum

class UserRole(str, Enum):
    USER = "user"
    ADMIN = "admin"
    

class User(Base):

    __tablename__="users"

    id: Mapped[str]=mapped_column(
        String(36),
        primary_key=True,
        default=lambda:str(uuid.uuid4())
    )

    full_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    email: Mapped[str] = mapped_column(
    String(225),
    unique=True,
    index=True,
    nullable=False
)

    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    refresh_token: Mapped[str | None] = mapped_column(
            String(225),
            nullable=True
        )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    created_at: Mapped[DateTime]=mapped_column(
        DateTime,
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )


    role: Mapped[UserRole] = mapped_column(
        SQLEnum(UserRole,name="user_role_enum"),
        default=UserRole.USER,
        nullable=False
        )
    