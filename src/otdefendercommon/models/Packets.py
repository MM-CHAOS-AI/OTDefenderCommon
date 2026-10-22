from datetime import datetime
from typing import List, Optional
from sqlalchemy import (
    String, Text, Integer, BigInteger, Float, LargeBinary, 
    ForeignKey, DateTime, Index, event
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.engine import Engine

from otdefendercommon.database.base import Base


class Packets(Base):
    __tablename__ = "packets"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    session_id: Mapped[int] = mapped_column(ForeignKey("capture_sessions_files.id", ondelete="CASCADE"), index=True)
    interface_id: Mapped[Optional[int]] = mapped_column(ForeignKey("capture_interfaces.id", ondelete="SET NULL"), nullable=True)
    
    packet_index: Mapped[int] = mapped_column(BigInteger, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime, nullable=False)  # High-precision datetime[cite: 6]
    captured_length: Mapped[int] = mapped_column(Integer, nullable=False)
    original_length: Mapped[int] = mapped_column(Integer, nullable=False)
    
    # MAC Metadata fields (set to 'NOI' if not available)
    src_mac: Mapped[Optional[str]] = mapped_column(String(20), index=True, nullable=True)
    dst_mac: Mapped[Optional[str]] = mapped_column(String(20), index=True, nullable=True)

    # Indexed L3/L4/OT Metadata for rapid query filters[cite: 6]
    src_ip: Mapped[Optional[str]] = mapped_column(String(45), index=True, nullable=True)
    dst_ip: Mapped[Optional[str]] = mapped_column(String(45), index=True, nullable=True)
    protocol: Mapped[Optional[str]] = mapped_column(String(30), index=True, nullable=True) # e.g., 'MODBUS', 'DNP3'[cite: 6]
    src_port: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    dst_port: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    
    # Raw packet data payload stored as SQLite BLOB[cite: 6]
    payload: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)

    # Relationships[cite: 6]
    session: Mapped["CaptureSessionFiles"] = relationship(back_populates="packets")
    interface: Mapped[Optional["CaptureInterfaces"]] = relationship(back_populates="packets")

    # Composite indexes for common analytical queries[cite: 6]
    __table_args__ = (
        Index('idx_session_timestamp', 'session_id', 'timestamp'),
        Index('idx_ips_packets', 'src_ip', 'dst_ip'),
        Index('idx_macs_packets', 'src_mac', 'dst_mac'),
    )

    