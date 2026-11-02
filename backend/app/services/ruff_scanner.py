import os
import json
import subprocess
from typing import List, Dict, Any

def run_ruff_scan(target_dir: str) -> List[Dict[str, Any]]:
    """
    Executes the Ruff quality and security linter on the target directory.
    Uses shell=False to strictly prevent command injection.
    NEVER executes the analyzed code.
    """
    findings: List[Dict[str, Any]] = []
    real_target_dir = os.path.realpath(target_dir)

    cmd = [
        "ruff", "check", real_target_dir,
        "--output-format=json",
        "--select=E,W,F,B,C90,S,UP",
        "--exit-zero",
        "--no-cache"
    ]

    try:
        proc = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=False,
            timeout=45
        )

        output_str = proc.stdout.strip()
        if not output_str:
            return findings

        violations = json.loads(output_str)
        if not isinstance(violations, list):
            return findings

        for item in violations:
            code = item.get("code", "RUFF")
            message = item.get("message", "")
            raw_filename = item.get("filename", "")

            try:
                rel_path = os.path.relpath(raw_filename, real_target_dir).replace("\\", "/")
            except ValueError:
                rel_path = os.path.basename(raw_filename)

            location = item.get("location", {})
            row = location.get("row", 1)
            column = location.get("column", 1)
            end_location = item.get("end_location", {})
            end_row = end_location.get("row", row)

            # Map Ruff severity
            # S codes (flake8-bandit) are security issues
            if code.startswith("S102") or code.startswith("S608") or code.startswith("S506"):
                severity = "CRITICAL"
                cwe_id = "CWE-89" if "S608" in code else ("CWE-95" if "S102" in code else "CWE-502")
            elif code.startswith("S") or code.startswith("E9") or code.startswith("F8"):
                severity = "HIGH"
                cwe_id = "CWE-798" if "S105" in code or "S106" in code else "CWE-398"
            elif code.startswith("B") or code == "C901":
                severity = "MEDIUM"
                cwe_id = "CWE-1007" if code == "C901" else "CWE-703"
            else:
                severity = "LOW"
                cwe_id = "CWE-1078"

            rule_name = f"Ruff: {code}"
            if code == "C901":
                rule_name = "Ruff: High Cyclomatic Complexity (C901)"
            elif code.startswith("F401"):
                rule_name = "Ruff: Unused Import (F401)"
            elif code.startswith("E501"):
                rule_name = "Ruff: Line Too Long (E501)"
            elif code.startswith("S"):
                rule_name = f"Ruff Security Check ({code})"

            findings.append({
                "tool_source": "RUFF",
                "rule_id": code,
                "rule_name": rule_name,
                "severity": severity,
                "cwe_id": cwe_id,
                "file_path": rel_path,
                "line_number": row,
                "end_line": end_row,
                "column_number": column,
                "description": message,
                "code_snippet": None
            })

    except subprocess.TimeoutExpired:
        findings.append({
            "tool_source": "RUFF",
            "rule_id": "RUFF-TIMEOUT",
            "rule_name": "Ruff Analysis Timeout",
            "severity": "LOW",
            "cwe_id": None,
            "file_path": ".",
            "line_number": 1,
            "column_number": 0,
            "description": "Ruff linter timed out after 45 seconds."
        })
    except Exception as e:
        findings.append({
            "tool_source": "RUFF",
            "rule_id": "RUFF-EXEC-WARNING",
            "rule_name": "Ruff Scanner Notice",
            "severity": "LOW",
            "cwe_id": None,
            "file_path": ".",
            "line_number": 1,
            "column_number": 0,
            "description": f"Ruff execution notice: {str(e)}"
        })

    return findings
