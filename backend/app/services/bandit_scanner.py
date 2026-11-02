import os
import json
import subprocess
import sys
from typing import List, Dict, Any

def run_bandit_scan(target_dir: str) -> List[Dict[str, Any]]:
    """
    Executes Bandit SAST analyzer on the target directory using subprocess.
    Uses shell=False to strictly prevent shell command injection.
    NEVER executes the analyzed code.
    """
    findings: List[Dict[str, Any]] = []
    real_target_dir = os.path.realpath(target_dir)

    # Command to run Bandit
    # We invoke through sys.executable -m bandit to ensure it runs inside the active Python environment
    cmd = [
        sys.executable, "-m", "bandit",
        "-r", real_target_dir,
        "-f", "json",
        "--exit-zero"
    ]

    try:
        proc = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=False,
            timeout=60
        )
        
        output_str = proc.stdout.strip()
        if not output_str:
            return findings

        # Bandit outputs JSON report
        data = json.loads(output_str)
        results = data.get("results", [])

        for item in results:
            raw_filename = item.get("filename", "")
            # Convert absolute path to relative path
            try:
                rel_path = os.path.relpath(raw_filename, real_target_dir).replace("\\", "/")
            except ValueError:
                rel_path = os.path.basename(raw_filename)

            test_id = item.get("test_id", "B000")
            test_name = item.get("test_name", "Security Issue")
            issue_sev = item.get("issue_severity", "LOW").upper()
            issue_conf = item.get("issue_confidence", "LOW").upper()
            line_no = item.get("line_number", 1)
            issue_text = item.get("issue_text", "")
            code_text = item.get("code", "")
            cwe_info = item.get("issue_cwe", {})
            cwe_id = f"CWE-{cwe_info.get('id')}" if cwe_info.get("id") else None

            # Map Bandit severity & confidence to standard
            if issue_sev == "HIGH" and issue_conf in {"HIGH", "MEDIUM"}:
                standard_sev = "CRITICAL"
            elif issue_sev == "HIGH" or (issue_sev == "MEDIUM" and issue_conf == "HIGH"):
                standard_sev = "HIGH"
            elif issue_sev == "MEDIUM":
                standard_sev = "MEDIUM"
            else:
                standard_sev = "LOW"

            findings.append({
                "tool_source": "BANDIT",
                "rule_id": test_id,
                "rule_name": f"Bandit: {test_name}",
                "severity": standard_sev,
                "cwe_id": cwe_id,
                "file_path": rel_path,
                "line_number": line_no,
                "column_number": 0,
                "description": issue_text,
                "code_snippet": code_text
            })

    except subprocess.TimeoutExpired:
        findings.append({
            "tool_source": "BANDIT",
            "rule_id": "BANDIT-TIMEOUT",
            "rule_name": "Bandit Execution Timeout",
            "severity": "MEDIUM",
            "cwe_id": None,
            "file_path": ".",
            "line_number": 1,
            "column_number": 0,
            "description": "Bandit analysis timed out after 60 seconds."
        })
    except Exception as e:
        # Fallback or error logging
        findings.append({
            "tool_source": "BANDIT",
            "rule_id": "BANDIT-EXEC-ERROR",
            "rule_name": "Bandit Execution Warning",
            "severity": "LOW",
            "cwe_id": None,
            "file_path": ".",
            "line_number": 1,
            "column_number": 0,
            "description": f"Bandit scanner execution notice: {str(e)}"
        })

    return findings
