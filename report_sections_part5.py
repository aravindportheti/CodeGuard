from docx.shared import Pt
from report_styles import (
    add_heading_1, add_heading_2, add_heading_3, add_paragraph,
    add_bullet, add_callout, add_code_block, add_page_break, create_styled_table
)

def build_part5(doc):
    # =========================================================================
    # SECTION 27: LIMITATIONS
    # =========================================================================
    add_heading_1(doc, "27.0 LIMITATIONS")
    
    add_paragraph(doc,
        "While CodeGuard delivers a robust, high-performance static assessment platform, every software engineering system operates "
        "under specific technical and theoretical constraints. The identified limitations include:")
        
    add_bullet(doc, "Dynamic Typing & Runtime Blindness: As a static analysis tool, CodeGuard inspects source code without executing it. It cannot resolve dynamic runtime behavior, such as runtime monkey-patching, dynamic attribute access via getattr(), or values supplied exclusively through runtime environment variables.")
    add_bullet(doc, "Inter-Procedural Data Flow Tracking: While Bandit performs localized taint analysis on function calls, deep inter-procedural taint propagation across complex multi-tier service boundaries is constrained compared to heavyweight commercial compilers.")
    add_bullet(doc, "Monolithic Archive File Limits: To protect against resource exhaustion and denial-of-service decompression attacks, project archives are currently capped at 25 MB. Extremely large monolithic repositories exceeding this limit must be scanned in modular packages.")
    add_bullet(doc, "Third-Party Generative AI Latency: When the optional AI remediation feature is enabled, response generation times depend on external LLM API availability and network round-trip latency, introducing brief delays in remediation rendering.")

    add_page_break(doc)

    # =========================================================================
    # SECTION 28: FUTURE ENHANCEMENTS
    # =========================================================================
    add_heading_1(doc, "28.0 FUTURE ENHANCEMENTS")
    
    add_paragraph(doc,
        "The modular architecture of CodeGuard provides a solid foundation for continuous evolution. "
        "The following strategic enhancements are planned for future versions:")
        
    add_bullet(doc, "CI/CD Pipeline Integrations: Developing official GitHub Actions, GitLab CI runners, and pre-commit hooks to automatically trigger CodeGuard scans upon pull request creation and block merges on Critical vulnerabilities.")
    add_bullet(doc, "Software Composition Analysis (SCA): Integrating open-source dependency vulnerability checkers (e.g., pip-audit / Safety) to inspect requirements.txt and pyproject.toml files for known Common Vulnerabilities and Exposures (CVEs) in third-party libraries.")
    add_bullet(doc, "IDE Extensions: Building lightweight extensions for Visual Studio Code and PyCharm to provide real-time CodeGuard diagnostics and one-click AI remediations directly inside the developer's code editor.")
    add_bullet(doc, "Polyglot Language Expansion: Extending the AST parser and normalization pipeline to ingest and analyze JavaScript, TypeScript, and Go codebases.")
    add_bullet(doc, "Local LLM Fine-Tuning: Deploying quantized, locally hosted open-source security LLMs (e.g., StarCoder or DeepSeek-Coder) within the Docker network to eliminate external API dependency and protect proprietary source code.")

    add_page_break(doc)

    # =========================================================================
    # SECTION 29: CONCLUSION
    # =========================================================================
    add_heading_1(doc, "29.0 CONCLUSION")
    
    add_paragraph(doc,
        "The CodeGuard internship project successfully conceptualized, designed, implemented, and validated an intelligent, "
        "full-stack source code quality assessment and security vulnerability detection platform tailored for the modern Python ecosystem. "
        "By synthesizing native Python Abstract Syntax Tree (AST) inspection, Bandit SAST security rule sets, and Ruff's high-speed Rust-powered linting, "
        "CodeGuard demonstrates that comprehensive code auditing does not require sacrificing developer velocity or investing in prohibitive enterprise licenses.")
        
    add_paragraph(doc,
        "The engineering accomplishments delivered during this internship include:")
    add_bullet(doc, "Full-Stack System Architecture: Engineered an asynchronous FastAPI backend paired with a modern React 18 / TypeScript SPA, fully containerized via Docker Compose.")
    add_bullet(doc, "Multi-Engine Triangulation: Harmonized heterogeneous static analyzers into a unified canonical JSON schema with standardized severity mapping.")
    add_bullet(doc, "Security Hardening: Implemented bulletproof file ingestion featuring Zip-Slip path-traversal prevention, file signature validation, and ephemeral sandbox isolation.")
    add_bullet(doc, "Historical Scan Diffing: Developed an algorithmic comparison engine that tracks New regressions, Fixed issues, and Recurring technical debt across code revisions.")
    add_bullet(doc, "Automated Publication Reporting: Integrated ReportLab for on-demand vector PDF audit generation and structured JSON exports.")
    
    add_paragraph(doc,
        "Ultimately, CodeGuard exemplifies the DevSecOps 'Shift-Left' philosophy, empowering software development teams to catch critical vulnerabilities "
        "and architectural defects early in the software development lifecycle, thereby fortifying software supply chains and reducing downstream remediation costs.")

    add_page_break(doc)

    # =========================================================================
    # SECTION 30: REFERENCES
    # =========================================================================
    add_heading_1(doc, "30.0 REFERENCES")
    
    references = [
        "[1] OpenStack Security Group. 'Bandit: A Python Source Code Security Linter.' Official Documentation, OpenStack Foundation, 2024. Available: https://bandit.readthedocs.io/",
        "[2] Astral Software Inc. 'Ruff: An Extremely Fast Python Linter and Code Formatter Written in Rust.' 2024. Available: https://docs.astral.sh/ruff/",
        "[3] Python Software Foundation. 'ast — Abstract Syntax Trees.' Python 3.12 Standard Library Documentation, 2024. Available: https://docs.python.org/3/library/ast.html",
        "[4] OWASP Foundation. 'OWASP Top 10: The Ten Most Critical Web Application Security Risks.' Open Web Application Security Project, 2021. Available: https://owasp.org/Top10/",
        "[5] MITRE Corporation. 'Common Weakness Enumeration (CWE) Specification.' National Cybersecurity FFRDC, 2024. Available: https://cwe.mitre.org/",
        "[6] S. Ramírez (tiangolo). 'FastAPI: High Performance Modern Web Framework for Python.' FastAPI Documentation, 2024. Available: https://fastapi.tiangolo.com/",
        "[7] M. Bayer. 'SQLAlchemy: The Database Toolkit for Python.' SQLAlchemy 2.0 Documentation, 2024. Available: https://www.sqlalchemy.org/",
        "[8] ReportLab Europe Ltd. 'ReportLab PDF Generation User Guide.' Version 4.1, 2024. Available: https://www.reportlab.com/docs/reportlab-userguide.pdf",
        "[9] D. Crockford. 'The application/json Media Type for JavaScript Object Notation (JSON).' RFC 8259, Internet Engineering Task Force (IETF), 2017.",
        "[10] Snyk Security Research Team. 'Zip Slip Vulnerability: Exploitation and Remediation in Java, Python, and Go.' Snyk Research Labs, 2018.",
        "[11] National Institute of Standards and Technology. 'Security and Privacy Controls for Information Systems and Organizations.' NIST Special Publication 800-53, Rev. 5, 2020.",
        "[12] D. Spinellis. 'Code Quality: The Open Source Perspective.' Addison-Wesley Professional, Boston, MA, 2006.",
        "[13] T. McCabe. 'A Complexity Measure.' IEEE Transactions on Software Engineering, vol. SE-2, no. 4, pp. 308-320, Dec. 1976.",
        "[14] Docker Inc. 'Docker Engine and Docker Compose Specifications.' Docker Documentation, 2024. Available: https://docs.docker.com/",
        "[15] V. Van Rossum and F. L. Drake. 'The Python Language Reference Manual.' Python Software Foundation, 2023."
    ]
    for ref in references:
        add_paragraph(doc, ref)

    add_page_break(doc)

    # =========================================================================
    # SECTION 31: APPENDICES
    # =========================================================================
    add_heading_1(doc, "31.0 APPENDICES")
    
    add_heading_2(doc, "Appendix A: Docker Compose & Deployment Configuration")
    code_compose = """# docker-compose.yml
version: '3.8'

services:
  db:
    image: postgres:16-alpine
    container_name: codeguard-db
    environment:
      POSTGRES_USER: codeguard_user
      POSTGRES_PASSWORD: secure_db_password_2026
      POSTGRES_DB: codeguard_db
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - codeguard-net
    restart: unless-stopped

  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: codeguard-backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://codeguard_user:secure_db_password_2026@db:5432/codeguard_db
      - SECRET_KEY=super_secure_cryptographic_jwt_key_2026
      - ALGORITHM=HS256
    depends_on:
      - db
    networks:
      - codeguard-net
    restart: unless-stopped

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: codeguard-frontend
    ports:
      - "80:80"
    depends_on:
      - backend
    networks:
      - codeguard-net
    restart: unless-stopped

networks:
  codeguard-net:
    driver: bridge

volumes:
  postgres_data:
    driver: local"""
    add_code_block(doc, code_compose, caption="Listing A.1: Complete docker-compose.yml Configuration")

    add_heading_2(doc, "Appendix B: Ruff Static Analysis Configuration (ruff.toml)")
    code_ruff_toml = """# backend/ruff.toml - CodeGuard Static Quality Configuration
target-version = "py311"
line-length = 100

[lint]
select = [
    "E",    # pycodestyle errors
    "W",    # pycodestyle warnings
    "F",    # Pyflakes
    "B",    # flake8-bugbear (common bug patterns)
    "C90",  # McCabe cyclomatic complexity
    "I",    # isort (import order)
    "S",    # flake8-bandit (security checks)
    "UP"    # pyupgrade (modern syntax)
]
ignore = ["E501"] # Handled via line-length

[lint.mccabe]
max-complexity = 10 # Flag functions exceeding McCabe score 10"""
    add_code_block(doc, code_ruff_toml, caption="Listing B.1: Pinned ruff.toml Configuration")

    add_page_break(doc)

    # =========================================================================
    # SECTION 32: TECHNICAL VIVA QUESTIONS AND ANSWERS
    # =========================================================================
    add_heading_1(doc, "32.0 TECHNICAL VIVA QUESTIONS AND ANSWERS")
    
    add_paragraph(doc,
        "This section compiles 25 comprehensive, in-depth technical viva questions and model answers "
        "designed for college academic evaluation and defense of the CodeGuard capstone project.")

    viva_qa = [
        # Category 1: Python Core & AST
        ("Q1: What is an Abstract Syntax Tree (AST), and why is AST parsing preferred over Regular Expressions for code analysis?",
         "An Abstract Syntax Tree (AST) is a hierarchical, tree-based representation of the abstract syntactic structure of source code. "
         "Each node in the tree denotes a structural construct in the syntax (e.g., FunctionDef, Call, Assign, BinOp). "
         "AST parsing is vastly superior to regular expressions (Regex) because source code is context-free and non-linear. Regex cannot reliably parse "
         "nested function calls, string escaping, multi-line statements, scope inheritance, or comments. AST parsing guarantees zero false-positive token mismatches "
         "and allows deterministic inspection of the code's exact syntactic meaning as understood by the Python compiler."),
         
        ("Q2: How does Python's standard library 'ast.NodeVisitor' operate in CodeGuard?",
         "The 'ast.NodeVisitor' class uses the Visitor design pattern to walk an AST. When visitor.visit(node) is called, it searches for a method named "
         "'visit_' + node.__class__.__name__ (such as visit_Call or visit_FunctionDef). If found, it executes custom inspection logic; otherwise, it calls "
         "generic_visit(node) to traverse child nodes. In CodeGuard, we subclass NodeVisitor to inspect every Call node, checking whether the invoked function "
         "is an unsafe builtin like eval(), exec(), or insecure pickle.loads()."),

        ("Q3: What is the difference between eval() and ast.literal_eval()?",
         "eval() dynamically executes arbitrary Python code strings with full access to global and local execution scopes, allowing an attacker to run malicious system commands (e.g., __import__('os').system('rm -rf /')). "
         "In contrast, ast.literal_eval() safely parses and evaluates strings containing only Python literals (strings, numbers, tuples, lists, dicts, booleans, and None). "
         "It raises a ValueError if the string attempts to call functions, invoke operators, or instantiate classes, making it immune to code injection."),

        ("Q4: How does CodeGuard calculate McCabe Cyclomatic Complexity?",
         "Cyclomatic complexity measures the number of linearly independent paths through a program's source code, formulated by Thomas McCabe as M = E - N + 2P "
         "(where E = edges, N = nodes, P = connected components). In CodeGuard, Ruff's C901 engine traverses decision points (if, elif, for, while, except, and/or expressions). "
         "Functions with a complexity score exceeding 10 are flagged with Medium severity as architectural code smells requiring modular refactoring."),

        # Category 2: SAST & Bandit
        ("Q5: What is Static Application Security Testing (SAST), and how does Bandit implement it?",
         "SAST is a white-box security auditing methodology that examines non-running source code to detect known vulnerabilities and coding standard violations. "
         "Bandit is a dedicated Python SAST engine developed by the OpenStack Security Group. Bandit reads Python source code, converts it into an AST, "
         "and executes a suite of security test plugins (B101 through B703). Each test targets specific AST node types (e.g., Call nodes for subprocess or SQL statements) "
         "and emits structured findings accompanied by severity (High/Med/Low) and confidence ratings."),

        ("Q6: How does Bandit detect SQL Injection (Rule B608)?",
         "Bandit's B608 plugin inspects database cursor execution calls (e.g., execute, executemany) where the SQL statement is formed using string concatenation "
         "(+ operator), % formatting, str.format(), or Python 3.6+ f-strings. When it detects dynamic variables interpolated directly into SQL syntax rather than "
         "using parameterized bind arguments, it flags a High-severity CWE-89 SQL Injection issue."),

        ("Q7: Why does Bandit emit both Severity and Confidence, and how does CodeGuard use them?",
         "Severity indicates the catastrophic potential of an issue if successfully exploited (e.g., SQL injection has High severity, while an insecure temporary file has Low severity). "
         "Confidence reflects the algorithmic certainty that the code pattern is an actual vulnerability rather than a false positive. "
         "CodeGuard uses both in its Normalization Engine: a Bandit finding is classified as CRITICAL only when Severity is HIGH and Confidence is HIGH/MEDIUM."),

        # Category 3: Ruff & Rust
        ("Q8: Why is Ruff dramatically faster than traditional Python linters like Flake8 or Pylint?",
         "Ruff is implemented from scratch in Rust, a compiled systems programming language with zero-cost abstractions, manual memory management without garbage collection pauses, "
         "and aggressive multi-threaded parallel execution via the Rayon library. Traditional linters like Flake8 launch separate Python processes and re-parse files multiple times sequentially. "
         "Ruff parses the codebase once into an internal Rust AST and applies hundreds of lint rules concurrently, achieving 10x to 100x speedups."),

        # Category 4: Web Security & Uploads
        ("Q9: What is the Zip-Slip vulnerability, and how does CodeGuard prevent it?",
         "Zip-Slip is an arbitrary file overwrite vulnerability that occurs when a malicious archive contains filenames with directory traversal sequences (e.g., '../../../../var/www/shell.py'). "
         "When an unhardened extractor extracts the file, it writes the file outside the intended target directory, potentially overwriting system files. "
         "CodeGuard prevents Zip-Slip by resolving every member's target path using os.path.realpath() and verifying that destination_path.startswith(target_dir + os.sep). "
         "If the extracted path breaks out of the sandbox root, extraction immediately aborts with an HTTP 400 Security Alert."),

        ("Q10: What is a Decompression Bomb (ZIP Bomb), and what are CodeGuard's defenses?",
         "A Decompression Bomb is a tiny, highly compressed archive (e.g., a few kilobytes) that expands into gigabytes or terabytes of uncompressed data, "
         "exhausting server memory and disk storage (Denial of Service). CodeGuard defends against this by enforcing a hard 25 MB upload limit, "
         "verifying file headers, and monitoring uncompressed disk usage during extraction."),

        # Category 5: FastAPI & Architecture
        ("Q11: Why is FastAPI considered an asynchronous web framework, and what is ASGI?",
         "FastAPI is built on Starlette and the Asynchronous Server Gateway Interface (ASGI) specification (the modern asynchronous successor to WSGI). "
         "Using Python's asyncio event loop, FastAPI can handle thousands of concurrent client connections on a single thread. When performing I/O-bound operations "
         "(such as reading uploaded files, querying PostgreSQL, or awaiting subprocesses), the event loop pauses the current coroutine and services other incoming requests, "
         "maximizing server throughput."),

        ("Q12: How does Pydantic v2 enhance FastAPI's request validation?",
         "Pydantic v2 is rewritten in Rust and provides ultra-fast data validation and serialization based on Python standard type hints. "
         "FastAPI uses Pydantic models to automatically parse incoming request JSON or form data. If a field fails validation (e.g., missing project_id or invalid email), "
         "FastAPI automatically generates an RFC 7807 compliant HTTP 422 Unprocessable Entity response without requiring manual conditional checks."),

        # Category 6: Database & SQLAlchemy
        ("Q13: What is the role of Alembic in the CodeGuard database architecture?",
         "Alembic is the database migration tool for SQLAlchemy. It tracks changes made to SQLAlchemy declarative models and generates version-controlled migration scripts "
         "containing 'upgrade()' and 'downgrade()' directives. This enables reproducible schema changes across development, testing, and production Docker environments without manual SQL alter scripts."),

        ("Q14: Explain the finding deduplication and scan comparison algorithm.",
         "CodeGuard generates a deterministic semantic hash for every finding based on (tool_source + rule_id + file_path + line_number). "
         "To compare two scans, CodeGuard retrieves the sets of finding hashes for Scan A (baseline) and Scan B (current). "
         "Using mathematical set operations: B \\ A yields New findings (regressions); A \\ B yields Fixed findings (resolved vulnerabilities); and A ∩ B yields Recurring technical debt."),

        # Category 7: DevOps & Docker
        ("Q15: Why is CodeGuard deployed using multi-stage Docker builds?",
         "Multi-stage Docker builds separate the build environment from the final runtime image. In the frontend, Node.js compiles TypeScript and Tailwind into optimized static assets, "
         "which are copied to a lightweight Nginx Alpine container, discarding Node.js dependencies. In the backend, build compilers are discarded, resulting in minimal image size, "
         "reduced attack surface, and faster container startup times."),

        # Category 8: Project Defense Questions
        ("Q16: How does CodeGuard handle False Positives?",
         "CodeGuard provides a finding resolution lifecycle. In the UI, an authorized auditor can inspect a finding, examine the contextual lines, and click 'Mark as False Positive'. "
         "This updates the finding status in the PostgreSQL database from OPEN to FALSE_POSITIVE, suppressing it from executive PDF audit tallies while retaining the audit trail."),

        ("Q17: What happens if an uploaded Python file contains a syntax error?",
         "Instead of crashing the scanner, the AST Analyzer catches the SyntaxError exception, extracts the exact line and column offset, and creates a normalized HIGH-severity "
         "finding with rule ID 'AST-SYNTAX-ERROR'. The file is marked as 'SYNTAX_ERROR' in the scan manifest, and the analysis of other valid project files continues uninterrupted."),

        ("Q18: What is the purpose of using ReportLab for PDF generation instead of HTML-to-PDF converters?",
         "HTML-to-PDF tools (like WeasyPrint or wkhtmltopdf) require heavy browser engines or WebKit dependencies that inflate Docker container sizes by several hundred megabytes "
         "and are vulnerable to Server-Side Request Forgery (SSRF). ReportLab is a pure Python library that programmatically draws vector shapes, tables, and typography directly to PDF streams "
         "with microsecond speed, pixel-perfect layout control, and zero external browser dependencies."),

        ("Q19: How does CodeGuard protect against shell injection during scanner execution?",
         "When invoking external tools like Bandit or Ruff, CodeGuard passes command arguments as an explicit array of strings to subprocess.run(..., shell=False). "
         "Because shell=False is enforced, the operating system executes the binary directly without passing the command through /bin/sh or cmd.exe, completely nullifying "
         "shell metacharacters (e.g., ';', '&&', '|', '`') that could otherwise trigger arbitrary command execution."),

        ("Q20: What are Common Weakness Enumeration (CWE) identifiers, and why are they included in findings?",
         "CWE is a standardized, industry-wide dictionary of software security weaknesses maintained by the MITRE Corporation (e.g., CWE-89 for SQL Injection, CWE-78 for OS Command Injection). "
         "Mapping findings to CWE IDs allows developers and enterprise auditors to cross-reference issues with national vulnerability databases (NVD) and NIST security frameworks."),

        ("Q21: Can CodeGuard analyze Python 3.12 syntax such as the new f-string syntax and type parameters?",
         "Yes. Because CodeGuard's backend runs on Python 3.11/3.12, Python's native 'ast' module inherently supports modern syntax constructs (including PEP 695 type parameter syntax and PEP 701 f-string nesting), "
         "guaranteeing full parsing compatibility without syntax errors on modern codebases."),

        ("Q22: How is multi-tenancy enforced in CodeGuard's database layer?",
         "Multi-tenancy is enforced through relational foreign-key associations and user context verification. Every project record is linked to a user_id foreign key. "
         "All API endpoints extract the authenticated user's ID from the validated JWT token and query only projects and scans matching that user ID, preventing cross-tenant data leakage."),

        ("Q23: How does CodeGuard ensure that scanned code is not permanently stored or leaked?",
         "CodeGuard treats source code files as ephemeral scan artifacts. Files are unpacked exclusively within a temporary directory created via tempfile.TemporaryDirectory(). "
         "Once the static analysis engines have completed token extraction and findings are stored in the database, the temporary directory is automatically purged from the filesystem "
         "via Python context managers and try...finally blocks."),

        ("Q24: What is the difference between cyclomatic complexity and cognitive complexity?",
         "Cyclomatic complexity (McCabe) measures the mathematical number of execution paths based purely on decision branches (if, for, while). "
         "Cognitive complexity measures how difficult code is for a human to comprehend by penalizing nested structures and breaks in linear reading flow. "
         "CodeGuard currently implements McCabe cyclomatic complexity via Ruff rule C901."),

        ("Q25: What was your personal contribution to this internship project?",
         "As the lead developer on this capstone project, I designed the multi-tier system architecture; implemented the FastAPI REST API gateway and JWT authentication; "
         "developed the Python AST Visitor and safe archive extraction service with Zip-Slip defense; integrated the Bandit and Ruff adapters; created the finding normalization and scan diffing algorithms; "
         "designed the React 18 / Tailwind CSS dashboard; and configured the containerized Docker Compose deployment environment.")
    ]

    for q, a in viva_qa:
        add_paragraph(doc, q, bold_prefix="Q: ")
        add_paragraph(doc, a, bold_prefix="Answer: ")
        # Tiny spacing between questions
        p_sp = doc.add_paragraph()
        p_sp.paragraph_format.space_before = Pt(0)
        p_sp.paragraph_format.space_after = Pt(4)

    return doc
