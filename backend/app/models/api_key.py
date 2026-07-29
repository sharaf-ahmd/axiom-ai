import uuid
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base



class APIKey(Base):

    __tablename__ = "api_keys"


    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )


    user_id: Mapped[uuid.UUID] = mapped_column(
        nullable=False
    )


    name: Mapped[str] = mapped_column(
        String(100)
    )


    key_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )