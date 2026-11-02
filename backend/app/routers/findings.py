from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.finding import Finding
from app.schemas.finding import FindingResponse, FindingStatusUpdate

router = APIRouter(prefix="/findings", tags=["Findings"])

@router.get("", response_model=List[FindingResponse])
def list_findings(
    scan_id: Optional[int] = Query(None, description="Filter by scan ID"),
    severity: Optional[str] = Query(None, description="Filter by severity (CRITICAL, HIGH, MEDIUM, LOW)"),
    tool_source: Optional[str] = Query(None, description="Filter by tool (BANDIT, RUFF, AST)"),
    status: Optional[str] = Query(None, description="Filter by status (OPEN, RESOLVED, FALSE_POSITIVE)"),
    db: Session = Depends(get_db)
):
    query = db.query(Finding)
    if scan_id is not None:
        query = query.filter(Finding.scan_id == scan_id)
    if severity:
        query = query.filter(Finding.severity == severity.upper())
    if tool_source:
        query = query.filter(Finding.tool_source == tool_source.upper())
    if status:
        query = query.filter(Finding.status == status.upper())

    findings = query.order_by(Finding.id.asc()).all()
    return [FindingResponse.from_orm(f) for f in findings]

@router.patch("/{finding_id}/status", response_model=FindingResponse)
def update_finding_status(
    finding_id: int,
    payload: FindingStatusUpdate,
    db: Session = Depends(get_db)
):
    valid_statuses = {"OPEN", "RESOLVED", "FALSE_POSITIVE"}
    new_status = payload.status.upper()
    if new_status not in valid_statuses:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid status '{payload.status}'. Allowed: {', '.join(valid_statuses)}"
        )

    finding = db.query(Finding).filter(Finding.id == finding_id).first()
    if not finding:
        raise HTTPException(status_code=404, detail="Finding record not found.")

    finding.status = new_status
    db.commit()
    db.refresh(finding)
    return FindingResponse.from_orm(finding)
