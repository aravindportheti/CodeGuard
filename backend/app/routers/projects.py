from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.project import Project
from app.models.scan import Scan
from app.schemas.project import ProjectCreate, ProjectResponse, ProjectDetailResponse
from app.schemas.scan import ScanSummaryResponse

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.get("", response_model=List[ProjectResponse])
def list_projects(db: Session = Depends(get_db)):
    projects = db.query(Project).order_by(Project.id.desc()).all()
    results = []
    for p in projects:
        scans_count = len(p.scans)
        latest_scan = p.scans[0] if p.scans else None
        results.append(ProjectResponse(
            id=p.id,
            name=p.name,
            description=p.description,
            repo_url=p.repo_url,
            created_at=p.created_at,
            updated_at=p.updated_at,
            scans_count=scans_count,
            latest_scan=ScanSummaryResponse.from_orm(latest_scan) if latest_scan else None
        ))
    return results

@router.post("", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(payload: ProjectCreate, db: Session = Depends(get_db)):
    project = Project(
        name=payload.name,
        description=payload.description,
        repo_url=payload.repo_url
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return ProjectResponse(
        id=project.id,
        name=project.name,
        description=project.description,
        repo_url=project.repo_url,
        created_at=project.created_at,
        updated_at=project.updated_at,
        scans_count=0,
        latest_scan=None
    )

@router.get("/{project_id}", response_model=ProjectDetailResponse)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    scans_list = [ScanSummaryResponse.from_orm(s) for s in project.scans]
    return ProjectDetailResponse(
        id=project.id,
        name=project.name,
        description=project.description,
        repo_url=project.repo_url,
        created_at=project.created_at,
        updated_at=project.updated_at,
        scans=scans_list
    )

@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    db.delete(project)
    db.commit()
    return None
