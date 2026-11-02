from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import APP_NAME, API_V1_PREFIX
from app.database import engine, Base, SessionLocal
from app.models.project import Project
from app.routers import projects, scans, findings, reports

# Initialize database schema tables
Base.metadata.create_all(bind=engine)

# Seed an initial default project if empty
def seed_initial_data():
    db = SessionLocal()
    try:
        if db.query(Project).count() == 0:
            default_proj = Project(
                name="Demo Python Project",
                description="Default workspace created for quick security & quality testing.",
                repo_url="https://github.com/example/demo-api"
            )
            db.add(default_proj)
            db.commit()
    finally:
        db.close()

seed_initial_data()

app = FastAPI(
    title=APP_NAME,
    description="Intelligent Source Code Quality Assessment and Security Vulnerability Detection Platform using Python, Bandit, Ruff, and AST.",
    version="1.0.0"
)

# Configure Cross-Origin Resource Sharing (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins in development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routers
app.include_router(projects.router, prefix=API_V1_PREFIX)
app.include_router(scans.router, prefix=API_V1_PREFIX)
app.include_router(findings.router, prefix=API_V1_PREFIX)
app.include_router(reports.router, prefix=API_V1_PREFIX)

@app.get("/")
def root():
    return {
        "platform": APP_NAME,
        "status": "online",
        "documentation": "/docs",
        "api_v1": API_V1_PREFIX
    }

@app.get("/api/health")
def health_check():
    return {"status": "healthy", "service": "CodeGuard Backend"}
