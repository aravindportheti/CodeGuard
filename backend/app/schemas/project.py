import datetime
from typing import List, Optional
from pydantic import BaseModel
from app.schemas.scan import ScanSummaryResponse

class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    repo_url: Optional[str] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    scans_count: int = 0
    latest_scan: Optional[ScanSummaryResponse] = None

    class Config:
        from_attributes = True

class ProjectDetailResponse(ProjectBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    scans: List[ScanSummaryResponse] = []

    class Config:
        from_attributes = True
