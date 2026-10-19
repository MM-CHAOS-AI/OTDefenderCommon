from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, Text, Integer, Float, DateTime, ForeignKey, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from otdefendermain.database.db_manager import Base


class OTAssetHealth(Base):
    __tablename__ = "ot_asset_health"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    asset_id: Mapped[int] = mapped_column(ForeignKey("ot_assets.id", ondelete="CASCADE"), index=True)
    health_status: Mapped[str] = mapped_column(String(50), nullable=False)
    last_packet_timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    # Relationships
    asset: Mapped["OTAssets"] = relationship(back_populates="health_logs")

    # Composite index for fast asset time-series historical checks
    __table_args__ = (
        Index('idx_asset_health_timestamp', 'asset_id', 'timestamp'),
    )