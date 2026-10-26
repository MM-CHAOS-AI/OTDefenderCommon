from datetime import datetime
from typing import List, Optional
from sqlalchemy import (
    String, Text, Integer, BigInteger, LargeBinary, 
    ForeignKey, DateTime, Index, Boolean
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from otdefendercommon.database.base import Base


class LivePackets(Base):
    __tablename__ = "live_packets"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    asset_id: Mapped[int] = mapped_column(ForeignKey("ot_assets.id", ondelete="RESTRICT"), index=True, nullable=False)
    in_sensor_id: Mapped[int] = mapped_column(Integer, nullable=False)
    interface_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    interface_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    
    packet_index: Mapped[int] = mapped_column(BigInteger, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    captured_length: Mapped[int] = mapped_column(Integer, nullable=False)
    original_length: Mapped[int] = mapped_column(Integer, nullable=False)
    
    # Gap detection fields
    is_gap: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    gap_size: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    
    # Packet-level comments from PCAPNG Enhanced Packet Blocks
    packet_comment: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    
    # MAC Metadata fields
    src_mac: Mapped[Optional[str]] = mapped_column(String(20), index=True, nullable=True)
    dst_mac: Mapped[Optional[str]] = mapped_column(String(20), index=True, nullable=True)

    # Indexed L3/L4/OT Metadata
    src_ip: Mapped[Optional[str]] = mapped_column(String(45), index=True, nullable=True)
    dst_ip: Mapped[Optional[str]] = mapped_column(String(45), index=True, nullable=True)
    protocol: Mapped[Optional[str]] = mapped_column(String(30), index=True, nullable=True)
    src_port: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    dst_port: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    
    # Raw packet data payload
    payload: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)

    # Relationships
    asset: Mapped["OTAssets"] = relationship(back_populates="packets")

    __table_args__ = (
        Index('idx_asset_timestamp', 'asset_id', 'timestamp'),
        Index('idx_ips_live_packets', 'src_ip', 'dst_ip'),
        Index('idx_macs_live_packets', 'src_mac', 'dst_mac'),
    )