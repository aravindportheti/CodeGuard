from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.scan import Scan
from app.services.report_service import generate_pdf_report, generate_json_report

router = APIRouter(prefix="/reports", tags=["Reports"])

@router.get("/{scan_id}/pdf")
def download_pdf_report(scan_id: int, db: Session = Depends(get_db)):
    scan = db.query(Scan).filter(Scan.id == scan_id).first()
    if not scan:
        raise HTTPException(status_code=404, detail="Scan record not found.")

    pdf_bytes = generate_pdf_report(scan.project, scan, scan.findings)
    filename = f"CodeGuard_Report_Scan_{scan.id}_{scan.project.name.replace(' ', '_')}.pdf"

    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename=\"{filename}\""
        }
    )

@router.get("/{scan_id}/json")
def download_json_report(scan_id: int, db: Session = Depends(get_db)):
    scan = db.query(Scan).filter(Scan.id == scan_id).first()
    if not scan:
        raise HTTPException(status_code=404, detail="Scan record not found.")

    report_dict = generate_json_report(scan.project, scan, scan.findings)
    return report_dict
