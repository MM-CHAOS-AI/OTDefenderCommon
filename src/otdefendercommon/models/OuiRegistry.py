from typing import Optional
from sqlalchemy import String, Text, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from otdefendercommon.database.base import Base


class OuiRegistry(Base):
    __tablename__ = "oui_registry"

    oui: Mapped[str] = mapped_column(String(50), primary_key=True)
    manufacturer: Mapped[str] = mapped_column(String(255), nullable=False)
    registry: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    short_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    device_type: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    registered_date: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    address: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    sources: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    registrant_raw: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    status: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    deregistered_date: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    registrant_history: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    last_updated: Mapped[Optional[str]] = mapped_column(
        String(50), server_default=func.current_timestamp(), nullable=True
    )

