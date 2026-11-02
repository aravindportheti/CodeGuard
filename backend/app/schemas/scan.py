import datetime
from typing import List, Optional, Dict
from pydantic import BaseModel
from app.schemas.finding import FindingResponse

class ScanFileResponse(BaseModel):
    id: int
    relative_path: str
    file_size_bytes: int
    line_count: int
    status: str

    class Config:
        from_attributes = True

class ScanMetrics(BaseModel):
    critical: int
    high: int
    medium: int
    low: int
    total: int

class ScanSummaryResponse(BaseModel):
    id: int
    project_id: int
    scan_number: int
    status: str
    total_files: int
    total_findings: int
    critical_count: int
    high_count: int
    medium_count: int
    low_count: int
    duration_seconds: float
    scan_type: str
    created_at: datetime.datetime

    class Config:
        from_attributes = True

class ScanDetailResponse(ScanSummaryResponse):
    findings: List[FindingResponse] = []
    files: List[ScanFileResponse] = []

class ScanDiffResult(BaseModel):
    baseline_scan_id: int
    current_scan_id: int
    new_findings: List[FindingResponse] = []
    fixed_findings: List[FindingResponse] = []
    recurring_findings: List[FindingResponse] = []
    metrics: Dict[str, int]
