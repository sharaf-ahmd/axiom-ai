import uuid
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class OrganizationMember(Base):

    __tablename__ = "organization_members"


    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )


    organization_id: Mapped[uuid.UUID] = mapped_column(
        nullable=False
    )


    user_id: Mapped[uuid.UUID] = mapped_column(
        nullable=False
    )


    role: Mapped[str] = mapped_column(
        String(50),
        default="member"
    )