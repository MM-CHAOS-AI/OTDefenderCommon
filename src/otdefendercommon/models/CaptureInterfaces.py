from datetime import datetime
from typing import List, Optional
from sqlalchemy import (
    String, Text, Integer, BigInteger, Float, LargeBinary, 
    ForeignKey, DateTime, Index, event
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.engine import Engine

from otdefendercommon.database.base import Base



class CaptureInterfaces(Base):
    __tablename__ = "capture_interfaces"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    session_id: Mapped[int] = mapped_column(ForeignKey("capture_sessions_files.id", ondelete="CASCADE"), index=True)
    interface_id_in_file: Mapped[int] = mapped_column(Integer, nullable=False)  # e.g., 0, 1 from IDB[cite: 2]
    name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)     # e.g., 'eth0'[cite: 2]
    link_type: Mapped[Optional[str]] = mapped_column(String(50), nullable=True) # e.g., 'EN10MB'[cite: 2]
    os_info: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    filter_string: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    mac_address: Mapped[Optional[str]] = mapped_column(String(17), nullable=True, index=True) # Added for MAC tracking

    # Relationships
    session: Mapped["CaptureSessionFiles"] = relationship(back_populates="interfaces")
    packets: Mapped[List["Packets"]] = relationship(back_populates="interface")
