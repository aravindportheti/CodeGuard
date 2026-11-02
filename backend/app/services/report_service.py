import io
import json
from typing import List, Dict, Any
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from app.models.scan import Scan
from app.models.finding import Finding
from app.models.project import Project

def generate_pdf_report(project: Project, scan: Scan, findings: List[Finding]) -> bytes:
    """
    Generates a publication-quality vector PDF audit report using ReportLab.
    """
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    
    # Custom Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#1E3A8A'),
        spaceAfter=6
    )

    sub_style = ParagraphStyle(
        'DocSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#475569'),
        spaceAfter=14
    )

    h2_style = ParagraphStyle(
        'DocH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#1E3A8A'),
        spaceBefore=12,
        spaceAfter=8
    )

    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#1E293B')
    )

    code_style = ParagraphStyle(
        'DocCode',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor('#0F172A')
    )

    story = []

    # Title & Header
    story.append(Paragraph("CodeGuard Security & Quality Audit Report", title_style))
    scan_date_str = scan.created_at.strftime("%Y-%m-%d %H:%M:%S UTC") if scan.created_at else "N/A"
    story.append(Paragraph(
        f"<b>Project:</b> {project.name} &nbsp;|&nbsp; <b>Scan ID:</b> #{scan.id} &nbsp;|&nbsp; <b>Scan Date:</b> {scan_date_str}",
        sub_style
    ))
    story.append(Spacer(1, 8))

    # Executive Summary Table
    story.append(Paragraph("1. Executive Summary & Scan Metrics", h2_style))
    summary_data = [
        ["Total Files Scanned", f"{scan.total_files} Modules", "Scan Duration", f"{scan.duration_seconds:.2f} s"],
        ["Total Detected Issues", f"{scan.total_findings}", "Status", f"{scan.status}"],
        ["Critical Severity", f"{scan.critical_count}", "High Severity", f"{scan.high_count}"],
        ["Medium Severity", f"{scan.medium_count}", "Low / Style Severity", f"{scan.low_count}"]
    ]

    t_summary = Table(summary_data, colWidths=[130, 140, 130, 140])
    t_summary.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F8FAFC')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#1E293B')),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold'),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_summary)
    story.append(Spacer(1, 14))

    # Findings Detail Section
    story.append(Paragraph("2. Detailed Vulnerabilities & Code Quality Findings", h2_style))

    if not findings:
        story.append(Paragraph("No security vulnerabilities or code quality issues were identified in this scan. Codebase passed all checks.", body_style))
    else:
        # Table of Findings
        findings_table_data = [
            ["Severity", "Rule ID", "Tool", "File & Line", "Description"]
        ]

        sev_colors = {
            "CRITICAL": colors.HexColor('#DC2626'),
            "HIGH": colors.HexColor('#EA580C'),
            "MEDIUM": colors.HexColor('#CA8A04'),
            "LOW": colors.HexColor('#2563EB')
        }

        for idx, f in enumerate(findings[:50]):  # Cap at top 50 in table for optimal document rendering
            f_line = f"{f.file_path}:{f.line_number}"
            # Shorten description if too long
            desc_text = f.description if len(f.description) < 140 else f.description[:137] + "..."
            findings_table_data.append([
                f.severity,
                f.rule_id,
                f.tool_source,
                Paragraph(f_line, code_style),
                Paragraph(desc_text, body_style)
            ])

        t_findings = Table(findings_table_data, colWidths=[65, 75, 55, 145, 200])
        t_findings.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E3A8A')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 8.5),
            ('ALIGN', (0, 0), (-1, 0), 'LEFT'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
            ('TOPPADDING', (0, 0), (-1, 0), 6),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8FAFC')]),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
            ('TOPPADDING', (0, 1), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 4),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('FONTSIZE', (0, 1), (-1, -1), 8),
        ]))
        story.append(t_findings)

    # Remediation Notes Section
    story.append(Spacer(1, 14))
    story.append(Paragraph("3. Remediation & Action Items", h2_style))
    remediation_intro = Paragraph(
        "Critical and High severity issues must be addressed before deployment. "
        "Ensure all raw database queries use parameterized placeholders, replace dynamic eval/exec builtins with "
        "type-safe parsers, and externalize all hardcoded credentials to environment variables.",
        body_style
    )
    story.append(remediation_intro)

    doc.build(story)
    pdf_bytes = buffer.getvalue()
    buffer.close()
    return pdf_bytes


def generate_json_report(project: Project, scan: Scan, findings: List[Finding]) -> Dict[str, Any]:
    """
    Serializes scan findings and metadata into a comprehensive JSON report.
    """
    return {
        "report_type": "CodeGuard_Audit_Report",
        "generated_at": scan.created_at.isoformat() if scan.created_at else None,
        "project": {
            "id": project.id,
            "name": project.name,
            "description": project.description,
            "repo_url": project.repo_url
        },
        "scan": {
            "id": scan.id,
            "scan_number": scan.scan_number,
            "status": scan.status,
            "duration_seconds": scan.duration_seconds,
            "total_files": scan.total_files,
            "total_findings": scan.total_findings,
            "metrics": {
                "critical": scan.critical_count,
                "high": scan.high_count,
                "medium": scan.medium_count,
                "low": scan.low_count
            }
        },
        "findings": [
            {
                "id": f.id,
                "tool_source": f.tool_source,
                "rule_id": f.rule_id,
                "rule_name": f.rule_name,
                "severity": f.severity,
                "cwe_id": f.cwe_id,
                "file_path": f.file_path,
                "line_number": f.line_number,
                "end_line": f.end_line,
                "column_number": f.column_number,
                "description": f.description,
                "code_snippet": f.code_snippet,
                "status": f.status,
                "ai_explanation": f.ai_explanation
            }
            for f in findings
        ]
    }
