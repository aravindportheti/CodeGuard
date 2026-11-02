import os
from report_styles import (
    add_heading_1, add_heading_2, add_heading_3, add_paragraph,
    add_bullet, add_callout, add_code_block, add_page_break, add_figure, create_styled_table
)

def build_part3(doc):
    # =========================================================================
    # SECTION 17: DATABASE DESIGN AND ER DIAGRAM
    # =========================================================================
    add_heading_1(doc, "17.0 DATABASE DESIGN AND ER DIAGRAM")
    
    add_paragraph(doc,
        "The CodeGuard database schema is engineered using PostgreSQL 16 to guarantee strict relational integrity, ACID transaction compliance, "
        "and optimal query performance. The schema supports multi-tenancy, historical scan tracking, fine-grained finding resolutions, "
        "and scan comparison metrics.")

    if os.path.exists("figures/er_diagram.png"):
        add_figure(doc, "figures/er_diagram.png", 
                   "Figure 7: Entity-Relationship (ER) Diagram of CodeGuard Database Schema", 
                   width_inches=6.2)

    add_heading_2(doc, "17.1 Relational Schema & Data Dictionary")
    add_paragraph(doc, "The comprehensive data dictionary defining tables, columns, data types, and constraints is provided below:")

    # Table 1: users
    add_heading_3(doc, "Table 1: users (User Authentication & Accounts)")
    headers_u = ["Column Name", "Data Type", "Constraints", "Description"]
    rows_u = [
        ["id", "UUID / SERIAL", "PK, NOT NULL", "Unique primary identifier for the user account"],
        ["username", "VARCHAR(50)", "UNIQUE, NOT NULL", "Unique alphanumeric user handle"],
        ["email", "VARCHAR(100)", "UNIQUE, NOT NULL", "User email address for alerts and notifications"],
        ["hashed_password", "VARCHAR(255)", "NOT NULL", "Bcrypt / PBKDF2 hashed password string with salt"],
        ["role", "VARCHAR(20)", "DEFAULT 'developer'", "Access role: 'developer', 'auditor', or 'admin'"],
        ["is_active", "BOOLEAN", "DEFAULT TRUE", "Status flag indicating whether account is active"],
        ["created_at", "TIMESTAMP WITH TZ", "DEFAULT CURRENT_TIMESTAMP", "Account registration timestamp"],
        ["updated_at", "TIMESTAMP WITH TZ", "ON UPDATE CURRENT_TIMESTAMP", "Timestamp of last profile update"]
    ]
    create_styled_table(doc, headers_u, rows_u, col_widths=[1.5, 1.5, 1.8, 2.2])

    # Table 2: projects
    add_heading_3(doc, "Table 2: projects (Workspace Project Registry)")
    headers_p = ["Column Name", "Data Type", "Constraints", "Description"]
    rows_p = [
        ["id", "UUID / SERIAL", "PK, NOT NULL", "Unique project workspace identifier"],
        ["user_id", "UUID / INT", "FK -> users(id) ON DELETE CASCADE", "Owner identifier referencing users table"],
        ["name", "VARCHAR(100)", "NOT NULL", "Human-readable project name (e.g., 'E-Commerce API')"],
        ["description", "TEXT", "NULLABLE", "Optional narrative description of codebase purpose"],
        ["repo_url", "VARCHAR(255)", "NULLABLE", "Associated source repository link (Git/VCS)"],
        ["created_at", "TIMESTAMP WITH TZ", "DEFAULT CURRENT_TIMESTAMP", "Project workspace creation timestamp"],
        ["updated_at", "TIMESTAMP WITH TZ", "ON UPDATE CURRENT_TIMESTAMP", "Timestamp of last modification"]
    ]
    create_styled_table(doc, headers_p, rows_p, col_widths=[1.5, 1.5, 1.8, 2.2])

    # Table 3: scans
    add_heading_3(doc, "Table 3: scans (Code Scan Audit Executions)")
    headers_s = ["Column Name", "Data Type", "Constraints", "Description"]
    rows_s = [
        ["id", "UUID / SERIAL", "PK, NOT NULL", "Unique scan execution identifier"],
        ["project_id", "UUID / INT", "FK -> projects(id) ON DELETE CASCADE", "Associated project workspace identifier"],
        ["scan_number", "INTEGER", "NOT NULL", "Monotonically increasing scan sequence number"],
        ["status", "VARCHAR(20)", "DEFAULT 'PENDING'", "Execution state: 'PENDING', 'RUNNING', 'COMPLETED', 'FAILED'"],
        ["total_files", "INTEGER", "DEFAULT 0", "Total number of Python files analyzed"],
        ["total_findings", "INTEGER", "DEFAULT 0", "Aggregate count of detected issues across all engines"],
        ["critical_count", "INTEGER", "DEFAULT 0", "Number of Critical severity findings"],
        ["high_count", "INTEGER", "DEFAULT 0", "Number of High severity findings"],
        ["medium_count", "INTEGER", "DEFAULT 0", "Number of Medium severity findings"],
        ["low_count", "INTEGER", "DEFAULT 0", "Number of Low severity findings"],
        ["duration_seconds", "DOUBLE PRECISION", "DEFAULT 0.0", "Total wall-clock duration of scan in seconds"],
        ["created_at", "TIMESTAMP WITH TZ", "DEFAULT CURRENT_TIMESTAMP", "Timestamp when scan was initiated"]
    ]
    create_styled_table(doc, headers_s, rows_s, col_widths=[1.5, 1.5, 1.8, 2.2])

    # Table 4: scan_files
    add_heading_3(doc, "Table 4: scan_files (Scanned Python File Manifest)")
    headers_sf = ["Column Name", "Data Type", "Constraints", "Description"]
    rows_sf = [
        ["id", "UUID / SERIAL", "PK, NOT NULL", "Unique scanned file record identifier"],
        ["scan_id", "UUID / INT", "FK -> scans(id) ON DELETE CASCADE", "Parent scan identifier"],
        ["relative_path", "VARCHAR(255)", "NOT NULL", "Relative file path within project (e.g. 'auth/login.py')"],
        ["file_size_bytes", "INTEGER", "NOT NULL", "Size of file in bytes"],
        ["line_count", "INTEGER", "NOT NULL", "Total lines of code (LOC) in file"],
        ["sha256_hash", "VARCHAR(64)", "NOT NULL", "SHA-256 content hash for change detection"],
        ["status", "VARCHAR(20)", "DEFAULT 'SCANNED'", "Status: 'SCANNED', 'SYNTAX_ERROR', 'SKIPPED'"]
    ]
    create_styled_table(doc, headers_sf, rows_sf, col_widths=[1.5, 1.5, 1.8, 2.2])

    # Table 5: findings
    add_heading_3(doc, "Table 5: findings (Normalized Vulnerability & Quality Issues)")
    headers_f = ["Column Name", "Data Type", "Constraints", "Description"]
    rows_f = [
        ["id", "UUID / SERIAL", "PK, NOT NULL", "Unique normalized finding identifier"],
        ["scan_id", "UUID / INT", "FK -> scans(id) ON DELETE CASCADE", "Parent scan identifier"],
        ["tool_source", "VARCHAR(20)", "NOT NULL", "Originating tool: 'BANDIT', 'RUFF', or 'AST'"],
        ["rule_id", "VARCHAR(50)", "NOT NULL", "Tool rule code (e.g., 'B608', 'C901', 'AST-EVAL')"],
        ["rule_name", "VARCHAR(150)", "NOT NULL", "Descriptive title of the violated rule"],
        ["severity", "VARCHAR(15)", "NOT NULL", "Standardized severity: 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW'"],
        ["cwe_id", "VARCHAR(20)", "NULLABLE", "Common Weakness Enumeration ID (e.g., 'CWE-89')"],
        ["file_path", "VARCHAR(255)", "NOT NULL", "Relative file path containing the finding"],
        ["line_number", "INTEGER", "NOT NULL", "Starting line number in source code"],
        ["end_line", "INTEGER", "NULLABLE", "Ending line number for multi-line issues"],
        ["column_number", "INTEGER", "DEFAULT 0", "Starting column offset"],
        ["description", "TEXT", "NOT NULL", "Detailed diagnostic message explaining the issue"],
        ["code_snippet", "TEXT", "NULLABLE", "Surrounding context code lines (±2 lines)"],
        ["status", "VARCHAR(20)", "DEFAULT 'OPEN'", "Resolution state: 'OPEN', 'RESOLVED', 'FALSE_POSITIVE'"],
        ["ai_explanation", "TEXT", "NULLABLE", "Generated AI root cause and remediation suggestion"]
    ]
    create_styled_table(doc, headers_f, rows_f, col_widths=[1.4, 1.5, 1.8, 2.3])

    # Table 6: scan_comparisons
    add_heading_3(doc, "Table 6: scan_comparisons (Revision Diffing Index)")
    headers_sc = ["Column Name", "Data Type", "Constraints", "Description"]
    rows_sc = [
        ["id", "UUID / SERIAL", "PK, NOT NULL", "Unique scan comparison record identifier"],
        ["baseline_scan_id", "UUID / INT", "FK -> scans(id)", "Earlier reference baseline scan identifier"],
        ["current_scan_id", "UUID / INT", "FK -> scans(id)", "Latest target scan identifier being compared"],
        ["new_count", "INTEGER", "DEFAULT 0", "Number of newly introduced findings (regressions)"],
        ["fixed_count", "INTEGER", "DEFAULT 0", "Number of findings resolved since baseline scan"],
        ["recurring_count", "INTEGER", "DEFAULT 0", "Number of persistent unresolved findings"],
        ["compared_at", "TIMESTAMP WITH TZ", "DEFAULT CURRENT_TIMESTAMP", "Timestamp when diff was calculated"]
    ]
    create_styled_table(doc, headers_sc, rows_sc, col_widths=[1.5, 1.5, 1.8, 2.2])

    add_heading_2(doc, "17.2 Database Indexing and Performance Strategy")
    add_paragraph(doc,
        "To maintain sub-50ms query response times even when projects accumulate tens of thousands of findings, specific B-tree indices are deployed:")
    add_bullet(doc, "idx_findings_scan_sev: Composite index on findings(scan_id, severity) to accelerate severity-filtered dashboard views.")
    add_bullet(doc, "idx_findings_scan_file: Composite index on findings(scan_id, file_path) to optimize file-tree browsing.")
    add_bullet(doc, "idx_scans_project_created: Composite index on scans(project_id, created_at DESC) for instantaneous scan history rendering.")
    add_bullet(doc, "idx_scan_files_hash: Index on scan_files(sha256_hash) for rapid content-based duplicate and change detection.")

    add_page_break(doc)

    # =========================================================================
    # SECTION 18: DETAILED MODULE DESCRIPTIONS
    # =========================================================================
    add_heading_1(doc, "18.0 DETAILED MODULE DESCRIPTIONS")
    
    add_paragraph(doc,
        "CodeGuard is architected into 10 decoupled subsystems. Each module is described below detailing its specific purpose, "
        "inputs, internal processing logic, and outputs.")

    modules = [
        {
            "name": "Module 1: Authentication & Authorization Module",
            "purpose": "Manages user identity, account registration, role-based access control, and cryptographic session tokens.",
            "inputs": "User credentials (username, email, password) submitted via JSON payloads.",
            "processing": "Validates password complexity; hashes passwords with bcrypt (cost factor 12); verifies credentials on login; generates signed JWT tokens containing user ID, role, and expiration timestamp (default 8 hours); validates Bearer tokens on protected endpoints.",
            "outputs": "Signed JWT access token, user profile metadata, and HTTP 401 Unauthorized exceptions for invalid tokens."
        },
        {
            "name": "Module 2: Project Management Module",
            "purpose": "Maintains project workspace boundaries, organizing scans, file manifests, and historical audit records.",
            "inputs": "Project metadata (name, description, repo URL) and authenticated user context.",
            "processing": "Enforces user ownership boundaries; performs CRUD operations via SQLAlchemy ORM; cascades deletion of associated scans and findings when a project is removed.",
            "outputs": "Project entities, scan revision summaries, and project-level aggregate security metrics."
        },
        {
            "name": "Module 3: Secure Upload & Archive Extraction Module",
            "purpose": "Ingests Python files and ZIP archives safely, defending the server against upload attack vectors.",
            "inputs": "Multipart/form-data HTTP upload streams and project IDs.",
            "processing": "Verifies MIME type and extension; enforces 25 MB size limits; verifies ZIP magic bytes (PK\\x03\\x04); performs canonical path validation on every archive member to block Zip-Slip traversal; extracts files to an ephemeral sandbox directory (/tmp/codeguard_scan_XXXXXX).",
            "outputs": "Sanitized directory path on the local filesystem containing validated Python source modules."
        },
        {
            "name": "Module 4: Python AST Syntax & Inspection Module",
            "purpose": "Performs zero-dependency syntax validation, dangerous builtin call detection, and complexity assessment.",
            "inputs": "Raw Python source code strings read from extracted filesystem modules.",
            "processing": "Invokes Python standard library ast.parse(); catches SyntaxError exceptions with line/col offsets; subclasses ast.NodeVisitor to detect unsafe builtins (eval, exec, compile, __import__, insecure pickle.loads); computes function complexity score.",
            "outputs": "List of ASTFinding objects containing syntax errors, unsafe calls, and McCabe complexity scores."
        },
        {
            "name": "Module 5: Bandit SAST Engine Adapter",
            "purpose": "Executes static application security testing against Python files using official OpenStack Bandit rule sets.",
            "inputs": "Extracted project directory path and optional bandit configuration file.",
            "processing": "Executes Bandit via safe subprocess parameter lists (without shell=True); runs plugins across B101-B703; parses resulting JSON stream; extracts line numbers, test IDs, severity, and confidence levels.",
            "outputs": "Structured raw Bandit findings dictionary containing test IDs, issue texts, and CWE references."
        },
        {
            "name": "Module 6: Ruff Code Quality Engine Adapter",
            "purpose": "Performs ultra-fast code quality, PEP 8 styling, and anti-pattern analysis powered by Rust.",
            "inputs": "Extracted project directory path.",
            "processing": "Executes the compiled Ruff binary with '--output-format=json'; evaluates PEP 8 violations (E/W), Pyflakes errors (F), flake8-bugbear patterns (B), and McCabe complexity (C901); parses JSON output.",
            "outputs": "Collection of Ruff diagnostic objects containing rule codes, messages, row/col locations, and fix availability."
        },
        {
            "name": "Module 7: Finding Normalization & Severity Mapping Engine",
            "purpose": "Transforms heterogeneous outputs from AST, Bandit, and Ruff into a single canonical data structure.",
            "inputs": "Raw output dictionaries from Modules 4, 5, and 6.",
            "processing": "Maps tool-specific severity and confidence to standardized tiers (Critical, High, Medium, Low); strips ephemeral server directory prefixes to generate clean relative file paths; extracts ±2 lines of surrounding code snippet; links CWE identifiers.",
            "outputs": "Unified list of CanonicalFinding objects ready for database persistence."
        },
        {
            "name": "Module 8: Scan Comparison & Diffing Engine",
            "purpose": "Compares findings between two scans of the same project to track code evolution.",
            "inputs": "Baseline scan ID and target current scan ID.",
            "processing": "Constructs unique finding signature hashes based on (rule_id, file_path, line_number, normalized_message); performs set difference operations: Current \\ Baseline = New Findings (regressions); Baseline \\ Current = Fixed Findings (resolved); Baseline ∩ Current = Recurring Findings.",
            "outputs": "ScanComparisonSummary containing counts and categorized lists of New, Fixed, and Recurring issues."
        },
        {
            "name": "Module 9: Report Generation Module (ReportLab PDF & JSON)",
            "purpose": "Compiles professional, publication-ready audit reports for compliance and archiving.",
            "inputs": "Scan ID, format parameter ('pdf' or 'json'), and database finding records.",
            "processing": "For JSON: serializes normalized findings into structured REST response. For PDF: uses ReportLab SimpleDocTemplate to render corporate cover block, executive metric tables, severity distribution bar charts, and detailed finding breakdown with line numbers and remediation text.",
            "outputs": "Application/pdf binary file stream or application/json payload."
        },
        {
            "name": "Module 10: AI Remediation & Fix Suggestion Module",
            "purpose": "Provides intelligent explanations of detected vulnerabilities and suggests secure code fixes.",
            "inputs": "Finding rule ID, CWE ID, description, and source code context snippet.",
            "processing": "Matches finding against curated secure-coding pattern database; optionally queries external generative AI API with security prompts; generates root-cause analysis and parameterized secure patch code.",
            "outputs": "Remediation response containing plain-language explanation and recommended secure code snippet."
        }
    ]

    for m in modules:
        add_heading_2(doc, m["name"])
        add_paragraph(doc, m["purpose"], bold_prefix="Module Purpose: ")
        add_paragraph(doc, m["inputs"], bold_prefix="Inputs: ")
        add_paragraph(doc, m["processing"], bold_prefix="Processing Logic: ")
        add_paragraph(doc, m["outputs"], bold_prefix="Outputs: ")

    add_page_break(doc)

    # =========================================================================
    # SECTION 19: SYSTEM WORKFLOW AND ALGORITHMS
    # =========================================================================
    add_heading_1(doc, "19.0 SYSTEM WORKFLOW AND ALGORITHMS")
    
    add_paragraph(doc,
        "This section details the algorithmic foundation of the CodeGuard platform. The core algorithms govern safe archive ingestion, "
        "AST syntax inspection, linter execution, canonical normalization, and two-way scan diffing.")

    if os.path.exists("figures/normalization_pipeline.png"):
        add_figure(doc, "figures/normalization_pipeline.png", 
                   "Figure 8: Multi-Engine Finding Normalization and Canonical Schema Transformation Pipeline", 
                   width_inches=6.2)

    add_heading_2(doc, "19.1 Algorithm 1: Safe ZIP Extraction & Zip-Slip Traversal Prevention")
    add_paragraph(doc,
        "Zip-Slip is an arbitrary file overwrite vulnerability occurring when an archive contains path traversal filenames "
        "(e.g., '../../etc/passwd'). Algorithm 1 guarantees that all extracted files remain strictly confined within the intended sandbox root.")
    
    code_algo1 = """Algorithm 1: Safe_Extract_Archive(zip_file_path, target_extract_dir)
Input: zip_file_path (Path to uploaded ZIP), target_extract_dir (Target ephemeral directory)
Output: List of extracted relative Python file paths, or raises SecurityException

1.  resolved_target_dir ← RealPath(target_extract_dir)
2.  extracted_files ← []
3.  Open zip_file_path using ZipFile in read mode as archive:
4.      For each member in archive.infolist():
5.          member_path ← member.filename
6.          # Normalize path and prevent directory traversal
7.          destination_path ← RealPath(Join(resolved_target_dir, member_path))
8.          # Security Check: Ensure destination starts with target directory path
9.          If NOT destination_path.startswith(resolved_target_dir + DirectorySeparator):
10.             Raise SecurityException("Zip-Slip Path Traversal Attack Detected: " + member_path)
11.         If member.is_dir():
12.             CreateDirectory(destination_path)
13.         Else:
14.             EnsureParentDirectoryExists(destination_path)
15.             Extract member to destination_path
16.             If destination_path.endswith(".py"):
17.                 relative_path ← RelPath(destination_path, resolved_target_dir)
18.                 extracted_files.append(relative_path)
19. Return extracted_files"""
    add_code_block(doc, code_algo1, caption="Algorithm 1: Zip-Slip Path Traversal Prevention Pseudocode")

    add_heading_2(doc, "19.2 Algorithm 2: Python AST Dangerous Call & Syntax Analysis")
    add_paragraph(doc,
        "Algorithm 2 operates natively using Python's 'ast' module to detect fatal syntax errors, calculate function complexity, "
        "and flag dangerous builtin functions without executing untrusted code.")
        
    code_algo2 = """Algorithm 2: Analyze_Python_AST(file_path, source_code)
Input: file_path (Path to Python module), source_code (Raw source text)
Output: List of ASTFinding objects

1.  findings ← []
2.  Try:
3.      tree ← ast.parse(source_code, filename=file_path)
4.  Except SyntaxError as se:
5.      findings.append(CreateFinding(
6.          rule_id="AST-SYNTAX-ERROR", severity="HIGH", 
7.          line=se.lineno, col=se.offset, message=str(se.msg)))
8.      Return findings
9.
10. DANGEROUS_CALLS ← {"eval": "CWE-95", "exec": "CWE-95", "compile": "CWE-95"}
11. Class SecurityNodeVisitor(ast.NodeVisitor):
12.     Method visit_Call(node):
13.         If isinstance(node.func, ast.Name) and node.func.id in DANGEROUS_CALLS:
14.             findings.append(CreateFinding(
15.                 rule_id="AST-" + node.func.id.upper(),
16.                 rule_name="Dangerous Builtin Execution: " + node.func.id,
17.                 severity="CRITICAL", cwe_id=DANGEROUS_CALLS[node.func.id],
18.                 line=node.lineno, col=node.col_offset,
19.                 message="Direct invocation of dangerous builtin '" + node.func.id + "()'"))
20.         # Check for insecure pickle deserialization
21.         If isinstance(node.func, ast.Attribute) and node.func.attr in {"loads", "load"}:
22.             If isinstance(node.func.value, ast.Name) and node.func.value.id == "pickle":
23.                 findings.append(CreateFinding(
24.                     rule_id="AST-PICKLE-INSECURE", severity="CRITICAL",
25.                     cwe_id="CWE-502", line=node.lineno, col=node.col_offset,
26.                     message="Unsafe deserialization using pickle." + node.func.attr + "()"))
27.         Self.generic_visit(node)
28.
29. visitor ← SecurityNodeVisitor()
30. visitor.visit(tree)
31. Return findings"""
    add_code_block(doc, code_algo2, caption="Algorithm 2: Python AST Visitor & Syntax Analysis Pseudocode")

    add_heading_2(doc, "19.3 Algorithm 3: Severity Mapping and Canonical Normalization")
    add_paragraph(doc,
        "Disparate tools express severity differently: Bandit uses High/Medium/Low with Confidence tiers; Ruff uses error/warning codes; "
        "AST emits syntax and call flags. Algorithm 3 normalizes them into a unified four-tier hierarchy: Critical, High, Medium, and Low.")
        
    code_algo3 = """Algorithm 3: Map_Severity_And_Normalize(raw_issue, tool_source)
Input: raw_issue (Raw finding dictionary), tool_source (BANDIT | RUFF | AST)
Output: CanonicalFinding object

1.  If tool_source == "AST":
2.      If raw_issue.rule_id in {"AST-EVAL", "AST-EXEC", "AST-PICKLE-INSECURE"}:
3.          severity ← "CRITICAL"
4.      Else If raw_issue.rule_id == "AST-SYNTAX-ERROR":
5.          severity ← "HIGH"
6.      Else:
7.          severity ← "MEDIUM"
8.  Else If tool_source == "BANDIT":
9.      b_sev ← raw_issue["issue_severity"].upper()
10.     b_conf ← raw_issue["issue_confidence"].upper()
11.     # Strict Severity Matrix
12.     If b_sev == "HIGH" and b_conf in {"HIGH", "MEDIUM"}:
13.         severity ← "CRITICAL"   # e.g., Confirmed SQLi or Shell Injection
14.     Else If b_sev == "HIGH" or (b_sev == "MEDIUM" and b_conf == "HIGH"):
15.         severity ← "HIGH"       # e.g., Hardcoded password, weak crypto
16.     Else If b_sev == "MEDIUM":
17.         severity ← "MEDIUM"     # e.g., Insecure MD5/SHA1 usage
18.     Else:
19.         severity ← "LOW"        # e.g., Try-Except-Pass blocks
20. Else If tool_source == "RUFF":
21.     code ← raw_issue["code"].upper()
22.     If code.startswith("E9") or code.startswith("F8"): # Runtime syntax / undefined names
23.         severity ← "HIGH"
24.     Else If code.startswith("B") or code == "C901":    # Bugbear smells or McCabe complexity > 10
25.         severity ← "MEDIUM"
26.     Else:                                              # Style / unused import warnings
27.         severity ← "LOW"
28.
29. snippet ← Extract_Context_Lines(raw_issue.file_path, raw_issue.line_number, radius=2)
30. Return CanonicalFinding(
31.     tool_source=tool_source, rule_id=raw_issue.rule_id, severity=severity,
32.     file_path=Sanitize_Path(raw_issue.file_path), line_number=raw_issue.line_number,
33.     description=raw_issue.message, code_snippet=snippet, status="OPEN")"""
    add_code_block(doc, code_algo3, caption="Algorithm 3: Severity Normalization Logic Pseudocode")

    add_heading_2(doc, "19.4 Algorithm 4: Two-Way Scan Diffing (Fixed, New, Recurring)")
    add_paragraph(doc,
        "Algorithm 4 tracks code evolution across scan revisions, categorizing issues into New (regressions), "
        "Fixed (resolved vulnerabilities), and Recurring (persistent technical debt).")
        
    code_algo4 = """Algorithm 4: Compute_Scan_Diff(baseline_scan_id, current_scan_id)
Input: baseline_scan_id (Previous Scan ID), current_scan_id (Latest Scan ID)
Output: ScanDiffResult(new_findings, fixed_findings, recurring_findings)

1.  baseline_list ← DB.Query(Finding).Filter(scan_id == baseline_scan_id).All()
2.  current_list ← DB.Query(Finding).Filter(scan_id == current_scan_id).All()
3.
4.  Function Generate_Finding_Key(finding):
5.      # Stable semantic identity: Tool + Rule + File + Normalized Line
6.      Return Hash(finding.tool_source + ":" + finding.rule_id + ":" + 
7.                  finding.file_path + ":" + Str(finding.line_number))
8.
9.  baseline_map ← { Generate_Finding_Key(f): f for f in baseline_list }
10. current_map ← { Generate_Finding_Key(f): f for f in current_list }
11.
12. baseline_keys ← Set(baseline_map.keys())
13. current_keys ← Set(current_map.keys())
14.
15. new_keys ← current_keys - baseline_keys          # Present in current, absent in baseline
16. fixed_keys ← baseline_keys - current_keys        # Present in baseline, absent in current
17. recurring_keys ← current_keys ∩ baseline_keys     # Present in both scans
18.
19. new_findings ← [ current_map[k] for k in new_keys ]
20. fixed_findings ← [ baseline_map[k] for k in fixed_keys ]
21. recurring_findings ← [ current_map[k] for k in recurring_keys ]
22.
23. Return ScanDiffResult(new=new_findings, fixed=fixed_findings, recurring=recurring_findings)"""
    add_code_block(doc, code_algo4, caption="Algorithm 4: Two-Way Scan Diffing Pseudocode")

    add_page_break(doc)

    # =========================================================================
    # SECTION 20: BACKEND AND FRONTEND IMPLEMENTATION
    # =========================================================================
    add_heading_1(doc, "20.0 BACKEND AND FRONTEND IMPLEMENTATION")
    
    add_paragraph(doc,
        "This section documents the practical implementation of CodeGuard, detailing the file directory hierarchy, "
        "core Python backend service implementations, and the React frontend component architecture.")

    add_heading_2(doc, "20.1 Codebase Directory Structure")
    code_tree = """codeguard-platform/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── endpoints/
│   │   │   │   │   ├── auth.py          # User registration, login, JWT issuance
│   │   │   │   │   ├── projects.py      # Project workspace CRUD
│   │   │   │   │   ├── scans.py         # Code upload, scan triggering, diff endpoints
│   │   │   │   │   └── reports.py       # ReportLab PDF & JSON generation
│   │   │   │   └── router.py            # API V1 router aggregation
│   │   ├── core/
│   │   │   ├── config.py                # Environment settings via Pydantic
│   │   │   └── security.py              # JWT encoding/decoding, bcrypt password hashing
│   │   ├── db/
│   │   │   ├── base.py                  # Declarative base & metadata
│   │   │   └── session.py               # SQLAlchemy async engine & sessionmaker
│   │   ├── models/                      # SQLAlchemy ORM database models
│   │   │   ├── user.py                  # User credentials and roles
│   │   │   ├── project.py               # Projects workspace model
│   │   │   ├── scan.py                  # Scan execution and file manifest
│   │   │   └── finding.py               # Normalized finding model
│   │   ├── schemas/                     # Pydantic DTO request/response schemas
│   │   │   ├── user_schema.py
│   │   │   ├── project_schema.py
│   │   │   └── scan_schema.py
│   │   └── services/                    # Core business logic & static analysis
│   │       ├── archive_service.py       # Safe ZIP validation & Zip-Slip protection
│   │       ├── ast_analyzer.py          # Python AST Visitor for dangerous calls
│   │       ├── bandit_scanner.py        # Bandit SAST runner & parser
│   │       ├── ruff_scanner.py          # Ruff linter adapter & JSON parser
│   │       ├── normalizer.py            # Finding canonicalization & severity mapper
│   │       ├── diff_service.py          # Scan revision diffing engine
│   │       └── report_generator.py      # ReportLab PDF document compiler
│   ├── tests/                           # Pytest automated test suites
│   ├── Dockerfile                       # Multi-stage Python 3.11 backend image
│   └── requirements.txt                 # Pinned dependencies
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.tsx               # Top navigation bar
│   │   │   ├── Sidebar.tsx              # Project & navigation sidebar
│   │   │   ├── SeverityBadge.tsx        # Styled Critical/High/Med/Low badges
│   │   │   ├── CodeViewer.tsx           # Monaco code highlighter with line markers
│   │   │   ├── ScanDiffMatrix.tsx       # Revision diff comparison table
│   │   │   └── UploadModal.tsx          # Drag-and-drop archive upload modal
│   │   ├── pages/
│   │   │   ├── Dashboard.tsx            # Central overview metrics & recent scans
│   │   │   ├── ProjectView.tsx          # Project details and scan history
│   │   │   └── ScanDetail.tsx           # In-depth findings explorer & code inspection
│   │   ├── services/
│   │   │   └── api.ts                   # Axios REST client with JWT interceptors
│   │   ├── App.tsx                      # React Router configuration
│   │   └── index.css                    # Tailwind CSS configuration
│   ├── Dockerfile                       # Node build + Nginx Alpine runtime
│   └── package.json
└── docker-compose.yml                   # Multi-container orchestration"""
    add_code_block(doc, code_tree, caption="Listing 20.1: CodeGuard Project Directory Organization")

    add_heading_2(doc, "20.2 Key Backend Python Implementations")
    
    # 1. AST Analyzer Implementation
    add_heading_3(doc, "20.2.1 Python AST Visitor Implementation (ast_analyzer.py)")
    code_ast_py = """# backend/app/services/ast_analyzer.py
import ast
from typing import List, Dict, Any

class SecurityASTVisitor(ast.NodeVisitor):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.findings: List[Dict[str, Any]] = []

    def visit_Call(self, node: ast.Call):
        # 1. Detect direct eval() and exec()
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
            if func_name in {"eval", "exec"}:
                self.findings.append({
                    "rule_id": f"AST-{func_name.upper()}",
                    "rule_name": f"Dangerous Builtin Call: {func_name}()",
                    "tool_source": "AST",
                    "severity": "CRITICAL",
                    "cwe_id": "CWE-95",
                    "line_number": node.lineno,
                    "column_number": node.col_offset,
                    "description": f"Direct invocation of dangerous builtin '{func_name}()' allowing arbitrary code execution."
                })
        # 2. Detect insecure pickle.loads() / pickle.load()
        elif isinstance(node.func, ast.Attribute):
            if node.func.attr in {"loads", "load"}:
                if isinstance(node.func.value, ast.Name) and node.func.value.id == "pickle":
                    self.findings.append({
                        "rule_id": "AST-PICKLE-INSECURE",
                        "rule_name": "Insecure Deserialization via pickle",
                        "tool_source": "AST",
                        "severity": "CRITICAL",
                        "cwe_id": "CWE-502",
                        "line_number": node.lineno,
                        "column_number": node.col_offset,
                        "description": "Unsafe deserialization detected using pickle, vulnerable to arbitrary code execution."
                    })
        self.generic_visit(node)

def analyze_ast(file_path: str, source_text: str) -> List[Dict[str, Any]]:
    try:
        tree = ast.parse(source_text, filename=file_path)
    except SyntaxError as se:
        return [{
            "rule_id": "AST-SYNTAX-ERROR",
            "rule_name": "Syntax Error",
            "tool_source": "AST",
            "severity": "HIGH",
            "cwe_id": "CWE-398",
            "line_number": se.lineno or 1,
            "column_number": se.offset or 0,
            "description": f"Fatal Python Syntax Error: {se.msg}"
        }]
    visitor = SecurityASTVisitor(file_path)
    visitor.visit(tree)
    return visitor.findings"""
    add_code_block(doc, code_ast_py, caption="Listing 20.2: Python AST Syntax & Security Analyzer")

    # 2. Archive Service
    add_heading_3(doc, "20.2.2 Safe Archive Extraction Service (archive_service.py)")
    code_archive_py = """# backend/app/services/archive_service.py
import os
import zipfile
import tempfile
from fastapi import HTTPException, status

def safe_extract_zip(zip_bytes: bytes, target_dir: str) -> list[str]:
    # Write uploaded archive to temporary zip file
    temp_zip_path = os.path.join(target_dir, "upload.zip")
    with open(temp_zip_path, "wb") as f:
        f.write(zip_bytes)

    if not zipfile.is_zipfile(temp_zip_path):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Uploaded file is not a valid ZIP archive."
        )

    extracted_files = []
    real_target_dir = os.path.realpath(target_dir)

    with zipfile.ZipFile(temp_zip_path, "r") as archive:
        for member in archive.infolist():
            member_path = member.filename
            # Resolve full target path
            dest_path = os.path.realpath(os.path.join(real_target_dir, member_path))
            
            # Defense against Zip-Slip path traversal vulnerability
            if not dest_path.startswith(real_target_dir + os.sep):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Security Alert: Zip-Slip path traversal attempt detected in '{member_path}'."
                )

            if member.is_dir():
                os.makedirs(dest_path, exist_ok=True)
            else:
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                with archive.open(member) as src, open(dest_path, "wb") as dst:
                    dst.write(src.read())

                if dest_path.endswith(".py"):
                    rel_path = os.path.relpath(dest_path, real_target_dir)
                    extracted_files.append(rel_path)

    os.remove(temp_zip_path) # Clean up archive file
    return extracted_files"""
    add_code_block(doc, code_archive_py, caption="Listing 20.3: Safe ZIP Extraction Service with Zip-Slip Defense")

    # 3. FastAPI Upload & Scan Router
    add_heading_3(doc, "20.2.3 FastAPI Scan Controller Endpoint (scans.py)")
    code_scan_py = """# backend/app/api/v1/endpoints/scans.py
import tempfile
import time
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.archive_service import safe_extract_zip
from app.services.bandit_scanner import run_bandit
from app.services.ruff_scanner import run_ruff
from app.services.ast_analyzer import analyze_ast
from app.services.normalizer import normalize_all_findings
from app.models.scan import Scan
from app.models.finding import Finding

router = APIRouter()

@router.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload_and_scan(
    project_id: int = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    start_time = time.time()
    contents = await file.read()
    if len(contents) > 25 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File exceeds maximum allowed size of 25MB.")

    with tempfile.TemporaryDirectory(prefix="codeguard_") as temp_dir:
        # Safe extraction
        py_files = safe_extract_zip(contents, temp_dir)
        if not py_files:
            raise HTTPException(status_code=400, detail="Archive contains no valid Python (.py) files.")

        # Multi-engine execution
        ast_findings = []
        for pf in py_files:
            full_p = os.path.join(temp_dir, pf)
            with open(full_p, "r", encoding="utf-8", errors="ignore") as f:
                ast_findings.extend(analyze_ast(pf, f.read()))

        bandit_findings = run_bandit(temp_dir)
        ruff_findings = run_ruff(temp_dir)

        # Normalization & Persistence
        normalized = normalize_all_findings(temp_dir, ast_findings, bandit_findings, ruff_findings)
        
        scan_record = Scan(
            project_id=project_id,
            status="COMPLETED",
            total_files=len(py_files),
            total_findings=len(normalized),
            duration_seconds=round(time.time() - start_time, 2)
        )
        db.add(scan_record)
        db.flush()

        for item in normalized:
            db.add(Finding(scan_id=scan_record.id, **item))
        db.commit()

    return {"scan_id": scan_record.id, "total_findings": len(normalized), "duration": scan_record.duration_seconds}"""
    add_code_block(doc, code_scan_py, caption="Listing 20.4: FastAPI Asynchronous Scan Orchestration Endpoint")

    add_page_break(doc)

    # =========================================================================
    # SECTION 21: REST API DOCUMENTATION
    # =========================================================================
    add_heading_1(doc, "21.0 REST API DOCUMENTATION")
    
    add_paragraph(doc,
        "CodeGuard exposes a modern, fully documented RESTful API conforming to the OpenAPI 3.0 specification. "
        "All endpoints return JSON responses and employ standard HTTP status codes (200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found).")

    add_heading_2(doc, "21.1 Core API Endpoint Directory")
    headers_api = ["HTTP Method", "Endpoint Route", "Auth Required", "Description"]
    rows_api = [
        ["POST", "/api/v1/auth/register", "No (Public)", "Register a new user account with username, email, password"],
        ["POST", "/api/v1/auth/login", "No (Public)", "Authenticate credentials and issue JWT bearer access token"],
        ["GET", "/api/v1/projects", "Yes (Bearer)", "Retrieve list of projects owned by authenticated user"],
        ["POST", "/api/v1/projects", "Yes (Bearer)", "Create a new project workspace container"],
        ["POST", "/api/v1/scans/upload", "Yes (Bearer)", "Upload source code/ZIP archive and trigger analysis"],
        ["GET", "/api/v1/scans/{id}", "Yes (Bearer)", "Fetch metadata, execution duration, and metric tallies for a scan"],
        ["GET", "/api/v1/scans/{id}/findings", "Yes (Bearer)", "Retrieve paginated list of normalized findings with filters"],
        ["PATCH", "/api/v1/findings/{id}/status", "Yes (Bearer)", "Update resolution status (OPEN, RESOLVED, FALSE_POSITIVE)"],
        ["GET", "/api/v1/scans/{id}/diff/{prev_id}", "Yes (Bearer)", "Compute New, Fixed, and Recurring issues between scans"],
        ["GET", "/api/v1/scans/{id}/report", "Yes (Bearer)", "Download audit report as vector PDF or raw JSON file"]
    ]
    create_styled_table(doc, headers_api, rows_api, col_widths=[1.2, 2.3, 1.2, 1.8])

    add_heading_2(doc, "21.2 Sample Request and Response Payloads")
    
    add_heading_3(doc, "Endpoint: POST /api/v1/scans/upload")
    add_paragraph(doc, "Headers: Authorization: Bearer <JWT_TOKEN>, Content-Type: multipart/form-data")
    add_paragraph(doc, "Request Form-Data: project_id=1, file=@vuln_api.zip")
    
    code_res1 = """// Response: HTTP 201 Created
{
  "scan_id": 4,
  "project_id": 1,
  "status": "COMPLETED",
  "total_files": 14,
  "total_findings": 7,
  "metrics": {
    "critical": 2,
    "high": 2,
    "medium": 2,
    "low": 1
  },
  "duration_seconds": 1.42,
  "created_at": "2026-11-02T14:22:10.450Z"
}"""
    add_code_block(doc, code_res1, caption="Sample JSON Response: Scan Upload & Initiation")

    add_heading_3(doc, "Endpoint: GET /api/v1/scans/4/findings?severity=CRITICAL")
    code_res2 = """// Response: HTTP 200 OK
{
  "scan_id": 4,
  "total_results": 2,
  "findings": [
    {
      "id": 101,
      "tool_source": "BANDIT",
      "rule_id": "B608",
      "rule_name": "Hardcoded SQL Expression / SQL Injection",
      "severity": "CRITICAL",
      "cwe_id": "CWE-89",
      "file_path": "app/auth/routes.py",
      "line_number": 84,
      "column_number": 12,
      "description": "Possible SQL injection vector through string formatting in cursor.execute.",
      "code_snippet": "83:   # Dynamic query\\n84:   query = f\"SELECT * FROM users WHERE u='{username}'\"\\n85:   cursor.execute(query)",
      "status": "OPEN",
      "ai_explanation": "Direct f-string concatenation in raw SQL statements allows an attacker to inject arbitrary SQL statements, completely bypassing login. Remediate by using parameterized bind variables."
    },
    {
      "id": 102,
      "tool_source": "AST",
      "rule_id": "AST-EVAL",
      "rule_name": "Dangerous Builtin Call: eval()",
      "severity": "CRITICAL",
      "cwe_id": "CWE-95",
      "file_path": "utils/calc.py",
      "line_number": 23,
      "column_number": 8,
      "description": "Direct invocation of dangerous builtin 'eval()' allowing arbitrary code execution.",
      "code_snippet": "22:   def compute(user_input):\\n23:       return eval(user_input)",
      "status": "OPEN",
      "ai_explanation": "Passing untrusted user input directly to eval() enables remote code execution. Replace eval() with ast.literal_eval() or dedicated mathematical parsers."
    }
  ]
}"""
    add_code_block(doc, code_res2, caption="Sample JSON Response: Filtered Findings Query")

    return doc
