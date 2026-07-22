from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid

from sqlalchemy.orm import Mapped, mapped_column

from app.shared.infrastructure.databases.base import Base

class TaskModel(Base):
    __tablename__ = "tasks"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(15),
        nullable=False,
    )
    
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )