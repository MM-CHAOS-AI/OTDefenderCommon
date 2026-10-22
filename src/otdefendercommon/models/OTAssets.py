from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, Text, Integer, Float, DateTime, ForeignKey, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from otdefendercommon.database.base import Base



class OTAssets(Base):

    __tablename__ = "ot_assets"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    sensor_id: Mapped[int] = mapped_column(ForeignKey("ot_sensors.id", ondelete="CASCADE"), index=True)
    asset_name: Mapped[str] = mapped_column(String(255), nullable=False)
    asset_company: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    asset_description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    asset_type: Mapped[str] = mapped_column(String(255), nullable=False)               # Asset type as OT, PLC, IOT etc.
    mac: Mapped[str] = mapped_column(String(20), index=True, nullable=False)
    ip: Mapped[str] = mapped_column(String(45), index=True, nullable=False)
    ports: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)         # e.g., '502, 44818, 20000'
    criticality: Mapped[str] = mapped_column(String(50), nullable=False)     # e.g., 'High', 'Medium', 'Low'
    vulnerability_score: Mapped[int] = mapped_column(Integer, nullable=False)     # e.g.,  25, 35, 45 -- Need to come from Vulnerability score
    level: Mapped[str] = mapped_column(String(50), nullable=False)           # e.g., 'Level 1 (Control)' SCADA 
    registration_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    location: Mapped[str] = mapped_column(String(255), nullable=False)
    protocol: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)        # e.g., 'MODBUS', 'DNP3'
    software_version: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    updated_by: Mapped[str] = mapped_column(String(100), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # Port and protocol >>

    # Relationships
    sensor: Mapped["OTSensor"] = relationship(back_populates="assets")
    health_logs: Mapped[List["OTAssetHealth"]] = relationship(
        back_populates="asset", cascade="all, delete-orphan"
    )

    # Indexes for asset network lookups
    __table_args__ = (
        Index('idx_asset_ip_mac', 'ip', 'mac'),
    )
