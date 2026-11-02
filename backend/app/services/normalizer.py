import os
from typing import List, Dict, Any, Optional

def extract_code_snippet(file_path: str, target_dir: str, target_line: int, radius: int = 2) -> Optional[str]:
    """
    Extracts surrounding lines of source code context around the target line.
    """
    try:
        full_path = os.path.join(target_dir, file_path)
        if not os.path.exists(full_path):
            return None

        with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        total_lines = len(lines)
        if total_lines == 0 or target_line < 1:
            return None

        start_line = max(1, target_line - radius)
        end_line = min(total_lines, target_line + radius)

        snippet_lines = []
        for l_num in range(start_line, end_line + 1):
            line_text = lines[l_num - 1].rstrip()
            prefix = ">>>" if l_num == target_line else "   "
            snippet_lines.append(f"{prefix} {l_num:4d} | {line_text}")

        return "\n".join(snippet_lines)
    except Exception:
        return None


def generate_remediation_guidance(rule_id: str, cwe_id: Optional[str], description: str) -> str:
    """
    Generates plain-language root-cause analysis and actionable remediation advice.
    """
    rule = rule_id.upper()

    if "B608" in rule or "S608" in rule or cwe_id == "CWE-89":
        return (
            "Root Cause: String interpolation or formatting inside a database query string creates a direct SQL Injection vulnerability (CWE-89).\n"
            "Remediation: Use parameterized queries with bind variables instead of f-strings or string concatenation. "
            "Example: cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))"
        )
    elif "EVAL" in rule or "EXEC" in rule or "S102" in rule or cwe_id == "CWE-95":
        return (
            "Root Cause: Direct invocation of dynamic execution builtins (eval/exec) allows execution of arbitrary Python code (CWE-95).\n"
            "Remediation: Replace eval() with ast.literal_eval() for parsing safe literal data structures, or use dedicated mathematical parsing libraries."
        )
    elif "PICKLE" in rule or "S301" in rule or cwe_id == "CWE-502":
        return (
            "Root Cause: Untrusted deserialization via pickle allows attackers to instantiate arbitrary objects and execute system commands (CWE-502).\n"
            "Remediation: Replace pickle with safe structured serialization formats such as JSON (json.loads/json.dumps) or Protocol Buffers."
        )
    elif "HARDCODED" in rule or "B105" in rule or "S105" in rule or cwe_id == "CWE-798":
        return (
            "Root Cause: Storing plaintext passwords, API keys, or tokens in source code leads to credential leakage (CWE-798).\n"
            "Remediation: Store credentials in environment variables or a secure secret manager. "
            "Example: db_password = os.getenv('DB_PASSWORD')"
        )
    elif "WEAK-HASH" in rule or "B303" in rule or "S324" in rule or cwe_id == "CWE-328":
        return (
            "Root Cause: MD5 and SHA1 are cryptographically broken algorithms vulnerable to collision attacks (CWE-328).\n"
            "Remediation: For integrity or password verification, use SHA-256 (hashlib.sha256()) or modern adaptive hashing algorithms like bcrypt/Argon2."
        )
    elif "SHELL" in rule or "B602" in rule or "S602" in rule or cwe_id == "CWE-78":
        return (
            "Root Cause: Invoking subprocesses with shell=True exposes the command string to shell metacharacter injection (CWE-78).\n"
            "Remediation: Set shell=False and pass command arguments as an explicit array of strings: subprocess.run(['ls', '-la'], shell=False)"
        )
    elif "C901" in rule or "COMPLEXITY" in rule or cwe_id == "CWE-1007":
        return (
            "Root Cause: The function contains excessive decision branches, nested loops, or exception handlers, increasing cognitive complexity.\n"
            "Remediation: Refactor the function using the Extract Method pattern, decompose nested conditions into guard clauses, and delegate responsibility to helper functions."
        )
    elif "SYNTAX" in rule:
        return (
            "Root Cause: The Python interpreter cannot parse this statement due to invalid syntax tokens.\n"
            "Remediation: Correct the syntax error indicated at the line and column offset before running tests."
        )
    elif "F401" in rule:
        return (
            "Root Cause: A module or identifier was imported but never referenced in this file.\n"
            "Remediation: Remove the unused import statement to reduce memory footprint and prevent circular import side-effects."
        )
    else:
        return (
            f"Advisory: Review code line against rule {rule_id}. "
            "Ensure input validation, error handling, and adherence to secure coding standards."
        )


def normalize_all_findings(
    target_dir: str,
    ast_findings: List[Dict[str, Any]],
    bandit_findings: List[Dict[str, Any]],
    ruff_findings: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Combines, normalizes, deduplicates, and enriches findings from all three static analysis engines.
    """
    raw_combined = ast_findings + bandit_findings + ruff_findings
    normalized_list: List[Dict[str, Any]] = []
    seen_signatures = set()

    # Severity priority order
    severity_rank = {"CRITICAL": 4, "HIGH": 3, "MEDIUM": 2, "LOW": 1}

    for item in raw_combined:
        file_path = item.get("file_path", "").replace("\\", "/")
        line_num = item.get("line_number", 1)
        rule_id = item.get("rule_id", "GENERAL")
        tool = item.get("tool_source", "AST")

        # Deduplicate identical findings on the same line from same tool
        sig = f"{tool}:{rule_id}:{file_path}:{line_num}"
        if sig in seen_signatures:
            continue
        seen_signatures.add(sig)

        sev = item.get("severity", "LOW").upper()
        if sev not in severity_rank:
            sev = "LOW"

        # Extract code snippet context if not already present
        snippet = item.get("code_snippet")
        if not snippet and file_path and file_path != ".":
            snippet = extract_code_snippet(file_path, target_dir, line_num, radius=2)

        # Generate intelligent remediation guidance
        cwe = item.get("cwe_id")
        desc = item.get("description", "")
        remediation = generate_remediation_guidance(rule_id, cwe, desc)

        normalized_list.append({
            "tool_source": tool,
            "rule_id": rule_id,
            "rule_name": item.get("rule_name", rule_id),
            "severity": sev,
            "cwe_id": cwe,
            "file_path": file_path,
            "line_number": line_num,
            "end_line": item.get("end_line"),
            "column_number": item.get("column_number", 0),
            "description": desc,
            "code_snippet": snippet,
            "status": "OPEN",
            "ai_explanation": remediation
        })

    # Sort findings by severity (Critical first) then file path and line number
    normalized_list.sort(
        key=lambda x: (-severity_rank.get(x["severity"], 0), x["file_path"], x["line_number"])
    )

    return normalized_list
