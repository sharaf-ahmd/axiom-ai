import uuid
from sqlalchemy import (
    String,
    Boolean,
    DateTime
)

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from app.models.base import Base

class User(Base):

    __tablename__="users"

    id: Mapped[str]=mapped_column(
        primary_key=True,
        default=lambda:str(uuid.uuid4())
    )

    full_name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    email: Mapped[str]=mapped_column(
        String(225),
        unique=True,
        index=True
    )

    hashed_password: Mapped[str]

    is_active: Mapped[bool] = mapped_column(
        default=True
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False
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
