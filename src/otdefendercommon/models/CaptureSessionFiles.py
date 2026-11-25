from datetime import datetime
from typing import List, Optional
from sqlalchemy import (
    String, Text, Integer, BigInteger, Float, LargeBinary, 
    ForeignKey, DateTime, Index, event
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.engine import Engine

from otdefendercommon.database.base import Base


class CaptureSessionFiles(Base):
    __tablename__ = "capture_sessions_files"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    filename: Mapped[str] = mapped_column(String(255), nullable=False)
    file_size_bytes: Mapped[int] = mapped_column(BigInteger, nullable=False)
    sha256_hash: Mapped[str] = mapped_column(String(64), unique=True, nullable=False, index=True)
    shb_comment: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    uploaded_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Relationships
    interfaces: Mapped[List["CaptureInterfaces"]] = relationship(
        back_populates="session", cascade="all, delete-orphan"
    )
    packets: Mapped[List["Packets"]] = relationship(
        back_populates="session", cascade="all, delete-orphan"
    )