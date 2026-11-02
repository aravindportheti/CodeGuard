import datetime
from typing import Optional
from pydantic import BaseModel

class FindingBase(BaseModel):
    tool_source: str
    rule_id: str
    rule_name: str
    severity: str
    cwe_id: Optional[str] = None
    file_path: str
    line_number: int
    end_line: Optional[int] = None
    column_number: int = 0
    description: str
    code_snippet: Optional[str] = None
    status: str = "OPEN"
    ai_explanation: Optional[str] = None

class FindingCreate(FindingBase):
    pass

class FindingStatusUpdate(BaseModel):
    status: str  # OPEN, RESOLVED, FALSE_POSITIVE

class FindingResponse(FindingBase):
    id: int
    scan_id: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True
