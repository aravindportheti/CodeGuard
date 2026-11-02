from report_styles import (
    add_heading_1, add_heading_2, add_heading_3, add_paragraph,
    add_bullet, add_callout, add_page_break, COLOR_PRIMARY, COLOR_SECONDARY,
    create_styled_table
)
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def build_part1(doc):
    # =========================================================================
    # SECTION 1: COVER PAGE
    # =========================================================================
    p_title_space = doc.add_paragraph()
    p_title_space.paragraph_format.space_before = Pt(36)
    
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_title = p_title.add_run("CodeGuard: An Intelligent Source Code Quality Assessment and Security Vulnerability Detection Platform Using Python")
    run_title.font.name = "Calibri"
    run_title.font.size = Pt(22)
    run_title.font.bold = True
    run_title.font.color.rgb = COLOR_PRIMARY
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(12)
    p_sub.paragraph_format.space_after = Pt(36)
    run_sub = p_sub.add_run("A Comprehensive Internship Project Report Submitted in Partial Fulfillment of the Requirements for the Degree of Bachelor of Technology in Computer Science and Engineering")
    run_sub.font.name = "Calibri"
    run_sub.font.size = Pt(11)
    run_sub.font.italic = True
    run_sub.font.color.rgb = RGBColor(71, 85, 105)
    
    # Border / Divider Line
    callout_box = doc.add_table(rows=1, cols=1)
    cell = callout_box.cell(0, 0)
    p_box = cell.paragraphs[0]
    p_box.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_box = p_box.add_run("INTERNSHIP CAPSTONE PROJECT REPORT — ADVANCED PYTHON TRACK")
    r_box.font.name = "Calibri"
    r_box.font.size = Pt(10)
    r_box.font.bold = True
    r_box.font.color.rgb = COLOR_PRIMARY

    p_mid_space = doc.add_paragraph()
    p_mid_space.paragraph_format.space_before = Pt(30)
    
    # Metadata Table
    p_meta = doc.add_paragraph()
    p_meta.paragraph_format.space_before = Pt(10)
    
    headers_meta = ["Candidate Details", "Institutional & Industry Supervision"]
    rows_meta = [
        [
            "Submitted By:\n[Student Name]\nUSN / Roll No: [Roll Number / USN]\nProgram: B.Tech / B.E. / MCA\nDepartment of Computer Science and Engineering",
            "Internal Guide:\n[Internal Faculty Guide Name]\nAssistant / Associate Professor\nDepartment of Computer Science & Engineering\n[College / University Name]"
        ],
        [
            "Internship Organization:\n[Internship Organization / Company Name]\nCorporate Division: Cyber Security & Cloud DevOps\nLocation: [City, State, Country]",
            "Industry Supervisor / Mentor:\n[Industry Supervisor / Mentor Name]\nSenior Python Software Architect / Lead Security Engineer\n[Internship Organization / Company Name]"
        ],
        [
            "Academic Year: [Submission Date / Academic Year]\nDate of Submission: [Submission Date]",
            "Evaluation Committee:\nHead of Department: [Head of Department Name]\nExternal Examiner: [External Examiner Name]"
        ]
    ]
    create_styled_table(doc, headers_meta, rows_meta, col_widths=[3.2, 3.3])
    
    add_page_break(doc)

    # =========================================================================
    # SECTION 2: CERTIFICATE
    # =========================================================================
    add_heading_1(doc, "CERTIFICATE OF ORIGINAL WORK")
    
    add_paragraph(doc, 
        "This is to certify that the project report titled \"CodeGuard: An Intelligent Source Code Quality Assessment and Security Vulnerability Detection Platform Using Python\" "
        "is a bonafide record of the work carried out by [Student Name] bearing University Seat Number / Roll Number [Roll Number / USN] in partial fulfillment of the requirements "
        "for the award of the Degree of Bachelor of Technology / Master of Computer Applications in Computer Science and Engineering from [College / University Name], affiliated with [Affiliated University Name], "
        "during the academic year [Submission Date / Academic Year].")
        
    add_paragraph(doc,
        "The project work described in this report has been carried out under our direct supervision and mentorship at [Internship Organization / Company Name]. "
        "To the best of our knowledge, the results and architectural designs embodied in this capstone report have not been submitted to any other university or institute for the award of any degree or diploma.")
        
    p_sig_space = doc.add_paragraph()
    p_sig_space.paragraph_format.space_before = Pt(40)
    
    headers_sig = ["Internal Guide", "Industry Mentor", "Head of Department"]
    rows_sig = [
        [
            "__________________________\n[Internal Faculty Guide Name]\nDesignation: Guide / Asst. Professor\nDepartment of CSE\n[College / University Name]",
            "__________________________\n[Industry Supervisor / Mentor Name]\nLead Security Architect\nSoftware Engineering Division\n[Internship Organization / Company]",
            "__________________________\n[Head of Department Name]\nProfessor and Head\nDepartment of CSE\n[College / University Name]"
        ]
    ]
    create_styled_table(doc, headers_sig, rows_sig, col_widths=[2.1, 2.2, 2.2])

    p_sig2_space = doc.add_paragraph()
    p_sig2_space.paragraph_format.space_before = Pt(25)
    
    headers_eval = ["Internal Examiner Signature", "External Examiner Signature"]
    rows_eval = [
        [
            "Signature: __________________________\nName: ______________________________\nDate: ______________________________",
            "Signature: __________________________\nName: ______________________________\nDate: ______________________________"
        ]
    ]
    create_styled_table(doc, headers_eval, rows_eval, col_widths=[3.25, 3.25])

    add_page_break(doc)

    # =========================================================================
    # SECTION 3: DECLARATION
    # =========================================================================
    add_heading_1(doc, "DECLARATION OF ACADEMIC INTEGRITY")
    
    add_paragraph(doc,
        "I, [Student Name], student of Bachelor of Technology in Computer Science and Engineering at [College / University Name], bearing Roll Number / USN [Roll Number / USN], "
        "hereby declare that the internship capstone project report titled \"CodeGuard: An Intelligent Source Code Quality Assessment and Security Vulnerability Detection Platform Using Python\" "
        "is an authentic record of my own research and engineering work carried out during my internship period at [Internship Organization / Company Name] under the joint guidance of "
        "[Industry Supervisor / Mentor Name] (Industry Mentor) and [Internal Faculty Guide Name] (Faculty Guide).")
        
    add_paragraph(doc,
        "I solemnly confirm that:")
    add_bullet(doc, "The code, algorithms, architectural designs, and benchmarks presented in this report are original implementations developed during my internship program.")
    add_bullet(doc, "Due citations, references, and acknowledgements have been strictly provided for all third-party libraries, open-source frameworks (FastAPI, Bandit, Ruff, ReportLab), and academic papers utilized.")
    add_bullet(doc, "The performance metrics, test cases, and scan findings documented in this report reflect actual experimental runs on synthetic and real-world Python codebases without fabrication.")
    add_bullet(doc, "This project report has not been submitted previously in part or in full to any other university or academic board for any academic credit, degree, or qualification.")

    p_dec_sig = doc.add_paragraph()
    p_dec_sig.paragraph_format.space_before = Pt(45)
    add_paragraph(doc, "Place: [City, State, Country]\nDate: [Submission Date]\n\n\n___________________________________\nSignature of the Student\n[Student Name]\nUSN: [Roll Number / USN]")

    add_page_break(doc)

    # =========================================================================
    # SECTION 4: ACKNOWLEDGEMENT
    # =========================================================================
    add_heading_1(doc, "ACKNOWLEDGEMENT")
    
    add_paragraph(doc,
        "The successful completion of this internship project and the compilation of this comprehensive technical report is the result of continuous support, intellectual guidance, "
        "and invaluable encouragement from several mentors, institutions, and colleagues whom I wish to acknowledge with profound gratitude.")
        
    add_paragraph(doc,
        "First and foremost, I express my deepest gratitude to my Industry Mentor, [Industry Supervisor / Mentor Name], Senior Python Software Architect at [Internship Organization / Company Name], "
        "for giving me the opportunity to work on cutting-edge DevSecOps and static application security tooling. His insightful feedback, rigorous code review standards, and deep technical wisdom "
        "on Python Abstract Syntax Trees (AST), asynchronous architectures with FastAPI, and secure archive processing significantly shaped the direction and quality of this project.")
        
    add_paragraph(doc,
        "I am equally indebted to my Internal Faculty Guide, [Internal Faculty Guide Name], for their scholarly advice, constant academic encouragement, and structured reviews throughout the project lifecycle. "
        "I extend my sincere thanks to [Head of Department Name], Head of the Department of Computer Science and Engineering, and [Principal / Dean Name], Principal of [College / University Name], "
        "for fostering an exceptional learning environment and providing the necessary infrastructure, compute resources, and laboratory access.")
        
    add_paragraph(doc,
        "I also convey my warm appreciation to the engineering team and fellow interns at [Internship Organization / Company Name] for their collaborative spirit, engaging technical discussions, "
        "and active participation during the beta testing phase of the CodeGuard platform.")
        
    add_paragraph(doc,
        "Finally, I express my heartfelt gratitude to my family and friends for their unconditional love, moral support, and patience throughout my academic journey.")

    p_ack_sig = doc.add_paragraph()
    p_ack_sig.paragraph_format.space_before = Pt(30)
    add_paragraph(doc, "[Student Name]\nDepartment of Computer Science and Engineering\n[College / University Name]")

    add_page_break(doc)

    # =========================================================================
    # SECTION 5: ABSTRACT
    # =========================================================================
    add_heading_1(doc, "ABSTRACT")
    
    add_paragraph(doc,
        "Modern software engineering ecosystems rely heavily on the Python programming language for building web backends, microservices, cloud automations, and data pipelines. "
        "However, Python's dynamic typing, flexible execution model, and extensive third-party package ecosystem frequently introduce subtle security vulnerabilities, "
        "such as SQL injection, unsafe deserialization, hardcoded secrets, shell injection, and performance degradation stemming from anti-patterns and high cyclomatic complexity. "
        "Traditional security auditing approaches often rely on disconnected, high-latency command-line tools or costly enterprise suites that lack accessibility, contextual code visualization, "
        "and unified multi-engine correlation.")
        
    add_paragraph(doc,
        "To solve this critical challenge, this internship capstone project presents CodeGuard: an intelligent, full-stack source code quality assessment and security vulnerability detection platform. "
        "CodeGuard implements a decoupled, high-throughput static application security testing (SAST) architecture powered by an asynchronous Python FastAPI backend, a high-performance React and TypeScript frontend, "
        "and a robust PostgreSQL relational database managed via SQLAlchemy 2.0 and Alembic. The platform features a novel multi-engine static analysis pipeline that synchronizes three specialized analysis layers: "
        "(1) Native Python Abstract Syntax Tree (AST) inspection for syntax errors, cyclomatic complexity, and dangerous builtin functions (e.g., eval(), exec(), insecure pickle.loads()); "
        "(2) Bandit SAST engine for comprehensive Common Weakness Enumeration (CWE) and OWASP Top 10 Python vulnerability detection; and "
        "(3) Ruff, an ultra-fast Rust-powered linter for PEP 8 compliance, code smell detection, and cyclomatic complexity (C901) profiling.")
        
    add_paragraph(doc,
        "CodeGuard introduces an intelligent Finding Normalization and Severity Classification Engine that unifies disparate linter and scanner outputs into a standardized canonical JSON data model, "
        "mapping findings across Critical, High, Medium, and Low severity tiers. To support real-world development workflows, CodeGuard provides secure archive extraction with rigorous Zip-Slip and path-traversal protection, "
        "scan revision diffing (tracking New, Fixed, and Recurring issues across builds), interactive source-code inspection with line-level highlights, resolution state management, "
        "AI-assisted vulnerability explanations and remediation snippets, and automated audit report generation in professional vector PDF (via ReportLab) and raw JSON formats. "
        "The entire platform is fully containerized using Docker and Docker Compose, achieving enterprise-grade reproducibility, sandboxed isolation, and high scanning throughput.")
        
    add_callout(doc,
        "Keywords: Static Application Security Testing (SAST), Python Abstract Syntax Tree (AST), Bandit, Ruff, FastAPI, React, DevSecOps, Vulnerability Remediation, ReportLab, Docker.",
        title="INDEX TERMS", callout_type="info")

    add_page_break(doc)

    # =========================================================================
    # SECTION 6: TABLE OF CONTENTS
    # =========================================================================
    add_heading_1(doc, "TABLE OF CONTENTS")
    
    toc_data = [
        ["1.0", "Cover Page & Project Overview", "i"],
        ["2.0", "Certificate of Original Work", "ii"],
        ["3.0", "Declaration of Academic Integrity", "iii"],
        ["4.0", "Acknowledgement", "iv"],
        ["5.0", "Abstract & Key Terms", "v"],
        ["6.0", "Table of Contents & List of Figures / Tables", "vi"],
        ["7.0", "Introduction & Industry Context", "1"],
        ["8.0", "Problem Statement & Threat Landscape", "4"],
        ["9.0", "Existing System and Limitations", "7"],
        ["10.0", "Proposed System & Architectural Innovation", "10"],
        ["11.0", "Objectives and Scope of the Project", "13"],
        ["12.0", "Feasibility Study (Technical, Operational, Economic, Schedule)", "16"],
        ["13.0", "Hardware and Software Requirements", "19"],
        ["14.0", "Technology Stack and Technical Justification", "22"],
        ["15.0", "System Architecture & Multi-Tier Topology", "26"],
        ["16.0", "UML System Modeling & Architectural Diagrams", "30"],
        ["17.0", "Database Design, ER Modeling & Data Dictionary", "37"],
        ["18.0", "Detailed Module Descriptions (10 Core Subsystems)", "43"],
        ["19.0", "System Workflows, Algorithms & Pseudocode", "51"],
        ["20.0", "Backend and Frontend Implementation Details", "58"],
        ["21.0", "REST API Documentation & Contract Specifications", "67"],
        ["22.0", "User Interface Design & Experience Architecture", "73"],
        ["23.0", "Security Engineering, Upload Hardening & Sandbox Isolation", "78"],
        ["24.0", "Testing Methodology & Comprehensive Test Cases", "83"],
        ["25.0", "Performance Benchmarks & Statistical Evaluation", "91"],
        ["26.0", "Results, Discussion & Empirical Vulnerability Findings", "96"],
        ["27.0", "System Limitations & Known Constraints", "101"],
        ["28.0", "Future Enhancements & Enterprise Roadmap", "104"],
        ["29.0", "Conclusion & Key Learning Outcomes", "107"],
        ["30.0", "Academic & Technical References", "110"],
        ["31.0", "Appendices: Docker Compose, Config & Test Suites", "113"],
        ["32.0", "Comprehensive Technical Viva Questions & Answers", "118"]
    ]
    create_styled_table(doc, ["Section", "Chapter Title", "Ref Page"], toc_data, col_widths=[1.0, 4.8, 0.7])
    
    add_heading_2(doc, "List of Figures")
    fig_list = [
        ["Figure 1", "CodeGuard Multi-Tier System Architecture Diagram", "Section 15"],
        ["Figure 2", "UML Use Case Diagram: Developer & Auditor Interactions", "Section 16.1"],
        ["Figure 3", "UML Activity Diagram: End-to-End Code Scan Lifecycle", "Section 16.2"],
        ["Figure 4", "UML Sequence Diagram: Asynchronous Analysis & Report Flow", "Section 16.3"],
        ["Figure 5", "UML Component Diagram: Decoupled Subsystem Architecture", "Section 16.4"],
        ["Figure 6", "UML Deployment Diagram: Docker Container Topology", "Section 16.5"],
        ["Figure 7", "Database Entity-Relationship (ER) Diagram", "Section 17.1"],
        ["Figure 8", "Multi-Engine Finding Normalization & Severity Mapping Pipeline", "Section 19.3"],
        ["Figure 9", "UI Design: Centralized Findings Dashboard & Metrics Overview", "Section 22.1"],
        ["Figure 10", "UI Design: Interactive Code Inspection & AI Remediation View", "Section 22.2"]
    ]
    create_styled_table(doc, ["Figure No.", "Caption Title", "Location"], fig_list, col_widths=[1.2, 4.3, 1.0])

    add_page_break(doc)

    # =========================================================================
    # SECTION 7: INTRODUCTION
    # =========================================================================
    add_heading_1(doc, "7.0 INTRODUCTION")
    
    add_heading_2(doc, "7.1 Background and Industry Context")
    add_paragraph(doc,
        "In the contemporary software engineering landscape, Python has established itself as one of the most widely adopted programming languages globally, "
        "powering mission-critical web applications, cloud-native microservices, automated infrastructure tooling, and artificial intelligence pipelines. "
        "Its concise syntax, dynamic nature, and massive package ecosystem (the Python Package Index or PyPI) enable rapid prototyping and agile release cycles. "
        "However, this unprecedented velocity often comes at the expense of rigorous code security and architectural quality.")
        
    add_paragraph(doc,
        "Because Python is dynamically typed and interpreted, entire categories of errors—such as subtle runtime syntax errors, missing exception handling, "
        "and unvalidated variable types—cannot be detected at compile-time as in static languages such as C++, Java, or Go. Furthermore, the ease with which developers "
        "can construct dynamic SQL queries, invoke OS-level subprocesses via shell commands, serialize and deserialize data using pickle, or dynamically evaluate expressions "
        "with eval() and exec() introduces severe attack surfaces. In enterprise systems, these vulnerabilities lead directly to devastating data breaches, "
        "remote code execution (RCE), privilege escalation, and costly regulatory non-compliance.")

    add_heading_2(doc, "7.2 The Shift-Left Paradigm and Static Code Analysis")
    add_paragraph(doc,
        "Historically, software security was treated as a reactionary phase conducted at the very end of the Software Development Life Cycle (SDLC) through penetration testing "
        "or manual security audits immediately prior to production deployment. This late-stage discovery creates massive engineering bottlenecks: remediating an architectural flaw "
        "or injection vulnerability in production is estimated by the Systems Sciences Institute at IBM to cost up to 30 times more than addressing it during initial development.")
        
    add_paragraph(doc,
        "To mitigate this risk, modern DevSecOps methodologies advocate for the 'Shift-Left' paradigm—integrating automated security and quality verification directly into early developer workflows. "
        "Static Application Security Testing (SAST) serves as the cornerstone of this paradigm. SAST analyzes software source code without executing the program, "
        "inspecting syntax trees, data flows, and lexical tokens to identify known Common Weakness Enumerations (CWEs) and violations of secure coding standards (such as OWASP Top 10).")

    add_heading_2(doc, "7.3 Overview of the CodeGuard Platform")
    add_paragraph(doc,
        "CodeGuard was conceived and engineered during this internship project to provide software engineering teams with an accessible, high-performance, and unified static analysis platform. "
        "Rather than forcing developers to juggle disparate command-line tools with conflicting outputs, CodeGuard orchestrates three distinct analysis engines into a coherent, web-accessible dashboard:")
    add_bullet(doc, "Python Abstract Syntax Tree (AST) Engine: Operates natively within the Python standard library to identify fatal syntax errors, compute structural cyclomatic complexity, and detect the invocation of dangerous standard functions.")
    add_bullet(doc, "Bandit SAST Engine: A mature, security-focused analyzer developed by the OpenStack Security Group to flag security vulnerabilities across files, such as SQL injection (B608), hardcoded passwords (B105), insecure cryptography (B303), and unsafe subprocesses (B602).")
    add_bullet(doc, "Ruff Quality Engine: An ultra-fast linter built in Rust that scans source code 10 to 100 times faster than traditional Python linters (Flake8, Pylint), verifying PEP 8 standards, flagging code smells, and computing cyclomatic complexity metrics.")

    add_page_break(doc)

    # =========================================================================
    # SECTION 8: PROBLEM STATEMENT
    # =========================================================================
    add_heading_1(doc, "8.0 PROBLEM STATEMENT")
    
    add_heading_2(doc, "8.1 Core Engineering Challenges")
    add_paragraph(doc,
        "Despite the availability of individual open-source linters and scanners, development teams encounter major operational and technical hurdles "
        "when attempting to enforce continuous code quality and security standards. The specific problems addressed by this project include:")
        
    add_paragraph(doc,
        "1. Fragmentation of Analysis Tools:", bold_prefix="Fragmented Ecosystem: ")
    add_paragraph(doc,
        "Developers are forced to install and configure multiple distinct CLI tools—such as Bandit for security, Flake8 or Black for style, and Mypy for typing. "
        "Each tool outputs diagnostic logs in differing formats (raw text, differing JSON schemas, or terminal ANSI colors). Correlating these disparate reports into an actionable remediation plan "
        "is tedious, error-prone, and frequently abandoned by busy engineering teams.")
        
    add_paragraph(doc,
        "2. High False Positive Fatigue:", bold_prefix="Cognitive Overload & False Positives: ")
    add_paragraph(doc,
        "Static analysis tools often emit high rates of false positives or low-priority warnings alongside critical security exploits. Without intelligent normalization, "
        "severity filtering, and contextual source-code visualization, developers experience 'alert fatigue', causing them to overlook genuinely critical vulnerabilities such as SQL injection or remote code execution.")
        
    add_paragraph(doc,
        "3. Lack of Scan Revision Tracking and Diffing:", bold_prefix="Absence of Historical Context: ")
    add_paragraph(doc,
        "Most open-source analyzers evaluate code in isolation, treating each scan as an ephemeral event. They fail to track the evolution of a codebase over time. "
        "A developer cannot readily determine whether a recent commit introduced new security regressions, successfully fixed existing issues, or left recurring vulnerabilities unaddressed.")
        
    add_paragraph(doc,
        "4. Insecure File Ingestion in Web Platforms:", bold_prefix="File Upload Attack Vectors: ")
    add_paragraph(doc,
        "Web-based code review platforms that accept ZIP archives or Python files are notoriously vulnerable to Zip-Slip exploits, path traversal attacks, and denial-of-service (DoS) decompression bombs. "
        "Without rigorous archive validation, file-size gating, and ephemeral sandbox directory isolation, the security platform itself becomes a primary vulnerability.")
        
    add_paragraph(doc,
        "5. The Remediation Gap:", bold_prefix="Lack of Actionable Guidance: ")
    add_paragraph(doc,
        "Standard static analysis tools typically emit cryptic error codes (e.g., 'B608: medium confidence, high severity') without explaining the underlying root cause "
        "or providing concrete, copy-pasteable remediation code snippets adapted to the developer's specific syntax context.")

    add_callout(doc,
        "Problem Statement Summary: How can we build an integrated, secure, and high-performance web platform that consolidates multi-engine static security and code quality analysis, "
        "normalizes heterogeneous findings into an actionable dashboard, tracks scan evolution over time, and provides context-aware remediation guidance without introducing security risks or performance bottlenecks?",
        title="CORE RESEARCH QUESTION", callout_type="warning")

    add_page_break(doc)

    # =========================================================================
    # SECTION 9: EXISTING SYSTEM AND LIMITATIONS
    # =========================================================================
    add_heading_1(doc, "9.0 EXISTING SYSTEM AND LIMITATIONS")
    
    add_heading_2(doc, "9.1 Analysis of Existing Approaches")
    add_paragraph(doc,
        "Currently, software development teams utilize a mixture of manual code reviews, isolated command-line tools, or heavyweight commercial enterprise platforms. "
        "A critical evaluation of these approaches highlights several decisive limitations:")
        
    headers_comp = ["Analysis Feature / Parameter", "Manual Code Review", "Standalone CLI Linters (Bandit / Flake8)", "Enterprise Platforms (SonarQube / Snyk)", "Proposed CodeGuard Platform"]
    rows_comp = [
        ["Speed & Throughput", "Extremely Slow (Days/Weeks)", "Fast for single files, manual CLI", "Moderate (Complex CI/CD queues)", "Real-time Asynchronous (<2.0s per scan)"],
        ["Cost & Licensing", "High (Expensive Engineering Time)", "Free Open-Source (CLI only)", "High Commercial Costs ($10k-$50k/yr)", "Free & Open-Source (Self-Hostable)"],
        ["Tool Aggregation", "None (Human Discretion)", "None (Separate execution required)", "Proprietary Rule Engine", "Unified AST + Bandit + Ruff Normalization"],
        ["Interactive Visual UI", "None (Pull Request comments)", "None (Raw terminal text)", "Complex Enterprise Portal", "Modern React SPA + Contextual Monaco Viewer"],
        ["Scan Comparison / Diffing", "Manual Git diff inspection", "None (Ephemeral execution)", "Branch analysis (Paid Tiers)", "Automated Revision Diffing (New/Fixed/Recurring)"],
        ["Remediation Guidance", "Subject to reviewer expertise", "Generic one-line descriptions", "Generic documentation links", "Contextual AI & Pattern-Based Fix Snippets"],
        ["Archive Ingestion Security", "Not Applicable", "Not Applicable", "Agent-based repository clone", "Hardened Zip-Slip Protected Ingestion"]
    ]
    create_styled_table(doc, headers_comp, rows_comp, col_widths=[1.5, 1.4, 1.4, 1.4, 1.4])

    add_heading_2(doc, "9.2 Key Limitations of Existing Systems")
    add_bullet(doc, "Steep Setup Overhead: Setting up enterprise SAST platforms like SonarQube requires dedicated servers, complex Java runtimes, database clustering, and expensive commercial licenses, putting them out of reach for individual developers, startups, and academic projects.")
    add_bullet(doc, "High Latency of Legacy Linters: Python linters like Pylint and Flake8 are implemented in pure Python and process files sequentially. In repositories with hundreds of modules, scan times can stretch into several minutes, disrupting developer flow.")
    add_bullet(doc, "Lack of Integrated History for Local Projects: Existing open-source CLI tools provide no persistence layer. Once the terminal closes, the scan history is lost, making regression tracking impossible without building custom wrapper scripts.")

    add_page_break(doc)

    # =========================================================================
    # SECTION 10: PROPOSED SYSTEM
    # =========================================================================
    add_heading_1(doc, "10.0 PROPOSED SYSTEM")
    
    add_heading_2(doc, "10.1 System Concept and Architectural Philosophy")
    add_paragraph(doc,
        "The proposed CodeGuard platform addresses the shortcomings of existing solutions by delivering a modern, full-stack, containerized web application "
        "that bridges the gap between raw command-line static analyzers and expensive enterprise security suites. "
        "CodeGuard is architected from the ground up to embody three fundamental engineering principles: speed, accuracy, and developer-centric usability.")
        
    add_paragraph(doc,
        "CodeGuard leverages FastAPI—a high-performance, asynchronous Python web framework built on Starlette and Pydantic—to serve as the backend API gateway. "
        "On the frontend, a responsive Single Page Application (SPA) built with React 18, TypeScript, and Tailwind CSS provides developers with an intuitive dashboard. "
        "Analysis results are persisted in a relational PostgreSQL database via SQLAlchemy 2.0 ORM, ensuring data integrity, fast query performance, and long-term scan tracking.")

    add_heading_2(doc, "10.2 Distinctive Capabilities and Innovations")
    add_paragraph(doc,
        "1. Tri-Engine Static Analysis Orchestration:", bold_prefix="Multi-Engine Triangulation: ")
    add_paragraph(doc,
        "CodeGuard simultaneously executes native Python AST parsing, Bandit security rules, and Ruff linting. By correlating syntactic structure, security vulnerability patterns, "
        "and code quality metrics, the platform provides a 360-degree assessment of Python codebases in a single automated pass.")

    add_paragraph(doc,
        "2. Standardized Finding Normalization Engine:", bold_prefix="Canonical Data Normalization: ")
    add_paragraph(doc,
        "Heterogeneous outputs from all three engines are ingested by a custom normalization pipeline that maps each issue to a canonical schema, extracts ±2 lines of surrounding code context, "
        "and assigns standardized severity tiers (Critical, High, Medium, Low) based on documented risk matrices and CWE classifications.")

    add_paragraph(doc,
        "3. Historical Scan Comparison & Diffing Engine:", bold_prefix="Automated Scan Diffing: ")
    add_paragraph(doc,
        "CodeGuard computes two-way mathematical set differences between consecutive scans within a project, categorizing findings into 'New' (regressions), 'Fixed' (resolved issues), "
        "and 'Recurring' (persistent technical debt). This enables development teams to immediately verify if their remediation efforts were successful.")

    add_paragraph(doc,
        "4. Enterprise-Grade Security and Hardened Upload Pipeline:", bold_prefix="Secure Sandbox Architecture: ")
    add_paragraph(doc,
        "To ensure that CodeGuard itself remains impenetrable, all file ingestion undergoes MIME validation, file-signature checks, maximum file-size limits (25 MB), "
        "and canonical path-traversal sanitization to prevent Zip-Slip attacks. Code scanning occurs within isolated ephemeral temporary directories that are guaranteed to be cleaned up after execution.")

    add_paragraph(doc,
        "5. Automated Audit Reporting (ReportLab PDF & JSON):", bold_prefix="Multi-Format Audit Export: ")
    add_paragraph(doc,
        "With a single click, users can generate executive-ready PDF audit reports featuring vector security charts, executive summaries, and detailed technical vulnerability logs generated via ReportLab, "
        "or download machine-readable JSON exports for automated CI/CD ingestion.")
        
    add_callout(doc,
        "Key Value Proposition: CodeGuard brings the rigor and depth of enterprise-grade DevSecOps security auditing to everyday Python developers in a clean, self-hostable, and lightning-fast package.",
        title="VALUE PROPOSITION", callout_type="success")

    return doc
