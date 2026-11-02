import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Scan(Base):
    __tablename__ = "scans"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False, index=True)
    scan_number = Column(Integer, default=1)
    status = Column(String(20), default="COMPLETED", index=True)  # PENDING, RUNNING, COMPLETED, FAILED
    total_files = Column(Integer, default=0)
    total_findings = Column(Integer, default=0)
    critical_count = Column(Integer, default=0)
    high_count = Column(Integer, default=0)
    medium_count = Column(Integer, default=0)
    low_count = Column(Integer, default=0)
    duration_seconds = Column(Float, default=0.0)
    scan_type = Column(String(20), default="ZIP_UPLOAD")  # SINGLE_FILE, ZIP_UPLOAD
    created_at = Column(DateTime, default=datetime.datetime.utcnow, index=True)

    # Relationships
    project = relationship("Project", back_populates="scans")
    findings = relationship("Finding", back_populates="scan", cascade="all, delete-orphan", order_by="Finding.id")
    files = relationship("ScanFile", back_populates="scan", cascade="all, delete-orphan")


class ScanFile(Base):
    __tablename__ = "scan_files"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    scan_id = Column(Integer, ForeignKey("scans.id", ondelete="CASCADE"), nullable=False, index=True)
    relative_path = Column(String(255), nullable=False)
    file_size_bytes = Column(Integer, default=0)
    line_count = Column(Integer, default=0)
    status = Column(String(20), default="SCANNED")  # SCANNED, SYNTAX_ERROR, SKIPPED

    # Relationship
    scan = relationship("Scan", back_populates="files")
