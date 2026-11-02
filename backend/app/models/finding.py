import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Finding(Base):
    __tablename__ = "findings"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    scan_id = Column(Integer, ForeignKey("scans.id", ondelete="CASCADE"), nullable=False, index=True)
    tool_source = Column(String(20), nullable=False)  # BANDIT, RUFF, AST
    rule_id = Column(String(50), nullable=False, index=True)
    rule_name = Column(String(150), nullable=False)
    severity = Column(String(20), nullable=False, index=True)  # CRITICAL, HIGH, MEDIUM, LOW
    cwe_id = Column(String(20), nullable=True)  # e.g., CWE-89, CWE-95
    file_path = Column(String(255), nullable=False, index=True)
    line_number = Column(Integer, nullable=False)
    end_line = Column(Integer, nullable=True)
    column_number = Column(Integer, default=0)
    description = Column(Text, nullable=False)
    code_snippet = Column(Text, nullable=True)
    status = Column(String(20), default="OPEN", index=True)  # OPEN, RESOLVED, FALSE_POSITIVE
    ai_explanation = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationship
    scan = relationship("Scan", back_populates="findings")
