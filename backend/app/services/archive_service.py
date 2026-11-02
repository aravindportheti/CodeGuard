import os
import zipfile
import tempfile
from typing import List, Tuple, Dict, Any
from fastapi import HTTPException, status
from app.config import MAX_UPLOAD_SIZE_BYTES, ALLOWED_EXTENSIONS

class ExtractedFileMeta:
    def __init__(self, relative_path: str, full_path: str, size_bytes: int, line_count: int):
        self.relative_path = relative_path
        self.full_path = full_path
        self.size_bytes = size_bytes
        self.line_count = line_count

def count_lines(filepath: str) -> int:
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            return sum(1 for _ in f)
    except Exception:
        return 0

def safe_extract_archive(
    file_bytes: bytes, 
    original_filename: str, 
    temp_dir: str
) -> Tuple[List[ExtractedFileMeta], str]:
    """
    Safely validates and extracts an uploaded file (.py or .zip).
    Implements strict defense against Zip-Slip path traversal attacks.
    NEVER executes any uploaded code.
    """
    if len(file_bytes) > MAX_UPLOAD_SIZE_BYTES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Uploaded file exceeds maximum limit of {MAX_UPLOAD_SIZE_BYTES // (1024*1024)} MB."
        )

    ext = os.path.splitext(original_filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported file format '{ext}'. Allowed formats: .py, .zip"
        )

    resolved_temp_dir = os.path.realpath(temp_dir)
    extracted_files: List[ExtractedFileMeta] = []

    if ext == ".py":
        # Single Python source file
        clean_filename = os.path.basename(original_filename)
        dest_path = os.path.join(resolved_temp_dir, clean_filename)
        with open(dest_path, "wb") as f:
            f.write(file_bytes)

        lines = count_lines(dest_path)
        size = len(file_bytes)
        meta = ExtractedFileMeta(clean_filename, dest_path, size, lines)
        extracted_files.append(meta)
        return extracted_files, "SINGLE_FILE"

    elif ext == ".zip":
        temp_zip = os.path.join(resolved_temp_dir, "upload_temp.zip")
        with open(temp_zip, "wb") as f:
            f.write(file_bytes)

        if not zipfile.is_zipfile(temp_zip):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The uploaded file is not a valid or readable ZIP archive."
            )

        with zipfile.ZipFile(temp_zip, "r") as archive:
            for member in archive.infolist():
                member_path = member.filename
                # Path Traversal Guard (Zip-Slip Prevention)
                destination_path = os.path.realpath(os.path.join(resolved_temp_dir, member_path))

                if not destination_path.startswith(resolved_temp_dir + os.sep) and destination_path != resolved_temp_dir:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"Security Alert: Zip-Slip path traversal detected in member '{member_path}'."
                    )

                if member.is_dir():
                    os.makedirs(destination_path, exist_ok=True)
                else:
                    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
                    with archive.open(member) as src, open(destination_path, "wb") as dst:
                        dst.write(src.read())

                    # Filter for Python source files
                    if destination_path.endswith(".py"):
                        rel_path = os.path.relpath(destination_path, resolved_temp_dir)
                        # Normalize forward slashes for clean presentation
                        rel_path_clean = rel_path.replace("\\", "/")
                        size = os.path.getsize(destination_path)
                        lines = count_lines(destination_path)
                        extracted_files.append(ExtractedFileMeta(rel_path_clean, destination_path, size, lines))

        # Remove temporary zip container
        try:
            os.remove(temp_zip)
        except OSError:
            pass

        if not extracted_files:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The uploaded ZIP archive contains no Python (.py) source files."
            )

        return extracted_files, "ZIP_UPLOAD"

    return [], "UNKNOWN"
