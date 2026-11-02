import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# SQLite database path
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DATA_DIR / 'codeguard.db'}")

# File upload limits
MAX_UPLOAD_SIZE_BYTES = 25 * 1024 * 1024  # 25 MB
ALLOWED_EXTENSIONS = {".py", ".zip"}

# Application settings
APP_NAME = "CodeGuard Security & Quality Platform"
API_V1_PREFIX = "/api/v1"
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
