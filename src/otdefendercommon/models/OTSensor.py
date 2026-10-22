from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, Text, Integer, Float, DateTime, ForeignKey, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from otdefendercommon.database.base import Base

class OTSensor(Base):
    __tablename__ = "ot_sensors"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    enterprise_id: Mapped[int] = mapped_column(ForeignKey("ot_enterprises.id", ondelete="CASCADE"), index=True)
    sensor_name: Mapped[str] = mapped_column(String(255), nullable=False)
    location: Mapped[str] = mapped_column(String(255), nullable=False)
    mac: Mapped[str] = mapped_column(String(20), index=True, nullable=False)
    ip: Mapped[str] = mapped_column(String(45), index=True, nullable=False)
    sensor_tag: Mapped[str] = mapped_column(String(200), nullable=False) # For registration and later identification.
    installation_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    updated_by: Mapped[str] = mapped_column(String(100), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # Relationships
    enterprise: Mapped["OTEnterprise"] = relationship(back_populates="sensors")
    health_logs: Mapped[List["OTSensorHealth"]] = relationship(
        back_populates="sensor", cascade="all, delete-orphan"
    )
    assets: Mapped[List["OTAssets"]] = relationship(
        back_populates="sensor", cascade="all, delete-orphan"
    )


