import os
import time
import tempfile
from typing import List, Optional
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.project import Project
from app.models.scan import Scan, ScanFile
from app.models.finding import Finding
from app.schemas.scan import (
    ScanSummaryResponse, ScanDetailResponse, ScanFileResponse, ScanDiffResult
)
from app.schemas.finding import FindingResponse
from app.services.archive_service import safe_extract_archive
from app.services.ast_analyzer import analyze_file_ast
from app.services.bandit_scanner import run_bandit_scan
from app.services.ruff_scanner import run_ruff_scan
from app.services.normalizer import normalize_all_findings
from app.services.diff_engine import compute_scan_diff

router = APIRouter(prefix="/scans", tags=["Scans"])

@router.post("/upload", response_model=ScanDetailResponse, status_code=status.HTTP_201_CREATED)
async def upload_and_scan(
    project_id: int = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    """
    Ingests a Python file or ZIP project archive, executes static analysis
    across AST, Bandit, and Ruff, normalizes findings, and saves results.
    NEVER executes the uploaded code.
    """
    start_time = time.time()

    # 1. Verify project exists
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Target project not found.")

    # 2. Read bytes
    try:
        contents = await file.read()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to read upload: {str(e)}")

    if not contents:
        raise HTTPException(status_code=400, detail="Uploaded file is empty.")

    # Determine scan number for this project
    existing_scans_count = db.query(Scan).filter(Scan.project_id == project_id).count()
    scan_number = existing_scans_count + 1

    # 3. Create Ephemeral Sandbox Directory for analysis
    with tempfile.TemporaryDirectory(prefix="codeguard_scan_") as temp_dir:
        # Safe extraction with Zip-Slip path traversal defense
        extracted_files, scan_type = safe_extract_archive(contents, file.filename, temp_dir)

        if not extracted_files:
            raise HTTPException(
                status_code=400,
                detail="No readable Python (.py) source files were found in the uploaded package."
            )

        # 4. Engine 1: Python AST Analysis (per file)
        ast_findings = []
        for fmeta in extracted_files:
            file_ast_res = analyze_file_ast(fmeta.relative_path, fmeta.full_path)
            ast_findings.extend(file_ast_res)

        # 5. Engine 2: Bandit SAST Scan
        bandit_findings = run_bandit_scan(temp_dir)

        # 6. Engine 3: Ruff Quality & Security Scan
        ruff_findings = run_ruff_scan(temp_dir)

        # 7. Normalization, Deduplication & Severity Mapping
        normalized_findings = normalize_all_findings(
            temp_dir, ast_findings, bandit_findings, ruff_findings
        )

        # Compute metric tallies
        crit_count = sum(1 for f in normalized_findings if f["severity"] == "CRITICAL")
        high_count = sum(1 for f in normalized_findings if f["severity"] == "HIGH")
        med_count = sum(1 for f in normalized_findings if f["severity"] == "MEDIUM")
        low_count = sum(1 for f in normalized_findings if f["severity"] == "LOW")
        duration = round(time.time() - start_time, 2)

        # 8. Database Persistence
        scan_record = Scan(
            project_id=project_id,
            scan_number=scan_number,
            status="COMPLETED",
            total_files=len(extracted_files),
            total_findings=len(normalized_findings),
            critical_count=crit_count,
            high_count=high_count,
            medium_count=med_count,
            low_count=low_count,
            duration_seconds=duration,
            scan_type=scan_type
        )
        db.add(scan_record)
        db.flush()

        # Add scan files manifest
        for fmeta in extracted_files:
            db_file = ScanFile(
                scan_id=scan_record.id,
                relative_path=fmeta.relative_path,
                file_size_bytes=fmeta.size_bytes,
                line_count=fmeta.line_count,
                status="SCANNED"
            )
            db.add(db_file)

        # Add normalized findings
        saved_findings = []
        for item in normalized_findings:
            db_finding = Finding(
                scan_id=scan_record.id,
                tool_source=item["tool_source"],
                rule_id=item["rule_id"],
                rule_name=item["rule_name"],
                severity=item["severity"],
                cwe_id=item.get("cwe_id"),
                file_path=item["file_path"],
                line_number=item["line_number"],
                end_line=item.get("end_line"),
                column_number=item.get("column_number", 0),
                description=item["description"],
                code_snippet=item.get("code_snippet"),
                status="OPEN",
                ai_explanation=item.get("ai_explanation")
            )
            db.add(db_finding)
            saved_findings.append(db_finding)

        db.commit()
        db.refresh(scan_record)

    # Convert to response DTO
    findings_response = [FindingResponse.from_orm(f) for f in scan_record.findings]
    files_response = [ScanFileResponse.from_orm(f) for f in scan_record.files]

    return ScanDetailResponse(
        id=scan_record.id,
        project_id=scan_record.project_id,
        scan_number=scan_record.scan_number,
        status=scan_record.status,
        total_files=scan_record.total_files,
        total_findings=scan_record.total_findings,
        critical_count=scan_record.critical_count,
        high_count=scan_record.high_count,
        medium_count=scan_record.medium_count,
        low_count=scan_record.low_count,
        duration_seconds=scan_record.duration_seconds,
        scan_type=scan_record.scan_type,
        created_at=scan_record.created_at,
        findings=findings_response,
        files=files_response
    )

@router.get("", response_model=List[ScanSummaryResponse])
def list_scans(
    project_id: Optional[int] = Query(None, description="Filter by project ID"),
    db: Session = Depends(get_db)
):
    query = db.query(Scan)
    if project_id is not None:
        query = query.filter(Scan.project_id == project_id)
    scans = query.order_by(Scan.id.desc()).all()
    return [ScanSummaryResponse.from_orm(s) for s in scans]

@router.get("/{scan_id}", response_model=ScanDetailResponse)
def get_scan(scan_id: int, db: Session = Depends(get_db)):
    scan = db.query(Scan).filter(Scan.id == scan_id).first()
    if not scan:
        raise HTTPException(status_code=404, detail="Scan record not found.")

    findings_response = [FindingResponse.from_orm(f) for f in scan.findings]
    files_response = [ScanFileResponse.from_orm(f) for f in scan.files]

    return ScanDetailResponse(
        id=scan.id,
        project_id=scan.project_id,
        scan_number=scan.scan_number,
        status=scan.status,
        total_files=scan.total_files,
        total_findings=scan.total_findings,
        critical_count=scan.critical_count,
        high_count=scan.high_count,
        medium_count=scan.medium_count,
        low_count=scan.low_count,
        duration_seconds=scan.duration_seconds,
        scan_type=scan.scan_type,
        created_at=scan.created_at,
        findings=findings_response,
        files=files_response
    )

@router.delete("/{scan_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_scan(scan_id: int, db: Session = Depends(get_db)):
    scan = db.query(Scan).filter(Scan.id == scan_id).first()
    if not scan:
        raise HTTPException(status_code=404, detail="Scan not found")
    db.delete(scan)
    db.commit()
    return None

@router.get("/{scan_id}/diff/{baseline_id}", response_model=ScanDiffResult)
def get_scan_diff(scan_id: int, baseline_id: int, db: Session = Depends(get_db)):
    """
    Compares the current scan against a baseline scan to categorize findings
    into New (regressions), Fixed (resolved), and Recurring issues.
    """
    current_scan = db.query(Scan).filter(Scan.id == scan_id).first()
    baseline_scan = db.query(Scan).filter(Scan.id == baseline_id).first()

    if not current_scan or not baseline_scan:
        raise HTTPException(status_code=404, detail="One or both scans not found for diff comparison.")

    diff_data = compute_scan_diff(baseline_scan.findings, current_scan.findings)

    return ScanDiffResult(
        baseline_scan_id=baseline_id,
        current_scan_id=scan_id,
        new_findings=[FindingResponse.from_orm(f) for f in diff_data["new_findings"]],
        fixed_findings=[FindingResponse.from_orm(f) for f in diff_data["fixed_findings"]],
        recurring_findings=[FindingResponse.from_orm(f) for f in diff_data["recurring_findings"]],
        metrics=diff_data["metrics"]
    )
