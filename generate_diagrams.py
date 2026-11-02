import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ArrowStyle

os.makedirs("figures", exist_ok=True)
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'

# 1. System Architecture Diagram
def create_architecture_diagram():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Background canvas title
    ax.text(50, 97, "CodeGuard Platform: Multi-Tier System Architecture", 
            fontsize=15, fontweight='bold', ha='center', color='#0F172A')
    ax.text(50, 94, "Decoupled Architecture with FastAPI Backend, Static Analysis Engine & React SPA", 
            fontsize=10, ha='center', color='#475569')

    # Tier 1: Client Layer
    box_client = FancyBboxPatch((5, 74), 90, 17, boxstyle="round,pad=0.8", 
                                facecolor='#EFF6FF', edgecolor='#3B82F6', linewidth=1.5)
    ax.add_patch(box_client)
    ax.text(8, 88.5, "PRESENTATION TIER (FRONTEND SPA)", fontsize=11, fontweight='bold', color='#1E40AF')
    
    comp_c1 = FancyBboxPatch((8, 76), 26, 10.5, boxstyle="round,pad=0.5", facecolor='#FFFFFF', edgecolor='#93C5FD', linewidth=1)
    ax.add_patch(comp_c1)
    ax.text(21, 83.5, "React 18 + TypeScript", fontsize=9.5, fontweight='bold', ha='center', color='#1E293B')
    ax.text(21, 78.5, "Tailwind CSS • Lucide Icons\nState Management & Modals", fontsize=8, ha='center', color='#64748B')

    comp_c2 = FancyBboxPatch((37, 76), 26, 10.5, boxstyle="round,pad=0.5", facecolor='#FFFFFF', edgecolor='#93C5FD', linewidth=1)
    ax.add_patch(comp_c2)
    ax.text(50, 83.5, "Interactive Findings View", fontsize=9.5, fontweight='bold', ha='center', color='#1E293B')
    ax.text(50, 78.5, "Monaco Code Highlighter\nSeverity Badges & Filtering", fontsize=8, ha='center', color='#64748B')

    comp_c3 = FancyBboxPatch((66, 76), 26, 10.5, boxstyle="round,pad=0.5", facecolor='#FFFFFF', edgecolor='#93C5FD', linewidth=1)
    ax.add_patch(comp_c3)
    ax.text(79, 83.5, "Scan Diff & Audit Reports", fontsize=9.5, fontweight='bold', ha='center', color='#1E293B')
    ax.text(79, 78.5, "Revision Comparison Matrix\nPDF/JSON Download Client", fontsize=8, ha='center', color='#64748B')

    # Arrow Down / Up
    ax.annotate("", xy=(50, 68), xytext=(50, 74),
                arrowprops=dict(arrowstyle="<->", color="#2563EB", lw=2, mutation_scale=15))
    ax.text(50.8, 71, "HTTPS / REST API (JSON & Multipart Form-Data)", fontsize=8.5, fontweight='bold', color='#1D4ED8')

    # Tier 2: Application / API Layer
    box_api = FancyBboxPatch((5, 48), 90, 19, boxstyle="round,pad=0.8", 
                             facecolor='#F8FAFC', edgecolor='#64748B', linewidth=1.5)
    ax.add_patch(box_api)
    ax.text(8, 64.5, "APPLICATION & API GATEWAY TIER (FASTAPI ASGI)", fontsize=11, fontweight='bold', color='#0F172A')

    comp_a1 = FancyBboxPatch((8, 50), 26, 12, boxstyle="round,pad=0.5", facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=1)
    ax.add_patch(comp_a1)
    ax.text(21, 58.5, "Security & Auth Layer", fontsize=9, fontweight='bold', ha='center', color='#0F172A')
    ax.text(21, 53, "JWT Bearer Authentication\nBcrypt Passwords • CORS\nRate Limiter & Input Validation", fontsize=7.5, ha='center', color='#475569')

    comp_a2 = FancyBboxPatch((37, 50), 26, 12, boxstyle="round,pad=0.5", facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=1)
    ax.add_patch(comp_a2)
    ax.text(50, 58.5, "Upload & Extraction Guard", fontsize=9, fontweight='bold', ha='center', color='#0F172A')
    ax.text(50, 53, "Zip-Slip Path Traversal Sanitizer\nFile Type & MIME Verification\nEphemeral Sandbox Isolator", fontsize=7.5, ha='center', color='#475569')

    comp_a3 = FancyBboxPatch((66, 50), 26, 12, boxstyle="round,pad=0.5", facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=1)
    ax.add_patch(comp_a3)
    ax.text(79, 58.5, "Reporting & Diff Service", fontsize=9, fontweight='bold', ha='center', color='#0F172A')
    ax.text(79, 53, "ReportLab PDF Engine\nHistorical Scan Diff Logic\nOpenAPI Documentation Auto-Gen", fontsize=7.5, ha='center', color='#475569')

    # Arrow Down / Up
    ax.annotate("", xy=(50, 42), xytext=(50, 48),
                arrowprops=dict(arrowstyle="<->", color="#059669", lw=2, mutation_scale=15))
    ax.text(50.8, 45, "Internal Service Invocations / Worker Orchestration", fontsize=8.5, fontweight='bold', color='#047857')

    # Tier 3: Core Analysis Engine
    box_eng = FancyBboxPatch((5, 23), 90, 18.5, boxstyle="round,pad=0.8", 
                             facecolor='#ECFDF5', edgecolor='#10B981', linewidth=1.5)
    ax.add_patch(box_eng)
    ax.text(8, 39, "CORE STATIC ANALYSIS & ASSESSMENT ENGINE", fontsize=11, fontweight='bold', color='#065F46')

    comp_e1 = FancyBboxPatch((8, 25), 20, 11.5, boxstyle="round,pad=0.5", facecolor='#FFFFFF', edgecolor='#A7F3D0', linewidth=1)
    ax.add_patch(comp_e1)
    ax.text(18, 33, "Python AST Parser", fontsize=9, fontweight='bold', ha='center', color='#064E3B')
    ax.text(18, 28, "Custom NodeVisitors\neval/exec/pickle checks\nSyntax Error Detection", fontsize=7.5, ha='center', color='#047857')

    comp_e2 = FancyBboxPatch((30.5, 25), 20, 11.5, boxstyle="round,pad=0.5", facecolor='#FFFFFF', edgecolor='#A7F3D0', linewidth=1)
    ax.add_patch(comp_e2)
    ax.text(40.5, 33, "Bandit SAST Engine", fontsize=9, fontweight='bold', ha='center', color='#064E3B')
    ax.text(40.5, 28, "Security Rule Sets (B1xx-B7xx)\nSQLi, Hardcoded Secrets\nWeak Crypto & Shell Injections", fontsize=7.5, ha='center', color='#047857')

    comp_e3 = FancyBboxPatch((53, 25), 20, 11.5, boxstyle="round,pad=0.5", facecolor='#FFFFFF', edgecolor='#A7F3D0', linewidth=1)
    ax.add_patch(comp_e3)
    ax.text(63, 33, "Ruff Quality Linter", fontsize=9, fontweight='bold', ha='center', color='#064E3B')
    ax.text(63, 28, "Rust-Powered Performance\nPEP 8 & Anti-Pattern Check\nCyclomatic Complexity (C901)", fontsize=7.5, ha='center', color='#047857')

    comp_e4 = FancyBboxPatch((75.5, 25), 17, 11.5, boxstyle="round,pad=0.5", facecolor='#FFFFFF', edgecolor='#A7F3D0', linewidth=1)
    ax.add_patch(comp_e4)
    ax.text(84, 33, "Normalizer & AI", fontsize=8.5, fontweight='bold', ha='center', color='#064E3B')
    ax.text(84, 28, "Schema Unification\nSeverity Mapping\nAI Fix Suggestions", fontsize=7.2, ha='center', color='#047857')

    # Arrow Down
    ax.annotate("", xy=(50, 17.5), xytext=(50, 23),
                arrowprops=dict(arrowstyle="<->", color="#D97706", lw=2, mutation_scale=15))

    # Tier 4: Data & Persistence Tier
    box_data = FancyBboxPatch((5, 2), 90, 15, boxstyle="round,pad=0.8", 
                              facecolor='#FFFBEB', edgecolor='#F59E0B', linewidth=1.5)
    ax.add_patch(box_data)
    ax.text(8, 14.5, "DATA PERSISTENCE & STORAGE TIER", fontsize=11, fontweight='bold', color='#92400E')

    comp_d1 = FancyBboxPatch((8, 4), 38, 8.5, boxstyle="round,pad=0.5", facecolor='#FFFFFF', edgecolor='#FDE68A', linewidth=1)
    ax.add_patch(comp_d1)
    ax.text(27, 9.5, "PostgreSQL 16 Relational Database", fontsize=9, fontweight='bold', ha='center', color='#78350F')
    ax.text(27, 6, "SQLAlchemy 2.0 ORM • Alembic Migrations • Relational Integrity", fontsize=7.5, ha='center', color='#92400E')

    comp_d2 = FancyBboxPatch((52, 4), 40, 8.5, boxstyle="round,pad=0.5", facecolor='#FFFFFF', edgecolor='#FDE68A', linewidth=1)
    ax.add_patch(comp_d2)
    ax.text(72, 9.5, "Ephemeral Sandbox & Report Artifacts", fontsize=9, fontweight='bold', ha='center', color='#78350F')
    ax.text(72, 6, "Secure Temp Directory Isolation • Automated Post-Scan Purging", fontsize=7.5, ha='center', color='#92400E')

    plt.tight_layout()
    plt.savefig("figures/architecture_diagram.png", bbox_inches='tight', dpi=300)
    plt.close()
    print("Created architecture_diagram.png")

# 2. UML Use Case Diagram
def create_use_case_diagram():
    fig, ax = plt.subplots(figsize=(11, 8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 97, "UML Use Case Diagram: CodeGuard Security Platform", 
            fontsize=15, fontweight='bold', ha='center', color='#0F172A')

    # System boundary box
    sys_box = FancyBboxPatch((24, 4), 52, 90, boxstyle="square,pad=0.5", 
                             facecolor='#F8FAFC', edgecolor='#0F172A', linewidth=2)
    ax.add_patch(sys_box)
    ax.text(50, 91.5, "CodeGuard Application Boundary", fontsize=11, fontweight='bold', ha='center', color='#1E293B')

    # Actors
    # Actor 1: Developer (Left)
    ax.plot(10, 68, 'o', markersize=14, color='#1E3A8A', fillstyle='full')
    ax.plot([10, 10], [60, 68], color='#1E3A8A', lw=3)
    ax.plot([4, 16], [64, 64], color='#1E3A8A', lw=3)
    ax.plot([10, 6], [60, 52], color='#1E3A8A', lw=3)
    ax.plot([10, 14], [60, 52], color='#1E3A8A', lw=3)
    ax.text(10, 48, "Software Developer\n(Primary Actor)", fontsize=9.5, fontweight='bold', ha='center', color='#0F172A')

    # Actor 2: Security Auditor / Team Lead (Right)
    ax.plot(90, 68, 'o', markersize=14, color='#047857', fillstyle='full')
    ax.plot([90, 90], [60, 68], color='#047857', lw=3)
    ax.plot([84, 96], [64, 64], color='#047857', lw=3)
    ax.plot([90, 86], [60, 52], color='#047857', lw=3)
    ax.plot([90, 94], [60, 52], color='#047857', lw=3)
    ax.text(90, 48, "Security Auditor /\nLead Reviewer", fontsize=9.5, fontweight='bold', ha='center', color='#064E3B')

    # Use Cases (Ovals)
    use_cases = [
        ("UC-1: Register & Authenticate (JWT)", 83),
        ("UC-2: Create & Manage Projects", 73),
        ("UC-3: Upload Python Files / ZIP Archive", 63),
        ("UC-4: Trigger Multi-Engine Code Scan", 53),
        ("UC-5: View Centralized Findings Dashboard", 43),
        ("UC-6: Request AI Remediation Suggestion", 33),
        ("UC-7: Compare Scan Revisions (Scan Diff)", 23),
        ("UC-8: Update Resolution Status (FP / Fixed)", 13),
        ("UC-9: Generate & Download PDF/JSON Report", 5)
    ]

    for label, y in use_cases:
        ellipse = patches.Ellipse((50, y), 38, 6.2, facecolor='#FFFFFF', edgecolor='#2563EB', linewidth=1.5)
        ax.add_patch(ellipse)
        ax.text(50, y-0.6, label, fontsize=8.2, fontweight='bold', ha='center', color='#1E293B')

    # Association lines: Developer
    for y in [83, 73, 63, 53, 43, 33, 23, 5]:
        ax.plot([14, 31], [60, y], color='#64748B', linestyle='-', linewidth=1.2)

    # Association lines: Auditor
    for y in [83, 43, 33, 23, 13, 5]:
        ax.plot([86, 69], [60, y], color='#64748B', linestyle='-', linewidth=1.2)

    plt.tight_layout()
    plt.savefig("figures/use_case_diagram.png", bbox_inches='tight', dpi=300)
    plt.close()
    print("Created use_case_diagram.png")

# 3. UML Activity Diagram
def create_activity_diagram():
    fig, ax = plt.subplots(figsize=(10, 9), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 97.5, "UML Activity Diagram: CodeGuard Static Analysis Lifecycle", 
            fontsize=14, fontweight='bold', ha='center', color='#0F172A')

    # Start node (Black circle)
    start_circle = patches.Circle((50, 93), 2, facecolor='#0F172A', edgecolor='#0F172A')
    ax.add_patch(start_circle)

    def draw_action(text, y, h=4.5, w=50, color='#EFF6FF', border='#2563EB'):
        box = FancyBboxPatch((50 - w/2, y - h/2), w, h, boxstyle="round,pad=0.4", 
                             facecolor=color, edgecolor=border, linewidth=1.4)
        ax.add_patch(box)
        ax.text(50, y-0.5, text, fontsize=8.2, fontweight='bold', ha='center', color='#0F172A')

    def draw_decision(y, label=""):
        poly = patches.Polygon([[50, y+2.5], [55, y], [50, y-2.5], [45, y]], 
                               facecolor='#FEF3C7', edgecolor='#D97706', linewidth=1.4)
        ax.add_patch(poly)
        if label:
            ax.text(50, y-0.4, label, fontsize=7.5, fontweight='bold', ha='center', color='#78350F')

    # Sequence of steps
    ax.annotate("", xy=(50, 87), xytext=(50, 91), arrowprops=dict(arrowstyle="->", color="#0F172A", lw=1.5))
    draw_action("1. User uploads .py or .zip file with Project Context", 85)

    ax.annotate("", xy=(50, 79), xytext=(50, 82.5), arrowprops=dict(arrowstyle="->", color="#0F172A", lw=1.5))
    draw_action("2. Validate MIME type, file size (<25MB), file signature", 77)

    ax.annotate("", xy=(50, 71.5), xytext=(50, 74.5), arrowprops=dict(arrowstyle="->", color="#0F172A", lw=1.5))
    draw_decision(69, "Valid?")

    # Reject branch
    ax.annotate("", xy=(22, 69), xytext=(45, 69), arrowprops=dict(arrowstyle="->", color="#DC2626", lw=1.5))
    ax.text(32, 70.5, "[No: Invalid]", fontsize=8, fontweight='bold', color='#DC2626')
    draw_action("Abort & Return HTTP 400 Bad Request", 69, w=32, color='#FEF2F2', border='#DC2626')

    # Accept branch
    ax.annotate("", xy=(50, 62.5), xytext=(50, 66.5), arrowprops=dict(arrowstyle="->", color="#059669", lw=1.5))
    ax.text(51.5, 64.5, "[Yes]", fontsize=8, fontweight='bold', color='#059669')
    draw_action("3. Extract archive safely (Zip-Slip Traversal Guard)", 60.5)

    ax.annotate("", xy=(50, 54), xytext=(50, 58), arrowprops=dict(arrowstyle="->", color="#0F172A", lw=1.5))
    draw_action("4. Enumerate Python files & build Scan File Manifest", 52)

    # Parallel Fork Bar
    ax.annotate("", xy=(50, 46.5), xytext=(50, 49.5), arrowprops=dict(arrowstyle="->", color="#0F172A", lw=1.5))
    fork_bar = patches.Rectangle((18, 45.8), 64, 1.2, facecolor='#1E293B', edgecolor='#1E293B')
    ax.add_patch(fork_bar)
    ax.text(50, 47.5, "Parallel Execution Fork", fontsize=7.5, fontweight='bold', ha='center', color='#475569')

    # 3 Parallel Engines
    # Engine 1: AST
    ax.annotate("", xy=(26, 40), xytext=(26, 45.8), arrowprops=dict(arrowstyle="->", color="#0F172A", lw=1.5))
    box1 = FancyBboxPatch((13, 33), 26, 6.8, boxstyle="round,pad=0.3", facecolor='#F0FDF4', edgecolor='#16A34A', linewidth=1.2)
    ax.add_patch(box1)
    ax.text(26, 37.5, "5a. Python AST Engine", fontsize=8, fontweight='bold', ha='center', color='#14532D')
    ax.text(26, 34.5, "Syntax errors & unsafe builtins\n(eval, exec, insecure pickle)", fontsize=7, ha='center', color='#15803D')

    # Engine 2: Bandit
    ax.annotate("", xy=(50, 40), xytext=(50, 45.8), arrowprops=dict(arrowstyle="->", color="#0F172A", lw=1.5))
    box2 = FancyBboxPatch((38, 33), 24, 6.8, boxstyle="round,pad=0.3", facecolor='#EFF6FF', edgecolor='#2563EB', linewidth=1.2)
    ax.add_patch(box2)
    ax.text(50, 37.5, "5b. Bandit SAST", fontsize=8, fontweight='bold', ha='center', color='#1E3A8A')
    ax.text(50, 34.5, "OWASP Top 10 Python checks\nHardcoded secrets, SQLi, cmd", fontsize=7, ha='center', color='#1D4ED8')

    # Engine 3: Ruff
    ax.annotate("", xy=(74, 40), xytext=(74, 45.8), arrowprops=dict(arrowstyle="->", color="#0F172A", lw=1.5))
    box3 = FancyBboxPatch((63, 33), 24, 6.8, boxstyle="round,pad=0.3", facecolor='#FDF4FF', edgecolor='#A855F7', linewidth=1.2)
    ax.add_patch(box3)
    ax.text(75, 37.5, "5c. Ruff Linter", fontsize=8, fontweight='bold', ha='center', color='#581C87')
    ax.text(75, 34.5, "PEP 8 quality, code smells\nCyclomatic complexity (C901)", fontsize=7, ha='center', color='#7E22CE')

    # Join Bar
    join_bar = patches.Rectangle((18, 27.5), 64, 1.2, facecolor='#1E293B', edgecolor='#1E293B')
    ax.add_patch(join_bar)
    ax.annotate("", xy=(26, 27.5), xytext=(26, 33), arrowprops=dict(arrowstyle="->", color="#0F172A", lw=1.5))
    ax.annotate("", xy=(50, 27.5), xytext=(50, 33), arrowprops=dict(arrowstyle="->", color="#0F172A", lw=1.5))
    ax.annotate("", xy=(74, 27.5), xytext=(74, 33), arrowprops=dict(arrowstyle="->", color="#0F172A", lw=1.5))

    ax.annotate("", xy=(50, 22), xytext=(50, 27.5), arrowprops=dict(arrowstyle="->", color="#0F172A", lw=1.5))
    draw_action("6. Normalize Findings into Canonical Schema & Severity Mapping", 20)

    ax.annotate("", xy=(50, 13.5), xytext=(50, 17.5), arrowprops=dict(arrowstyle="->", color="#0F172A", lw=1.5))
    draw_action("7. Persist to PostgreSQL & Compute Scan Diff (New/Fixed/Recurring)", 11.5)

    ax.annotate("", xy=(50, 5.5), xytext=(50, 9), arrowprops=dict(arrowstyle="->", color="#0F172A", lw=1.5))
    draw_action("8. Render Findings on UI & Enable ReportLab PDF Generation", 4)

    plt.tight_layout()
    plt.savefig("figures/activity_diagram.png", bbox_inches='tight', dpi=300)
    plt.close()
    print("Created activity_diagram.png")

# 4. UML Sequence Diagram
def create_sequence_diagram():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 97, "UML Sequence Diagram: Code Scan Execution & Analysis Lifecycle", 
            fontsize=14, fontweight='bold', ha='center', color='#0F172A')

    # Lifeline entities
    lifelines = [
        ("User / Client", 10),
        ("React Frontend", 28),
        ("FastAPI Router", 46),
        ("Analysis Engine", 64),
        ("PostgreSQL DB", 82),
        ("Report Engine", 95)
    ]

    for name, x in lifelines:
        box = FancyBboxPatch((x-7, 88), 14, 5, boxstyle="round,pad=0.3", 
                             facecolor='#EFF6FF', edgecolor='#2563EB', linewidth=1.2)
        ax.add_patch(box)
        ax.text(x, 90.5, name, fontsize=8, fontweight='bold', ha='center', color='#1E40AF')
        ax.plot([x, x], [88, 6], color='#94A3B8', linestyle='--', linewidth=1)

    messages = [
        (83, 10, 28, "1. Select Project & Upload source/ZIP", '#0F172A'),
        (77, 28, 46, "2. POST /api/v1/scans/upload (FormData)", '#0F172A'),
        (71, 46, 64, "3. validate_and_extract_archive()", '#0F172A'),
        (65, 64, 64, "4. execute_bandit(), execute_ruff(), parse_ast()", '#2563EB'),
        (59, 64, 64, "5. normalize_findings() & map_severity()", '#2563EB'),
        (53, 64, 82, "6. persist_scan_and_findings(session)", '#059669'),
        (47, 82, 64, "7. scan_record_committed(scan_id)", '#059669'),
        (41, 64, 46, "8. return ScanSummaryResponse (DTO)", '#0F172A'),
        (35, 46, 28, "9. HTTP 201 Created (JSON Response)", '#0F172A'),
        (29, 28, 10, "10. Display Summary & Severity Metrics", '#0F172A'),
        (23, 10, 28, "11. Click 'Export PDF Audit Report'", '#7C3AED'),
        (17, 28, 46, "12. GET /api/v1/scans/{id}/report?format=pdf", '#7C3AED'),
        (11, 46, 95, "13. generate_pdf_report(scan_id)", '#7C3AED'),
        (6.5, 95, 10, "14. Binary Stream: Content-Type: application/pdf", '#059669')
    ]

    for y, x1, x2, text, col in messages:
        if x1 == x2:
            # Self call
            ax.plot([x1, x1+6, x1+6, x1], [y+2, y+2, y-1, y-1], color=col, lw=1.2)
            ax.annotate("", xy=(x1, y-1), xytext=(x1+2, y-1),
                        arrowprops=dict(arrowstyle="->", color=col, lw=1.2))
            ax.text(x1+7, y+0.5, text, fontsize=7.2, fontweight='bold', color=col)
        else:
            ax.annotate("", xy=(x2, y), xytext=(x1, y),
                        arrowprops=dict(arrowstyle="->", color=col, lw=1.2))
            mid_x = (x1 + x2) / 2
            ax.text(mid_x, y+1.2, text, fontsize=7.2, fontweight='bold', ha='center', color=col)

    plt.tight_layout()
    plt.savefig("figures/sequence_diagram.png", bbox_inches='tight', dpi=300)
    plt.close()
    print("Created sequence_diagram.png")

# 5. UML Component Diagram
def create_component_diagram():
    fig, ax = plt.subplots(figsize=(11, 7.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 97, "UML Component Diagram: CodeGuard Modular Architecture", 
            fontsize=14, fontweight='bold', ha='center', color='#0F172A')

    def draw_component(x, y, w, h, title, subtitle, color, border):
        box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3", facecolor=color, edgecolor=border, linewidth=1.3)
        ax.add_patch(box)
        # Small component tabs on left
        tab1 = patches.Rectangle((x-1.5, y+h-2.5), 3, 1.5, facecolor=color, edgecolor=border, lw=1)
        tab2 = patches.Rectangle((x-1.5, y+h-5), 3, 1.5, facecolor=color, edgecolor=border, lw=1)
        ax.add_patch(tab1)
        ax.add_patch(tab2)
        ax.text(x + w/2, y + h/2 + 1, title, fontsize=8.5, fontweight='bold', ha='center', color='#0F172A')
        ax.text(x + w/2, y + h/2 - 2, subtitle, fontsize=7.2, ha='center', color='#475569')

    # Frontend Components (Top)
    draw_component(5, 78, 26, 12, "Frontend SPA", "React 18 / TypeScript\nTailwind / Dashboard UI", "#EFF6FF", "#3B82F6")
    draw_component(37, 78, 26, 12, "Code Inspection UI", "Monaco / Syntax View\nInline Finding Markers", "#EFF6FF", "#3B82F6")
    draw_component(69, 78, 26, 12, "Report Client", "Diff Comparison View\nPDF/JSON Exporter UI", "#EFF6FF", "#3B82F6")

    # API / Controllers (Middle)
    draw_component(5, 48, 26, 12, "Auth & User Controller", "FastAPI JWT Handler\nBcrypt Passwords", "#F8FAFC", "#64748B")
    draw_component(37, 48, 26, 12, "Scan API Controller", "Upload Handler\nArchive Sanitizer", "#F8FAFC", "#64748B")
    draw_component(69, 48, 26, 12, "ReportLab Generator", "Document Builder\nVector Charts & Tables", "#F8FAFC", "#64748B")

    # Engine Core (Bottom Middle)
    draw_component(5, 18, 26, 14, "Bandit SAST Engine", "Bandit Core / AST checks\nSecurity Rule Mapping", "#ECFDF5", "#10B981")
    draw_component(37, 18, 26, 14, "Python AST Analyzer", "Syntax Error Checker\nUnsafe Builtin Detector", "#ECFDF5", "#10B981")
    draw_component(69, 18, 26, 14, "Ruff Quality Linter", "PEP 8 Linting Rules\nComplexity Engine", "#ECFDF5", "#10B981")

    # Persistence (Bottom)
    box_db = FancyBboxPatch((25, 2), 50, 10, boxstyle="round,pad=0.3", facecolor="#FFFBEB", edgecolor="#F59E0B", linewidth=1.3)
    ax.add_patch(box_db)
    ax.text(50, 7.5, "PostgreSQL 16 Relational Storage Layer", fontsize=9, fontweight='bold', ha='center', color='#78350F')
    ax.text(50, 4.5, "SQLAlchemy Models • Alembic Migrations • Relational Schema", fontsize=7.5, ha='center', color='#92400E')

    # Connections
    ax.annotate("", xy=(18, 62), xytext=(18, 76), arrowprops=dict(arrowstyle="->", color="#94A3B8", lw=1.2))
    ax.annotate("", xy=(50, 62), xytext=(50, 76), arrowprops=dict(arrowstyle="->", color="#94A3B8", lw=1.2))
    ax.annotate("", xy=(82, 62), xytext=(82, 76), arrowprops=dict(arrowstyle="->", color="#94A3B8", lw=1.2))

    ax.annotate("", xy=(18, 34), xytext=(45, 46), arrowprops=dict(arrowstyle="->", color="#10B981", lw=1.2))
    ax.annotate("", xy=(50, 34), xytext=(50, 46), arrowprops=dict(arrowstyle="->", color="#10B981", lw=1.2))
    ax.annotate("", xy=(82, 34), xytext=(55, 46), arrowprops=dict(arrowstyle="->", color="#10B981", lw=1.2))

    ax.annotate("", xy=(40, 14), xytext=(18, 16), arrowprops=dict(arrowstyle="->", color="#D97706", lw=1.2))
    ax.annotate("", xy=(50, 14), xytext=(50, 16), arrowprops=dict(arrowstyle="->", color="#D97706", lw=1.2))
    ax.annotate("", xy=(60, 14), xytext=(82, 16), arrowprops=dict(arrowstyle="->", color="#D97706", lw=1.2))

    plt.tight_layout()
    plt.savefig("figures/component_diagram.png", bbox_inches='tight', dpi=300)
    plt.close()
    print("Created component_diagram.png")

# 6. UML Deployment Diagram
def create_deployment_diagram():
    fig, ax = plt.subplots(figsize=(11, 7.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 97, "UML Deployment Diagram: Docker Containerized Infrastructure", 
            fontsize=14, fontweight='bold', ha='center', color='#0F172A')

    # Physical Host Node
    host_box = FancyBboxPatch((3, 3), 94, 91, boxstyle="square,pad=0.5", 
                              facecolor='#F8FAFC', edgecolor='#334155', linewidth=2)
    ax.add_patch(host_box)
    ax.text(6, 91, "«device» Host Machine / Production Server (Linux / Windows Host)", 
            fontsize=10.5, fontweight='bold', color='#1E293B')

    # Docker Engine Boundary
    dock_box = FancyBboxPatch((6, 6), 88, 81, boxstyle="round,pad=0.5", 
                             facecolor='#F1F5F9', edgecolor='#0284C7', linewidth=1.5, linestyle='--')
    ax.add_patch(dock_box)
    ax.text(9, 83.5, "«environment» Docker Compose Network (codeguard-network)", 
            fontsize=9.5, fontweight='bold', color='#0369A1')

    # Container 1: Frontend
    c1 = FancyBboxPatch((9, 12), 25, 68, boxstyle="round,pad=0.5", facecolor='#FFFFFF', edgecolor='#3B82F6', linewidth=1.4)
    ax.add_patch(c1)
    ax.text(21.5, 76, "«container»\ncodeguard-frontend", fontsize=9.5, fontweight='bold', ha='center', color='#1E40AF')
    ax.text(21.5, 68, "Base: node:20-alpine\nRuntime: Nginx:alpine\nExposed Port: 80 / 443", fontsize=8, ha='center', color='#475569')
    
    art1 = FancyBboxPatch((11, 20), 21, 42, boxstyle="round,pad=0.3", facecolor='#EFF6FF', edgecolor='#93C5FD', linewidth=1)
    ax.add_patch(art1)
    ax.text(21.5, 57, "«artifact»\nReact Production Bundle", fontsize=8.5, fontweight='bold', ha='center', color='#1E3A8A')
    ax.text(21.5, 47, "• HTML5 / JS / CSS\n• Tailwind Styles\n• Axios REST Client\n• React Router v6\n• Monaco Editor", fontsize=7.5, ha='center', color='#334155')
    ax.text(21.5, 25, "Client Reverse Proxy\n& SSL Termination", fontsize=7.5, fontstyle='italic', ha='center', color='#2563EB')

    # Container 2: Backend
    c2 = FancyBboxPatch((38, 12), 30, 68, boxstyle="round,pad=0.5", facecolor='#FFFFFF', edgecolor='#10B981', linewidth=1.4)
    ax.add_patch(c2)
    ax.text(53, 76, "«container»\ncodeguard-backend", fontsize=9.5, fontweight='bold', ha='center', color='#065F46')
    ax.text(53, 68, "Base: python:3.11-slim\nRuntime: Uvicorn ASGI\nExposed Port: 8000", fontsize=8, ha='center', color='#475569')

    art2 = FancyBboxPatch((40, 20), 26, 42, boxstyle="round,pad=0.3", facecolor='#ECFDF5', edgecolor='#A7F3D0', linewidth=1)
    ax.add_patch(art2)
    ax.text(53, 57, "«artifact»\nFastAPI Application Core", fontsize=8.5, fontweight='bold', ha='center', color='#064E3B')
    ax.text(53, 45, "• FastAPI Routers & JWT\n• Bandit SAST Engine\n• Ruff Quality Binary\n• Python AST Visitor\n• ReportLab PDF Service\n• Alembic Migrations", fontsize=7.5, ha='center', color='#334155')
    ax.text(53, 25, "Stateless Service Worker\nEphemeral /tmp Mount", fontsize=7.5, fontstyle='italic', ha='center', color='#059669')

    # Container 3: Database
    c3 = FancyBboxPatch((72, 12), 20, 68, boxstyle="round,pad=0.5", facecolor='#FFFFFF', edgecolor='#F59E0B', linewidth=1.4)
    ax.add_patch(c3)
    ax.text(82, 76, "«container»\ncodeguard-db", fontsize=9.5, fontweight='bold', ha='center', color='#92400E')
    ax.text(82, 68, "Base: postgres:16-alpine\nPort: 5432 (Internal)", fontsize=8, ha='center', color='#475569')

    art3 = FancyBboxPatch((73.5, 36), 17, 26, boxstyle="round,pad=0.3", facecolor='#FFFBEB', edgecolor='#FDE68A', linewidth=1)
    ax.add_patch(art3)
    ax.text(82, 57, "«database»\nPostgreSQL RDBMS", fontsize=8, fontweight='bold', ha='center', color='#78350F')
    ax.text(82, 47, "• User Credentials\n• Project Registry\n• Scans & Files\n• Unified Findings\n• Scan Diff Indices", fontsize=7, ha='center', color='#334155')

    # Persistent Volume
    vol_box = FancyBboxPatch((73.5, 16), 17, 16, boxstyle="round,pad=0.3", facecolor='#FEF3C7', edgecolor='#D97706', linewidth=1)
    ax.add_patch(vol_box)
    ax.text(82, 27, "«volume»\npostgres_data", fontsize=8, fontweight='bold', ha='center', color='#92400E')
    ax.text(82, 20, "Host persistent bind\n/var/lib/postgresql/data", fontsize=6.8, ha='center', color='#B45309')

    # Links
    ax.annotate("", xy=(38, 48), xytext=(34, 48), arrowprops=dict(arrowstyle="<->", color="#2563EB", lw=2))
    ax.text(36, 50, "HTTP", fontsize=7.5, fontweight='bold', ha='center', color='#2563EB')

    ax.annotate("", xy=(72, 48), xytext=(68, 48), arrowprops=dict(arrowstyle="<->", color="#059669", lw=2))
    ax.text(70, 50, "TCP/5432", fontsize=7.5, fontweight='bold', ha='center', color='#059669')

    plt.tight_layout()
    plt.savefig("figures/deployment_diagram.png", bbox_inches='tight', dpi=300)
    plt.close()
    print("Created deployment_diagram.png")

# 7. Database ER Diagram
def create_er_diagram():
    fig, ax = plt.subplots(figsize=(12, 8), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 97, "Entity-Relationship (ER) Diagram: CodeGuard Relational Schema", 
            fontsize=14, fontweight='bold', ha='center', color='#0F172A')

    def draw_entity(x, y, w, h, table_name, pk_list, attr_list):
        # Header
        hdr = FancyBboxPatch((x, y+h-4), w, 4, boxstyle="square,pad=0", facecolor='#1E3A8A', edgecolor='#1E3A8A')
        ax.add_patch(hdr)
        ax.text(x+w/2, y+h-2.5, table_name, fontsize=8.5, fontweight='bold', ha='center', color='#FFFFFF')
        
        # Body
        body = FancyBboxPatch((x, y), w, h-4, boxstyle="square,pad=0", facecolor='#F8FAFC', edgecolor='#CBD5E1', lw=1.2)
        ax.add_patch(body)
        
        # Text
        curr_y = y + h - 6
        for pk in pk_list:
            ax.text(x+1, curr_y, pk, fontsize=7.2, fontweight='bold', color='#B91C1C')
            curr_y -= 2.6
        for attr in attr_list:
            ax.text(x+1, curr_y, attr, fontsize=7, color='#1E293B')
            curr_y -= 2.4

    # Table 1: users
    draw_entity(4, 60, 24, 28, "users", 
                ["PK  id: UUID / Integer"], 
                ["username: VARCHAR(50)", "email: VARCHAR(100)", "hashed_password: VARCHAR", 
                 "role: VARCHAR(20)", "is_active: BOOLEAN", "created_at: TIMESTAMP", "updated_at: TIMESTAMP"])

    # Table 2: projects
    draw_entity(36, 60, 26, 28, "projects", 
                ["PK  id: UUID / Integer", "FK  user_id -> users.id"], 
                ["name: VARCHAR(100)", "description: TEXT", "repo_url: VARCHAR(255)", 
                 "created_at: TIMESTAMP", "updated_at: TIMESTAMP"])

    # Table 3: scans
    draw_entity(70, 52, 26, 36, "scans", 
                ["PK  id: UUID / Integer", "FK  project_id -> projects.id"], 
                ["scan_number: INTEGER", "status: VARCHAR(20)", "total_files: INTEGER", 
                 "total_findings: INTEGER", "critical_count: INTEGER", "high_count: INTEGER", 
                 "medium_count: INTEGER", "low_count: INTEGER", "duration_seconds: FLOAT", 
                 "scan_type: VARCHAR(20)", "created_at: TIMESTAMP"])

    # Table 4: scan_files
    draw_entity(4, 10, 25, 30, "scan_files", 
                ["PK  id: UUID / Integer", "FK  scan_id -> scans.id"], 
                ["relative_path: VARCHAR(255)", "file_size: INTEGER", "line_count: INTEGER", 
                 "sha256_hash: VARCHAR(64)", "status: VARCHAR(20)", "created_at: TIMESTAMP"])

    # Table 5: findings
    draw_entity(35, 2, 30, 44, "findings", 
                ["PK  id: UUID / Integer", "FK  scan_id -> scans.id"], 
                ["file_path: VARCHAR(255)", "line_number: INTEGER", "end_line: INTEGER", 
                 "column_number: INTEGER", "rule_id: VARCHAR(50)", "rule_name: VARCHAR(100)", 
                 "tool_source: VARCHAR(20)", "severity: VARCHAR(15)", "cwe_id: VARCHAR(20)", 
                 "description: TEXT", "code_snippet: TEXT", "status: VARCHAR(20)", 
                 "ai_explanation: TEXT", "ai_fix_suggestion: TEXT", "created_at: TIMESTAMP"])

    # Table 6: scan_comparisons
    draw_entity(72, 10, 25, 30, "scan_comparisons", 
                ["PK  id: UUID / Integer", "FK  baseline_id -> scans.id", "FK  current_id -> scans.id"], 
                ["new_findings: INTEGER", "fixed_findings: INTEGER", "recurring_findings: INTEGER", 
                 "compared_at: TIMESTAMP"])

    # Relationships Lines
    # users -> projects (1 to Many)
    ax.annotate("", xy=(36, 75), xytext=(28, 75), arrowprops=dict(arrowstyle="->", color="#1E3A8A", lw=1.5))
    ax.text(30, 76.5, "1 : N", fontsize=7.5, fontweight='bold', color='#1E3A8A')

    # projects -> scans (1 to Many)
    ax.annotate("", xy=(70, 75), xytext=(62, 75), arrowprops=dict(arrowstyle="->", color="#1E3A8A", lw=1.5))
    ax.text(64, 76.5, "1 : N", fontsize=7.5, fontweight='bold', color='#1E3A8A')

    # scans -> scan_files (1 to Many)
    ax.annotate("", xy=(16, 40), xytext=(72, 54), arrowprops=dict(arrowstyle="->", color="#059669", lw=1.2, connectionstyle="arc3,rad=-0.1"))
    ax.text(40, 48, "1 : N (Scanned Files)", fontsize=7.2, fontweight='bold', color='#059669')

    # scans -> findings (1 to Many)
    ax.annotate("", xy=(50, 46), xytext=(70, 60), arrowprops=dict(arrowstyle="->", color="#059669", lw=1.5))
    ax.text(56, 52, "1 : N (Findings)", fontsize=7.5, fontweight='bold', color='#059669')

    # scans -> scan_comparisons (1 to Many)
    ax.annotate("", xy=(84, 40), xytext=(84, 52), arrowprops=dict(arrowstyle="->", color="#7C3AED", lw=1.5))
    ax.text(85, 46, "1 : N", fontsize=7.5, fontweight='bold', color='#7C3AED')

    plt.tight_layout()
    plt.savefig("figures/er_diagram.png", bbox_inches='tight', dpi=300)
    plt.close()
    print("Created er_diagram.png")

# 8. Normalization Pipeline Diagram
def create_normalization_diagram():
    fig, ax = plt.subplots(figsize=(11, 6.5), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96, "CodeGuard Multi-Engine Finding Normalization Pipeline", 
            fontsize=14, fontweight='bold', ha='center', color='#0F172A')
    ax.text(50, 92, "Transformation from Heterogeneous Raw Tool Outputs to Canonical Schema", 
            fontsize=9.5, ha='center', color='#475569')

    # Left: 3 Raw outputs
    raw1 = FancyBboxPatch((4, 65), 26, 20, boxstyle="round,pad=0.3", facecolor='#EFF6FF', edgecolor='#3B82F6', lw=1.2)
    ax.add_patch(raw1)
    ax.text(17, 81.5, "Bandit SAST JSON", fontsize=8.5, fontweight='bold', ha='center', color='#1E40AF')
    ax.text(17, 72.5, "• test_id: 'B608'\n• issue_severity: 'HIGH'\n• issue_confidence: 'HIGH'\n• filename, line_number", fontsize=7.2, ha='center', color='#334155')

    raw2 = FancyBboxPatch((4, 38), 26, 20, boxstyle="round,pad=0.3", facecolor='#FDF4FF', edgecolor='#A855F7', lw=1.2)
    ax.add_patch(raw2)
    ax.text(17, 54.5, "Ruff Linter JSON", fontsize=8.5, fontweight='bold', ha='center', color='#6B21A8')
    ax.text(17, 45.5, "• code: 'E501', 'F401'\n• message: 'Unused import'\n• location: {row, column}\n• fix: {applicability}", fontsize=7.2, ha='center', color='#334155')

    raw3 = FancyBboxPatch((4, 11), 26, 20, boxstyle="round,pad=0.3", facecolor='#F0FDF4', edgecolor='#16A34A', lw=1.2)
    ax.add_patch(raw3)
    ax.text(17, 27.5, "Python AST Visitors", fontsize=8.5, fontweight='bold', ha='center', color='#14532D')
    ax.text(17, 18.5, "• ast.Call(func='eval')\n• SyntaxError tokens\n• Cyclomatic score > 10\n• lineno, col_offset", fontsize=7.2, ha='center', color='#334155')

    # Center: Normalization Engine
    engine_box = FancyBboxPatch((37, 20), 26, 58, boxstyle="round,pad=0.4", facecolor='#F8FAFC', edgecolor='#0F172A', lw=1.8)
    ax.add_patch(engine_box)
    ax.text(50, 74, "NORMALIZATION &\nSEVERITY MAPPER", fontsize=9.5, fontweight='bold', ha='center', color='#0F172A')
    
    rules = [
        "1. Standardize Rule IDs\n   (e.g., AST-EVAL, B608, E501)",
        "2. Severity Mapping Engine:\n   • Bandit HIGH + High Conf -> CRITICAL\n   • Bandit MED / SyntaxErr -> HIGH\n   • Ruff Errors / B-LOW -> MEDIUM\n   • Ruff Warnings/Info -> LOW",
        "3. CWE Identification Mapping\n   (CWE-89, CWE-78, CWE-95...)",
        "4. Code Snippet Extraction\n   Context lines (±2 lines)",
        "5. File Path Sanitization\n   Strip ephemeral root prefix"
    ]
    curr_y = 66
    for r in rules:
        ax.text(39, curr_y, r, fontsize=7.2, color='#1E293B')
        curr_y -= 8.5

    # Right: Unified Canonical Finding Model
    canon_box = FancyBboxPatch((70, 20), 26, 58, boxstyle="round,pad=0.4", facecolor='#ECFDF5', edgecolor='#059669', lw=1.8)
    ax.add_patch(canon_box)
    ax.text(83, 74, "CANONICAL FINDING\nDATA MODEL", fontsize=9.5, fontweight='bold', ha='center', color='#065F46')

    schema_fields = [
        "id: UUID",
        "scan_id: UUID",
        "tool_source: ToolEnum",
        "rule_id: str",
        "rule_name: str",
        "severity: SeverityEnum",
        "cwe_id: Optional[str]",
        "file_path: str",
        "line_number: int",
        "column_number: int",
        "description: str",
        "code_snippet: str",
        "status: FindingStatus",
        "ai_explanation: Optional[str]"
    ]
    curr_y = 66
    for sf in schema_fields:
        ax.text(72, curr_y, sf, fontsize=7.2, fontweight='bold', color='#064E3B')
        curr_y -= 3.2

    # Connecting arrows
    ax.annotate("", xy=(37, 75), xytext=(30, 75), arrowprops=dict(arrowstyle="->", color="#3B82F6", lw=1.5))
    ax.annotate("", xy=(37, 48), xytext=(30, 48), arrowprops=dict(arrowstyle="->", color="#A855F7", lw=1.5))
    ax.annotate("", xy=(37, 21), xytext=(30, 21), arrowprops=dict(arrowstyle="->", color="#16A34A", lw=1.5))

    ax.annotate("", xy=(70, 49), xytext=(63, 49), arrowprops=dict(arrowstyle="->", color="#059669", lw=2))

    plt.tight_layout()
    plt.savefig("figures/normalization_pipeline.png", bbox_inches='tight', dpi=300)
    plt.close()
    print("Created normalization_pipeline.png")

# 9. UI Mockup - Centralized Dashboard
def create_ui_mockup_dashboard():
    fig, ax = plt.subplots(figsize=(11, 7), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Browser window chrome
    win = FancyBboxPatch((2, 2), 96, 96, boxstyle="round,pad=0.3", facecolor='#F8FAFC', edgecolor='#94A3B8', lw=1.5)
    ax.add_patch(win)
    
    # Title bar
    bar = patches.Rectangle((2, 92), 96, 6, facecolor='#1E293B', edgecolor='#1E293B')
    ax.add_patch(bar)
    # Window dots
    ax.plot(4.5, 95, 'o', color='#EF4444', markersize=6)
    ax.plot(6.5, 95, 'o', color='#F59E0B', markersize=6)
    ax.plot(8.5, 95, 'o', color='#10B981', markersize=6)
    ax.text(50, 94.5, "CodeGuard - Security & Quality Overview: /projects/e-commerce-api/scans/4", 
            fontsize=8.5, color='#F8FAFC', ha='center', fontweight='bold')

    # Sidebar
    sidebar = patches.Rectangle((2, 2), 18, 90, facecolor='#0F172A', edgecolor='#0F172A')
    ax.add_patch(sidebar)
    ax.text(11, 86, "CodeGuard", fontsize=11, fontweight='bold', color='#38BDF8', ha='center')
    menu_items = ["Dashboard", "Projects", "Scan History", "Findings Matrix", "Diff Comparison", "PDF Reports", "Settings"]
    my = 78
    for item in menu_items:
        if item == "Dashboard":
            ax.add_patch(patches.Rectangle((3.5, my-2.5), 15, 4, facecolor='#1E293B'))
            ax.text(11, my-0.8, item, fontsize=8, fontweight='bold', color='#FFFFFF', ha='center')
        else:
            ax.text(11, my-0.8, item, fontsize=8, color='#94A3B8', ha='center')
        my -= 6.5

    # Main content header
    ax.text(23, 86, "Project: E-Commerce Backend API  •  Scan #4 (Latest)", fontsize=11, fontweight='bold', color='#0F172A')
    ax.text(23, 82.5, "Completed 2 minutes ago  |  Duration: 1.42s  |  Files Analyzed: 38 Python Modules", fontsize=7.5, color='#64748B')
    
    # Metric cards
    cards = [
        ("CRITICAL", "2", "#FEF2F2", "#DC2626"),
        ("HIGH", "5", "#FFF7ED", "#EA580C"),
        ("MEDIUM", "11", "#FEFCE8", "#CA8A04"),
        ("LOW", "24", "#EFF6FF", "#2563EB")
    ]
    cx = 23
    for title, val, bg, text_col in cards:
        c_box = FancyBboxPatch((cx, 68), 16, 11, boxstyle="round,pad=0.3", facecolor=bg, edgecolor=text_col, lw=1.2)
        ax.add_patch(c_box)
        ax.text(cx + 8, 75.5, title, fontsize=7.5, fontweight='bold', color=text_col, ha='center')
        ax.text(cx + 8, 70.5, val, fontsize=14, fontweight='bold', color=text_col, ha='center')
        cx += 18.5

    # Finding breakdown table header
    ax.text(23, 62, "Detected Vulnerabilities & Quality Issues (Active Filter: All Severities)", fontsize=9.5, fontweight='bold', color='#0F172A')
    
    tbl_hdr = patches.Rectangle((23, 54), 72, 4.5, facecolor='#1E3A8A')
    ax.add_patch(tbl_hdr)
    ax.text(25, 56, "SEVERITY", fontsize=7.5, fontweight='bold', color='#FFFFFF')
    ax.text(34, 56, "RULE ID", fontsize=7.5, fontweight='bold', color='#FFFFFF')
    ax.text(44, 56, "TOOL", fontsize=7.5, fontweight='bold', color='#FFFFFF')
    ax.text(52, 56, "FILE : LINE", fontsize=7.5, fontweight='bold', color='#FFFFFF')
    ax.text(72, 56, "VULNERABILITY DESCRIPTION", fontsize=7.5, fontweight='bold', color='#FFFFFF')
    ax.text(90, 56, "STATUS", fontsize=7.5, fontweight='bold', color='#FFFFFF')

    # Table rows
    rows = [
        ("CRITICAL", "#DC2626", "B608", "Bandit", "app/auth/routes.py : 84", "Hardcoded SQL formatting / SQL Injection", "OPEN"),
        ("CRITICAL", "#DC2626", "AST-EVAL", "AST", "utils/calc.py : 23", "Dangerous execution of untrusted input via eval()", "OPEN"),
        ("HIGH", "#EA580C", "B105", "Bandit", "config/settings.py : 12", "Hardcoded password string in variable 'DB_PASS'", "OPEN"),
        ("HIGH", "#EA580C", "B602", "Bandit", "tasks/worker.py : 45", "Subprocess execution with shell=True parameter", "OPEN"),
        ("MEDIUM", "#CA8A04", "B303", "Bandit", "security/hash.py : 19", "Insecure MD5 hashing algorithm detected", "RESOLVED"),
        ("MEDIUM", "#CA8A04", "C901", "Ruff", "services/order.py : 102", "Function 'process_order' complexity score 14 (>10)", "OPEN"),
        ("LOW", "#2563EB", "F401", "Ruff", "models/base.py : 4", "Module imported but unused: 'sys'", "OPEN")
    ]
    ry = 49.5
    for sev, scol, rid, tool, fline, desc, st in rows:
        row_bg = '#F8FAFC' if ry % 2 == 0 else '#FFFFFF'
        ax.add_patch(patches.Rectangle((23, ry-2), 72, 4.5, facecolor=row_bg, edgecolor='#E2E8F0', lw=0.5))
        
        # Badge
        badge = FancyBboxPatch((24.5, ry-1.5), 7.5, 3.2, boxstyle="round,pad=0.2", facecolor=scol)
        ax.add_patch(badge)
        ax.text(28.2, ry-0.5, sev, fontsize=6.2, fontweight='bold', color='#FFFFFF', ha='center')

        ax.text(34, ry-0.3, rid, fontsize=7, fontweight='bold', color='#0F172A')
        ax.text(44, ry-0.3, tool, fontsize=7, color='#475569')
        ax.text(52, ry-0.3, fline, fontsize=7, color='#1E40AF')
        ax.text(72, ry-0.3, desc[:38] + "...", fontsize=6.8, color='#334155')
        
        st_col = '#16A34A' if st == 'RESOLVED' else '#DC2626'
        ax.text(90, ry-0.3, st, fontsize=6.8, fontweight='bold', color=st_col)
        ry -= 4.8

    # Bottom action buttons
    btn1 = FancyBboxPatch((23, 7), 22, 5, boxstyle="round,pad=0.3", facecolor='#2563EB', edgecolor='#1D4ED8')
    ax.add_patch(btn1)
    ax.text(34, 9.5, "Export Audit Report (PDF)", fontsize=7.5, fontweight='bold', color='#FFFFFF', ha='center')

    btn2 = FancyBboxPatch((47, 7), 20, 5, boxstyle="round,pad=0.3", facecolor='#059669', edgecolor='#047857')
    ax.add_patch(btn2)
    ax.text(57, 9.5, "Export Raw JSON Findings", fontsize=7.5, fontweight='bold', color='#FFFFFF', ha='center')

    btn3 = FancyBboxPatch((69, 7), 22, 5, boxstyle="round,pad=0.3", facecolor='#475569', edgecolor='#334155')
    ax.add_patch(btn3)
    ax.text(80, 9.5, "Compare with Scan #3", fontsize=7.5, fontweight='bold', color='#FFFFFF', ha='center')

    plt.tight_layout()
    plt.savefig("figures/ui_mockup_dashboard.png", bbox_inches='tight', dpi=300)
    plt.close()
    print("Created ui_mockup_dashboard.png")

# 10. UI Mockup - Finding Detail & AI Remediation
def create_ui_mockup_findings():
    fig, ax = plt.subplots(figsize=(11, 7), dpi=300)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    win = FancyBboxPatch((2, 2), 96, 96, boxstyle="round,pad=0.3", facecolor='#F8FAFC', edgecolor='#94A3B8', lw=1.5)
    ax.add_patch(win)
    
    # Title bar
    bar = patches.Rectangle((2, 92), 96, 6, facecolor='#1E293B', edgecolor='#1E293B')
    ax.add_patch(bar)
    ax.plot(4.5, 95, 'o', color='#EF4444', markersize=6)
    ax.plot(6.5, 95, 'o', color='#F59E0B', markersize=6)
    ax.plot(8.5, 95, 'o', color='#10B981', markersize=6)
    ax.text(50, 94.5, "CodeGuard - Finding Details & AI Remediation: B608 (CWE-89)", 
            fontsize=8.5, color='#F8FAFC', ha='center', fontweight='bold')

    # Finding summary header card
    head_card = FancyBboxPatch((5, 76), 90, 13, boxstyle="round,pad=0.4", facecolor='#FEF2F2', edgecolor='#DC2626', lw=1.2)
    ax.add_patch(head_card)
    
    badge = FancyBboxPatch((7, 83), 11, 4.5, boxstyle="round,pad=0.2", facecolor='#DC2626')
    ax.add_patch(badge)
    ax.text(12.5, 84.8, "CRITICAL", fontsize=7.5, fontweight='bold', color='#FFFFFF', ha='center')

    ax.text(20, 86, "Rule: B608 - Possible SQL Injection vector via string formatting", fontsize=10, fontweight='bold', color='#991B1B')
    ax.text(20, 82.5, "File: app/auth/routes.py  |  Line: 84  |  Tool: Bandit SAST Engine  |  CWE: CWE-89 (Improper Neutralization)", fontsize=7.5, color='#7F1D1D')
    ax.text(20, 78.5, "Status: OPEN  |  Confidence: HIGH  |  Detected: 2026-11-02 14:22:10 UTC", fontsize=7.2, color='#991B1B')

    # Code snippet viewer (Left)
    code_box = FancyBboxPatch((5, 12), 43, 61, boxstyle="round,pad=0.4", facecolor='#0F172A', edgecolor='#334155', lw=1.2)
    ax.add_patch(code_box)
    ax.text(26.5, 69, "SOURCE CODE CONTEXT (± 2 Lines)", fontsize=8, fontweight='bold', color='#38BDF8', ha='center')

    lines = [
        ("82", "  def authenticate_user(username, password):", '#94A3B8'),
        ("83", "      # Dynamic query construction", '#64748B'),
        ("84", ">>>   query = f\"SELECT * FROM users WHERE u='{username}'\"", '#EF4444'),
        ("85", "      cursor.execute(query)", '#CBD5E1'),
        ("86", "      user = cursor.fetchone()", '#94A3B8'),
        ("87", "      if not user:", '#94A3B8'),
        ("88", "          return None", '#94A3B8')
    ]
    cy = 63
    for lno, ctext, ccol in lines:
        if ">>>" in ctext:
            ax.add_patch(patches.Rectangle((6, cy-1.8), 41, 4.5, facecolor='#450A0A'))
        ax.text(7, cy, lno, fontsize=7.2, fontweight='bold', color='#64748B')
        ax.text(11, cy, ctext, fontsize=7, fontfamily='monospace', fontweight='bold' if ">>>" in ctext else 'normal', color=ccol)
        cy -= 6

    # AI Remediation and Fix Advice (Right)
    ai_box = FancyBboxPatch((51, 12), 44, 61, boxstyle="round,pad=0.4", facecolor='#F0FDF4', edgecolor='#16A34A', lw=1.2)
    ax.add_patch(ai_box)
    ax.text(73, 69, "AI-ASSISTED REMEDIATION & FIX SUGGESTION", fontsize=8, fontweight='bold', color='#14532D', ha='center')

    ax.text(53, 64, "Root Cause Analysis:", fontsize=8, fontweight='bold', color='#166534')
    ax.text(53, 56.5, "Direct f-string concatenation in raw SQL statements\nallows an attacker to inject arbitrary SQL statements\n(e.g., ' OR '1'='1), completely bypassing login.", fontsize=7.2, color='#14532D')

    ax.text(53, 50, "Recommended Fix (Parameterized Query):", fontsize=8, fontweight='bold', color='#166534')

    fix_box = FancyBboxPatch((53, 26), 40, 21, boxstyle="round,pad=0.3", facecolor='#0F172A', edgecolor='#22C55E')
    ax.add_patch(fix_box)
    fix_lines = [
        ("# Secure Implementation using Bind Parameters", '#64748B'),
        ("query = \"\"\"", '#CBD5E1'),
        ("    SELECT id, username, hashed_pw", '#CBD5E1'),
        ("    FROM users WHERE username = :u", '#22C55E'),
        ("\"\"\"", '#CBD5E1'),
        ("cursor.execute(query, {'u': username})", '#22C55E')
    ]
    f_y = 43
    for fl, fc in fix_lines:
        ax.text(55, f_y, fl, fontsize=6.8, fontfamily='monospace', color=fc)
        f_y -= 3.2

    ax.text(53, 21, "OWASP Reference: OWASP Top 10 - A03:2021-Injection", fontsize=7, color='#15803D')
    ax.text(53, 16, "CWE Reference: CWE-89 SQL Command Neutralization", fontsize=7, color='#15803D')

    # Bottom Bar buttons
    btn_resolve = FancyBboxPatch((51, 4), 20, 5.5, boxstyle="round,pad=0.3", facecolor='#16A34A', edgecolor='#15803D')
    ax.add_patch(btn_resolve)
    ax.text(61, 6.8, "Mark as Resolved", fontsize=7.5, fontweight='bold', color='#FFFFFF', ha='center')

    btn_fp = FancyBboxPatch((74, 4), 21, 5.5, boxstyle="round,pad=0.3", facecolor='#DC2626', edgecolor='#B91C1C')
    ax.add_patch(btn_fp)
    ax.text(84.5, 6.8, "Mark as False Positive", fontsize=7.5, fontweight='bold', color='#FFFFFF', ha='center')

    plt.tight_layout()
    plt.savefig("figures/ui_mockup_findings.png", bbox_inches='tight', dpi=300)
    plt.close()
    print("Created ui_mockup_findings.png")

if __name__ == "__main__":
    create_architecture_diagram()
    create_use_case_diagram()
    create_activity_diagram()
    create_sequence_diagram()
    create_component_diagram()
    create_deployment_diagram()
    create_er_diagram()
    create_normalization_diagram()
    create_ui_mockup_dashboard()
    create_ui_mockup_findings()
    print("All 10 diagrams successfully generated!")
