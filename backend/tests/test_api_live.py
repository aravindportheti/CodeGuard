import os
import sys

# Ensure backend root is on sys.path
sys.path.insert(0, os.path.abspath("backend"))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def run_api_tests():
    print("=== Testing CodeGuard FastAPI Endpoints ===")

    # 1. Health check
    res = client.get("/api/health")
    assert res.status_code == 200, f"Health check failed: {res.text}"
    print("[PASS] GET /api/health:", res.json())

    # 2. List projects
    res = client.get("/api/v1/projects")
    assert res.status_code == 200, f"List projects failed: {res.text}"
    projects = res.json()
    assert len(projects) > 0, "No projects returned"
    proj_id = projects[0]["id"]
    print(f"[PASS] GET /api/v1/projects: Found {len(projects)} project(s). Using Project ID: {proj_id}")

    # 3. Test single .py file scan upload (samples/vulnerable_app.py)
    vuln_path = os.path.abspath("samples/vulnerable_app.py")
    assert os.path.exists(vuln_path)

    with open(vuln_path, "rb") as f:
        upload_res = client.post(
            "/api/v1/scans/upload",
            data={"project_id": str(proj_id)},
            files={"file": ("vulnerable_app.py", f, "text/x-python")}
        )
    assert upload_res.status_code == 201, f"Upload failed: {upload_res.text}"
    scan_data = upload_res.json()
    scan_id_1 = scan_data["id"]
    print(f"[PASS] POST /api/v1/scans/upload (vulnerable_app.py): Created Scan #{scan_id_1} with {scan_data['total_findings']} findings!")
    print(f"       Metrics -> Crit: {scan_data['critical_count']}, High: {scan_data['high_count']}, Med: {scan_data['medium_count']}, Low: {scan_data['low_count']}")

    # 4. Test ZIP project upload (samples/sample_project.zip)
    zip_path = os.path.abspath("samples/sample_project.zip")
    assert os.path.exists(zip_path)

    with open(zip_path, "rb") as f:
        zip_res = client.post(
            "/api/v1/scans/upload",
            data={"project_id": str(proj_id)},
            files={"file": ("sample_project.zip", f, "application/zip")}
        )
    assert zip_res.status_code == 201, f"ZIP upload failed: {zip_res.text}"
    scan_data_2 = zip_res.json()
    scan_id_2 = scan_data_2["id"]
    print(f"[PASS] POST /api/v1/scans/upload (sample_project.zip): Created Scan #{scan_id_2} with {scan_data_2['total_findings']} findings across {scan_data_2['total_files']} files!")

    # 5. Test Scan Diff between scan_id_2 and scan_id_1
    diff_res = client.get(f"/api/v1/scans/{scan_id_2}/diff/{scan_id_1}")
    assert diff_res.status_code == 200, f"Scan diff failed: {diff_res.text}"
    diff_data = diff_res.json()
    print(f"[PASS] GET /api/v1/scans/{scan_id_2}/diff/{scan_id_1}: Diff metrics -> {diff_data['metrics']}")

    # 6. Test PDF report download
    pdf_res = client.get(f"/api/v1/reports/{scan_id_1}/pdf")
    assert pdf_res.status_code == 200, f"PDF report failed: {pdf_res.text}"
    assert pdf_res.headers["content-type"] == "application/pdf"
    assert len(pdf_res.content) > 1000, "PDF content is too small"
    print(f"[PASS] GET /api/v1/reports/{scan_id_1}/pdf: Generated valid PDF binary stream ({len(pdf_res.content)} bytes)!")

    # 7. Test JSON report download
    json_res = client.get(f"/api/v1/reports/{scan_id_1}/json")
    assert json_res.status_code == 200, f"JSON report failed: {json_res.text}"
    json_data = json_res.json()
    assert json_data["report_type"] == "CodeGuard_Audit_Report"
    print(f"[PASS] GET /api/v1/reports/{scan_id_1}/json: Validated structured audit JSON export!")

    # 8. Test Finding status update (Mark as Resolved)
    if scan_data["findings"]:
        finding_id = scan_data["findings"][0]["id"]
        patch_res = client.patch(f"/api/v1/findings/{finding_id}/status", json={"status": "RESOLVED"})
        assert patch_res.status_code == 200
        assert patch_res.json()["status"] == "RESOLVED"
        print(f"[PASS] PATCH /api/v1/findings/{finding_id}/status: Successfully transitioned to RESOLVED!")

    print("\n=== ALL API TESTS PASSED SUCCESSFULLY! ===")

if __name__ == "__main__":
    run_api_tests()
