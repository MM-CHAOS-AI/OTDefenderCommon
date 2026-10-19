from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, Text, Integer, Float, DateTime, ForeignKey, Index, func, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from otdefendermain.database.db_manager import Base


class OTSensorHealth(Base):
    __tablename__ = "ot_sensor_health"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    sensor_id: Mapped[int] = mapped_column(ForeignKey("ot_sensors.id", ondelete="CASCADE"), index=True)
    health_status: Mapped[str] = mapped_column(String(50), nullable=False)  # e.g., 'Healthy', 'Warning', 'Critical'
    cpu: Mapped[float] = mapped_column(Float, nullable=False)               # CPU usage percentage
    memory: Mapped[float] = mapped_column(Float, nullable=False)            # Memory usage percentage
    uptime: Mapped[int] = mapped_column(BigInteger, nullable=False)         # Uptime in seconds
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # Relationships
    sensor: Mapped["OTSensor"] = relationship(back_populates="health_logs")

    # Composite index for fast time-series queries per sensor
    __table_args__ = (
        Index('idx_sensor_timestamp', 'sensor_id', 'timestamp'),
    )
    