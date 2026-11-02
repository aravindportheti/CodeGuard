import os
from report_styles import (
    add_heading_1, add_heading_2, add_heading_3, add_paragraph,
    add_bullet, add_callout, add_page_break, add_figure, create_styled_table
)

def build_part2(doc):
    # =========================================================================
    # SECTION 11: OBJECTIVES AND SCOPE
    # =========================================================================
    add_heading_1(doc, "11.0 OBJECTIVES AND SCOPE")
    
    add_heading_2(doc, "11.1 Primary Engineering Objectives")
    add_paragraph(doc,
        "The overarching mission of the CodeGuard project is to democratize high-velocity static code security and quality assessment "
        "for Python developers. The project establishes the following primary objectives:")
    add_bullet(doc, "Multi-Engine Integration: Architect and implement an automated scanning pipeline that seamlessly integrates Python Abstract Syntax Tree (AST) analysis, Bandit SAST rules, and Ruff code quality linting into a unified assessment process.")
    add_bullet(doc, "High-Throughput Asynchronous Backend: Design a robust, non-blocking REST API gateway using FastAPI, SQLAlchemy 2.0, and PostgreSQL capable of processing complex multi-file Python archives in under 2.5 seconds.")
    add_bullet(doc, "Canonical Schema Normalization: Develop an intelligent finding normalization algorithm that transforms disparate diagnostic messages, severities, and line references into a standardized canonical JSON data model.")
    add_bullet(doc, "Historical Scan Diffing Engine: Create an algorithmic comparison module to track code evolution across scan revisions, accurately categorizing findings into New (regressions), Fixed (resolved), and Recurring (unmitigated) issues.")
    add_bullet(doc, "Secure Ingestion & Sandbox Isolation: Enforce strict defense-in-depth security controls on file uploads, including Zip-Slip path-traversal prevention, MIME type verification, file-size gating, and ephemeral sandbox workspace cleanup.")
    add_bullet(doc, "Developer-Centric User Interface: Build an interactive, responsive Single Page Application using React 18, TypeScript, and Tailwind CSS, featuring code highlighting with inline issue markers and filterable metrics dashboards.")
    add_bullet(doc, "Multi-Format Export: Implement automated audit report generation in both publication-grade vector PDF (utilizing ReportLab) and machine-readable JSON format for seamless CI/CD integration.")

    add_heading_2(doc, "11.2 Scope of the Project")
    add_paragraph(doc, "The functional and architectural scope of CodeGuard is explicitly bounded as follows:")
    
    add_paragraph(doc, "1. In-Scope Functional Capabilities:", bold_prefix="In-Scope Capabilities: ")
    add_bullet(doc, "Target Programming Language: Python source code compatible with Python versions 3.8 through 3.12.")
    add_bullet(doc, "File Ingestion: Direct upload of standalone .py files or multi-module .zip project archives up to 25 MB in size.")
    add_bullet(doc, "Vulnerability Coverage: Comprehensive detection of OWASP Top 10 Python vulnerabilities (SQL injection, command execution, hardcoded credentials, insecure hashes, weak pseudo-random generators, shell=True invocations).")
    add_bullet(doc, "Quality Coverage: PEP 8 style validation, code smell identification, cyclomatic complexity (McCabe C901 threshold checking), and unused import detection.")
    add_bullet(doc, "User Authentication: Secure multi-tenant user authentication utilizing JWT (JSON Web Tokens) with PBKDF2/Bcrypt password hashing.")
    add_bullet(doc, "Deployment: Multi-container orchestration using Docker and Docker Compose for production and development environments.")

    add_paragraph(doc, "2. Out-of-Scope Boundaries:", bold_prefix="Out-of-Scope Boundaries: ")
    add_bullet(doc, "Dynamic Application Security Testing (DAST): CodeGuard performs static analysis without runtime execution of untrusted code; fuzzing and live server pen-testing are out of scope.")
    add_bullet(doc, "Polyglot Language Support: CodeGuard is purpose-built and highly optimized specifically for Python codebases; languages such as Java, C#, or PHP are not covered in this release.")
    add_bullet(doc, "Direct Repository Git Sync: Automatic continuous polling of remote GitHub/GitLab webhooks is designated as a post-internship future enhancement.")

    add_page_break(doc)

    # =========================================================================
    # SECTION 12: FEASIBILITY STUDY
    # =========================================================================
    add_heading_1(doc, "12.0 FEASIBILITY STUDY")
    
    add_paragraph(doc,
        "Prior to architectural modeling and system implementation, a comprehensive feasibility study was conducted across four vital dimensions "
        "to ensure the technical viability, operational usability, economic sustainability, and schedule adherence of the CodeGuard platform.")

    add_heading_2(doc, "12.1 Technical Feasibility")
    add_paragraph(doc,
        "The technical feasibility evaluates the availability of mature programming languages, libraries, and architectural frameworks required to satisfy the project requirements:")
    add_bullet(doc, "Python & AST Capabilities: Python's standard library provides a mature, built-in 'ast' module that parses Python source code into structured syntax trees without requiring external dependencies, making syntax inspection and complexity calculation straightforward.")
    add_bullet(doc, "Bandit SAST Engine: Bandit is an actively maintained, battle-tested security analyzer backed by the OpenStack foundation with robust CLI and programmatic JSON export capabilities.")
    add_bullet(doc, "Ruff Linter Performance: Ruff is compiled to native machine code via Rust, achieving execution speeds up to 100x faster than traditional Python linters. This guarantees that static analysis will not introduce severe latency.")
    add_bullet(doc, "FastAPI & Modern Web Stack: FastAPI provides native asynchronous request processing, automatic OpenAPI documentation generation, and high-performance Pydantic data serialization.")
    add_bullet(doc, "Technical Feasibility Verdict: Highly Feasible. All chosen technologies are stable, open-source, and have proven production track records.")

    add_heading_2(doc, "12.2 Operational Feasibility")
    add_paragraph(doc,
        "Operational feasibility assesses how effectively the proposed software fits into daily engineering workflows and whether developers will encounter friction in adoption:")
    add_bullet(doc, "Zero-Configuration Onboarding: Unlike complex enterprise platforms requiring database clustering and dedicated server admins, CodeGuard boots up via a single Docker Compose command ('docker compose up -d').")
    add_bullet(doc, "Intuitive Visual Dashboard: The React SPA eliminates the cognitive barrier of raw command-line tools. Developers can drag-and-drop a ZIP archive and inspect findings with syntax highlighting in under a minute.")
    add_bullet(doc, "Operational Feasibility Verdict: Highly Feasible. The platform simplifies security verification without altering existing development workflows.")

    add_heading_2(doc, "12.3 Economic Feasibility")
    add_paragraph(doc,
        "Economic feasibility assesses the total cost of development, infrastructure hosting, and long-term licensing:")
    add_bullet(doc, "Zero Software Licensing Costs: CodeGuard is engineered entirely with open-source software under permissive MIT, Apache 2.0, and BSD licenses (Python, FastAPI, React, PostgreSQL, Bandit, Ruff, ReportLab).")
    add_bullet(doc, "Low Infrastructure Requirements: The optimized micro-services architecture runs comfortably on modest cloud hardware (2 vCPUs, 4 GB RAM) costing less than $20/month, representing massive savings compared to commercial SAST licenses ($10,000+ annually).")
    add_bullet(doc, "Economic Feasibility Verdict: Highly Feasible. Zero software licensing expenditure and minimal hosting costs.")

    add_heading_2(doc, "12.4 Schedule and Legal Feasibility")
    add_bullet(doc, "Schedule Adherence: The 12-week internship timeframe was structured into agile two-week sprints covering requirements, backend API development, analysis engine integration, UI construction, testing, and documentation.")
    add_bullet(doc, "Legal Compliance: All third-party dependencies were audited for license compatibility. No GPL-restricted code was statically linked that would violate enterprise intellectual property standards.")

    add_page_break(doc)

    # =========================================================================
    # SECTION 13: HARDWARE AND SOFTWARE REQUIREMENTS
    # =========================================================================
    add_heading_1(doc, "13.0 HARDWARE AND SOFTWARE REQUIREMENTS")
    
    add_paragraph(doc, "The minimal and recommended hardware and software configurations required to host, develop, and operate CodeGuard are specified below.")

    add_heading_2(doc, "13.1 Hardware Requirements")
    headers_hw = ["Hardware Component", "Minimum Development Spec", "Recommended Production Server Spec"]
    rows_hw = [
        ["Processor (CPU)", "Dual-Core 2.0 GHz (x86_64 or ARM64)", "Quad-Core 3.0+ GHz (e.g., AMD EPYC / Intel Xeon)"],
        ["System Memory (RAM)", "4 GB DDR4", "8 GB to 16 GB DDR4/DDR5"],
        ["Storage Space", "10 GB Available SSD Storage", "50 GB High-Speed NVMe Storage (for DB & Scans)"],
        ["Network Interface", "Standard 10/100 Mbps NIC", "Gigabit Ethernet (1 Gbps) with SSL/TLS termination"]
    ]
    create_styled_table(doc, headers_hw, rows_hw, col_widths=[2.0, 2.2, 2.3])

    add_heading_2(doc, "13.2 Software Requirements")
    headers_sw = ["Software Layer", "Technology Component", "Version Specification", "Purpose / Role"]
    rows_sw = [
        ["Operating System", "Linux (Ubuntu / Debian / Alpine) or Windows 11", "Ubuntu 22.04 LTS / Alpine 3.19", "Host OS / Container Base"],
        ["Backend Runtime", "Python", "Version 3.11 or 3.12", "Core Application Runtime"],
        ["Web Framework", "FastAPI + Uvicorn ASGI", "FastAPI >= 0.110.0, Uvicorn >= 0.28.0", "Asynchronous REST API Gateway"],
        ["Database System", "PostgreSQL Server", "Version 16.2+", "Relational Storage for Scans & Users"],
        ["Database ORM", "SQLAlchemy + Alembic", "SQLAlchemy >= 2.0.28, Alembic >= 1.13.0", "ORM & Schema Version Migration"],
        ["Frontend Runtime", "Node.js + npm", "Node.js >= 20.11.0 LTS", "Frontend Build & Bundling"],
        ["Frontend Framework", "React + TypeScript + Tailwind CSS", "React 18.2, TypeScript 5.3, Tailwind 3.4", "User Interface Presentation Layer"],
        ["Security Scanner", "Bandit", "Bandit >= 1.7.8", "SAST Vulnerability Detection Engine"],
        ["Linter & Formatter", "Ruff", "Ruff >= 0.3.4", "Code Quality & Complexity Engine"],
        ["PDF Engine", "ReportLab", "ReportLab >= 4.1.0", "Vector PDF Audit Report Generation"],
        ["Containerization", "Docker & Docker Compose", "Docker Engine >= 25.0, Compose >= 2.24", "Container Orchestration & Isolation"]
    ]
    create_styled_table(doc, headers_sw, rows_sw, col_widths=[1.4, 1.8, 1.5, 1.8])

    add_page_break(doc)

    # =========================================================================
    # SECTION 14: TECHNOLOGY STACK AND JUSTIFICATION
    # =========================================================================
    add_heading_1(doc, "14.0 TECHNOLOGY STACK AND JUSTIFICATION")
    
    add_paragraph(doc,
        "Every component in the CodeGuard technology stack was deliberately evaluated and selected based on benchmarked performance, "
        "security hardening characteristics, and architectural maintainability.")

    add_heading_2(doc, "14.1 Backend Framework: FastAPI vs. Flask and Django")
    add_paragraph(doc,
        "While Django and Flask are established Python frameworks, FastAPI was chosen for three definitive reasons:")
    add_bullet(doc, "Native Asynchronous Performance: Built upon Starlette and ASGI, FastAPI natively handles non-blocking asynchronous I/O, allowing concurrent execution of file validation, disk writing, and worker process spawning without blocking the server event loop.")
    add_bullet(doc, "Automatic Data Validation & Serialization: FastAPI leverages Pydantic v2 to enforce strict type hints, automatically validating incoming multipart/form-data and JSON request payloads with clear, auto-generated error responses.")
    add_bullet(doc, "Automated OpenAPI & Swagger Documentation: FastAPI automatically generates interactive OpenAPI documentation (/docs) directly from route function signatures and Pydantic schemas, drastically streamlining frontend-backend collaboration.")

    add_heading_2(doc, "14.2 Code Analysis Engines: AST, Bandit, and Ruff")
    add_bullet(doc, "Native Python AST: Utilizing Python's built-in 'ast' module allows CodeGuard to parse source code into an in-memory tree of nodes without executing the code. Custom NodeVisitor subclasses can traverse the tree to detect dangerous builtin calls (eval, exec, compile) and unhandled syntax errors before any third-party scanner runs.")
    add_bullet(doc, "Bandit SAST: Developed specifically for Python by the OpenStack foundation, Bandit inspects AST nodes against security rule plugins (B101-B703), detecting serious threats such as SQL injection, hardcoded secrets, weak cryptographic algorithms (MD5/SHA1), and unsafe shell subprocesses.")
    add_bullet(doc, "Ruff Quality Engine: Traditional Python linters (Flake8, Pylint) are written in Python and execute slowly on large codebases. Ruff is engineered in Rust from scratch. It is over 10 to 100 times faster, reimplements hundreds of Flake8, isort, and pyupgrade rules, and provides instantaneous McCabe cyclomatic complexity (C901) calculation.")

    add_heading_2(doc, "14.3 Database and ORM: PostgreSQL & SQLAlchemy 2.0")
    add_paragraph(doc,
        "PostgreSQL 16 was selected as the relational database engine because of its enterprise reliability, strict ACID guarantees, and sophisticated JSONB querying capabilities. "
        "SQLAlchemy 2.0 provides modern typed queries, explicit transaction management, and seamless integration with Alembic for automated database migrations.")

    add_heading_2(doc, "14.4 Frontend: React, TypeScript, and Tailwind CSS")
    add_paragraph(doc,
        "The frontend is implemented as a decoupled Single Page Application (SPA). React 18 with TypeScript ensures compile-time type safety, component reusability, and clean state management. "
        "Tailwind CSS provides a utility-first styling system that allows rapid construction of clean, accessible, and responsive dashboards.")

    add_page_break(doc)

    # =========================================================================
    # SECTION 15: SYSTEM ARCHITECTURE
    # =========================================================================
    add_heading_1(doc, "15.0 SYSTEM ARCHITECTURE")
    
    add_paragraph(doc,
        "CodeGuard is architected using a decoupled, multi-tier micro-service pattern designed to isolate presentation, application logic, "
        "analysis execution, and persistent storage into distinct layers. This separation of concerns ensures horizontal scalability, "
        "security sandboxing, and maintainability.")

    if os.path.exists("figures/architecture_diagram.png"):
        add_figure(doc, "figures/architecture_diagram.png", 
                   "Figure 1: CodeGuard Multi-Tier System Architecture Diagram (Presentation, Gateway, Engine & Storage Tiers)", 
                   width_inches=6.3)

    add_heading_2(doc, "15.1 Architectural Layers Description")
    add_paragraph(doc, "The system architecture consists of four distinct tiers:")
    
    add_paragraph(doc, "1. Presentation Tier (Frontend SPA):", bold_prefix="Tier 1 - Presentation Layer: ")
    add_paragraph(doc,
        "A responsive Single Page Application built with React 18 and TypeScript. It communicates with the backend exclusively via HTTPS REST API calls. "
        "The presentation layer renders the security metric cards, severity breakdown charts, project workspaces, interactive code inspection views with line-number highlights, "
        "and triggering controls for PDF/JSON report downloads.")

    add_paragraph(doc, "2. Application & API Gateway Tier (FastAPI ASGI Server):", bold_prefix="Tier 2 - API Gateway Layer: ")
    add_paragraph(doc,
        "The FastAPI application acts as the central controller and entry point. It enforces JWT bearer authentication, role-based authorization, "
        "request body validation via Pydantic, rate-limiting, and CORS policies. It hosts the Upload Sanitizer service, which inspects incoming files "
        "for Zip-Slip vulnerabilities before delegating processing to the core analysis engine.")

    add_paragraph(doc, "3. Core Static Analysis & Assessment Engine:", bold_prefix="Tier 3 - Static Analysis Engine: ")
    add_paragraph(doc,
        "The analytical core of the platform. It orchestrates the parallel/sequential execution of three sub-analyzers: "
        "(a) Python AST Visitor for syntax validation and dangerous builtin calls; "
        "(b) Bandit SAST for Common Weakness Enumeration security testing; and "
        "(c) Ruff for quality, PEP 8, and cyclomatic complexity checking. "
        "The Normalizer and Severity Mapper converts all raw outputs into the canonical finding model, while the Diff Engine computes revision differences.")

    add_paragraph(doc, "4. Data Persistence & Storage Tier:", bold_prefix="Tier 4 - Persistence & Storage Layer: ")
    add_paragraph(doc,
        "Consists of a PostgreSQL 16 database storing relational records of users, projects, scans, files, findings, and scan comparisons. "
        "Additionally, an ephemeral filesystem sandbox manages temporary scan directories that are strictly isolated and purged upon scan completion.")

    add_page_break(doc)

    # =========================================================================
    # SECTION 16: UML DIAGRAMS
    # =========================================================================
    add_heading_1(doc, "16.0 UML SYSTEM MODELING & ARCHITECTURAL DIAGRAMS")
    
    add_paragraph(doc,
        "To provide rigorous visual and structural documentation of the CodeGuard platform in accordance with standard software engineering practices, "
        "five standard Unified Modeling Language (UML) diagrams are presented and analyzed in this section.")

    # 16.1 Use Case Diagram
    add_heading_2(doc, "16.1 UML Use Case Diagram")
    add_paragraph(doc,
        "The Use Case Diagram defines the interactions between human actors and the functional capabilities enclosed within the CodeGuard system boundary. "
        "Two primary actors interact with the system:")
    add_bullet(doc, "Software Developer (Primary Actor): Responsible for creating projects, uploading source code archives, triggering scans, inspecting contextual findings, marking issues as resolved, and exporting reports.")
    add_bullet(doc, "Security Auditor / Lead Reviewer (Secondary Actor): Responsible for performing architectural security reviews, validating false positive markings, comparing scan revisions across releases, and auditing overall compliance.")

    if os.path.exists("figures/use_case_diagram.png"):
        add_figure(doc, "figures/use_case_diagram.png", 
                   "Figure 2: UML Use Case Diagram illustrating Developer and Auditor Interactions with CodeGuard", 
                   width_inches=6.0)

    add_paragraph(doc, "Use Case Specifications:")
    add_bullet(doc, "UC-1: Register & Authenticate: Users establish identity and obtain a cryptographically signed JWT bearer token.")
    add_bullet(doc, "UC-2: Create & Manage Projects: Organizes repositories and scans under distinct logical project workspaces.")
    add_bullet(doc, "UC-3: Upload Python Files / ZIP Archive: Ingests source code packages through the secure validation filter.")
    add_bullet(doc, "UC-4: Trigger Multi-Engine Code Scan: Initiates synchronized execution of AST, Bandit, and Ruff analysis.")
    add_bullet(doc, "UC-5: View Centralized Findings Dashboard: Presents interactive tables with severity badges and search filters.")
    add_bullet(doc, "UC-6: Request AI Remediation Suggestion: Requests contextual vulnerability explanations and secure patch snippets.")
    add_bullet(doc, "UC-7: Compare Scan Revisions (Scan Diff): Calculates New, Fixed, and Recurring issues between two scan runs.")
    add_bullet(doc, "UC-8: Update Resolution Status: Transitions finding states between OPEN, FALSE_POSITIVE, and RESOLVED.")
    add_bullet(doc, "UC-9: Generate & Download PDF/JSON Report: Exports publication-grade audit documents.")

    add_page_break(doc)

    # 16.2 Activity Diagram
    add_heading_2(doc, "16.2 UML Activity Diagram")
    add_paragraph(doc,
        "The Activity Diagram models the dynamic operational workflow of CodeGuard, detailing the sequential, conditional, and parallel control flows "
        "from the instant a developer uploads source code to the final rendering of findings and report generation.")

    if os.path.exists("figures/activity_diagram.png"):
        add_figure(doc, "figures/activity_diagram.png", 
                   "Figure 3: UML Activity Diagram depicting the End-to-End Code Scan and Normalization Lifecycle", 
                   width_inches=5.8)

    add_paragraph(doc, "Activity Workflow Stages:")
    add_bullet(doc, "Upload & Ingestion: The developer submits a single .py file or a compressed .zip archive along with the target project identifier.")
    add_bullet(doc, "Security Validation & Decision: The system validates file size (<25 MB), MIME type, and extension. Invalid uploads trigger an immediate HTTP 400 Bad Request.")
    add_bullet(doc, "Safe Extraction: Valid ZIP archives are unpacked using canonical path sanitization, rejecting any member attempting Zip-Slip traversal.")
    add_bullet(doc, "Parallel Analysis Fork: The engine spawns parallel/concurrent analysis tasks across Python AST, Bandit SAST, and Ruff Linter.")
    add_bullet(doc, "Join & Normalization: Execution joins to normalize all findings into a unified canonical schema, map severities, and assign CWE numbers.")
    add_bullet(doc, "Persistence & Diffing: Scan metadata and findings are committed to PostgreSQL, and diff comparison is computed against prior scans.")
    add_bullet(doc, "Reporting & Presentation: The dashboard updates in real-time and ReportLab PDF compilation becomes available.")

    add_page_break(doc)

    # 16.3 Sequence Diagram
    add_heading_2(doc, "16.3 UML Sequence Diagram")
    add_paragraph(doc,
        "The Sequence Diagram delineates the chronological exchange of HTTP requests, internal method calls, and database transactions "
        "among the React Frontend, FastAPI Router, Core Analysis Engine, PostgreSQL Database, and ReportLab Service.")

    if os.path.exists("figures/sequence_diagram.png"):
        add_figure(doc, "figures/sequence_diagram.png", 
                   "Figure 4: UML Sequence Diagram showing Message Exchanges during Scan Execution and Report Generation", 
                   width_inches=6.2)

    add_paragraph(doc, "Key Sequence Interactions:")
    add_bullet(doc, "Step 1-2: User uploads project code via React UI, triggering an asynchronous multipart/form-data POST request to /api/v1/scans/upload.")
    add_bullet(doc, "Step 3-5: FastAPI Router validates the archive, extracts files safely into an ephemeral workspace, and invokes the multi-engine orchestrator.")
    add_bullet(doc, "Step 6-8: Analysis findings are normalized, severity scores are computed, and records are committed to the PostgreSQL database within an atomic transaction.")
    add_bullet(doc, "Step 9-10: FastAPI responds with HTTP 201 Created and the ScanSummaryResponse DTO, rendering the results on the React UI.")
    add_bullet(doc, "Step 11-14: When the user requests an audit report, a GET request triggers ReportLab to dynamically compile vector charts and return an application/pdf binary stream.")

    add_page_break(doc)

    # 16.4 Component Diagram
    add_heading_2(doc, "16.4 UML Component Diagram")
    add_paragraph(doc,
        "The Component Diagram illustrates the structural organization and software dependencies among CodeGuard's modular components, "
        "emphasizing high cohesion within modules and loose coupling between system layers.")

    if os.path.exists("figures/component_diagram.png"):
        add_figure(doc, "figures/component_diagram.png", 
                   "Figure 5: UML Component Diagram illustrating Subsystem Dependencies and Interfaces", 
                   width_inches=6.2)

    add_paragraph(doc, "Component Subsystem Breakdown:")
    add_bullet(doc, "Frontend Components: Comprises the AuthModule, ProjectExplorer, UploadModal, FindingsDashboard, MonacoCodeViewer, and ReportClient.")
    add_bullet(doc, "API Controller Components: FastAPI Routers including AuthController, ProjectController, ScanController, and ReportController.")
    add_bullet(doc, "Engine Core Components: EngineOrchestrator, ASTParserComponent, BanditAdapter, RuffAdapter, NormalizerComponent, and DiffEngine.")
    add_bullet(doc, "Persistence Components: DBRepository, SQLAlchemySessionManager, AlembicMigrationEngine, and PostgreSQL 16 RDBMS.")

    add_page_break(doc)

    # 16.5 Deployment Diagram
    add_heading_2(doc, "16.5 UML Deployment Diagram")
    add_paragraph(doc,
        "The Deployment Diagram models the physical and containerized hardware topology of CodeGuard, detailing Docker containers, "
        "internal virtual network bridges, port mappings, and persistent volume mounts.")

    if os.path.exists("figures/deployment_diagram.png"):
        add_figure(doc, "figures/deployment_diagram.png", 
                   "Figure 6: UML Deployment Diagram showing Docker Multi-Container Architecture and Networks", 
                   width_inches=6.2)

    add_paragraph(doc, "Containerized Deployment Topology:")
    add_bullet(doc, "Container 1 (codeguard-frontend): Nginx Alpine container serving optimized React SPA static bundles on HTTP Port 80 / 443.")
    add_bullet(doc, "Container 2 (codeguard-backend): Python 3.11-slim container running Uvicorn ASGI on Port 8000, housing FastAPI, Bandit, Ruff, and ReportLab.")
    add_bullet(doc, "Container 3 (codeguard-db): PostgreSQL 16 Alpine container listening on internal Port 5432 with an isolated network bind.")
    add_bullet(doc, "Docker Network & Volumes: Containers communicate over an isolated bridge network (codeguard-network), with persistent host storage bound to postgres_data.")

    return doc
