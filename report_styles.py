import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

# Color Palette Constants
HEX_PRIMARY = "1E3A8A"      # Deep Navy
HEX_SECONDARY = "2563EB"    # Slate Blue
HEX_ACCENT = "0D9488"       # Teal
HEX_DARK_TEXT = "1E293B"    # Charcoal
HEX_MUTED_TEXT = "64748B"   # Muted Gray
HEX_BG_LIGHT = "F8FAFC"     # Off-white / light slate
HEX_BORDER = "CBD5E1"       # Light gray border

COLOR_PRIMARY = RGBColor(30, 58, 138)
COLOR_SECONDARY = RGBColor(37, 99, 235)
COLOR_DARK_TEXT = RGBColor(30, 41, 59)
COLOR_MUTED = RGBColor(100, 116, 139)

def init_document():
    doc = docx.Document()
    
    # Configure 1-inch margins
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.page_width = Inches(8.5)
        section.page_height = Inches(11.0)
        
        # Setup Header
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("CodeGuard: Source Code Quality & Vulnerability Detection Platform")
        hrun.font.name = "Calibri"
        hrun.font.size = Pt(8.5)
        hrun.font.italic = True
        hrun.font.color.rgb = COLOR_MUTED
        
        # Setup Footer
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        frun1 = fp.add_run("Academic Internship Project Report | Advanced Python Development")
        frun1.font.name = "Calibri"
        frun1.font.size = Pt(8.5)
        frun1.font.color.rgb = COLOR_MUTED
        
        # Add tab and page number
        frun2 = fp.add_run("\t\tPage ")
        frun2.font.name = "Calibri"
        frun2.font.size = Pt(8.5)
        frun2.font.color.rgb = COLOR_MUTED
        
        # Add XML Page Field
        fld1 = OxmlElement('w:fldChar')
        fld1.set(qn('w:fldCharType'), 'begin')
        instr = OxmlElement('w:instrText')
        instr.set(qn('xml:space'), 'preserve')
        instr.text = "PAGE"
        fld2 = OxmlElement('w:fldChar')
        fld2.set(qn('w:fldCharType'), 'separate')
        fld3 = OxmlElement('w:fldChar')
        fld3.set(qn('w:fldCharType'), 'end')
        fp.add_run()._r.extend([fld1, instr, fld2, fld3])
        
    return doc

def add_heading_1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.color.rgb = COLOR_PRIMARY
    return p

def add_heading_2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.color.rgb = COLOR_SECONDARY
    return p

def add_heading_3(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(11)
    run.font.bold = True
    run.font.color.rgb = COLOR_DARK_TEXT
    return p

def add_paragraph(doc, text, bold_prefix=None, italic_prefix=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.line_spacing = 1.15
    
    if bold_prefix:
        brun = p.add_run(bold_prefix)
        brun.font.name = "Calibri"
        brun.font.size = Pt(10.5)
        brun.font.bold = True
        brun.font.color.rgb = COLOR_DARK_TEXT
        
    if italic_prefix:
        irun = p.add_run(italic_prefix)
        irun.font.name = "Calibri"
        irun.font.size = Pt(10.5)
        irun.font.italic = True
        irun.font.color.rgb = COLOR_DARK_TEXT

    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(10.5)
    run.font.color.rgb = COLOR_DARK_TEXT
    return p

def add_bullet(doc, text, bold_prefix=None):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.15
    
    if bold_prefix:
        brun = p.add_run(bold_prefix)
        brun.font.name = "Calibri"
        brun.font.size = Pt(10.5)
        brun.font.bold = True
        brun.font.color.rgb = COLOR_DARK_TEXT

    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(10.5)
    run.font.color.rgb = COLOR_DARK_TEXT
    return p

def add_callout(doc, text, title="NOTE / BEST PRACTICE", callout_type="info"):
    bg_color = "EFF6FF" if callout_type == "info" else ("ECFDF5" if callout_type == "success" else "FEF2F2")
    border_color = "2563EB" if callout_type == "info" else ("059669" if callout_type == "success" else "DC2626")
    
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    
    # Set cell shading
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_color}"/>'))
    
    # Left border only (thick accent line)
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="none"/>
            <w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/>
            <w:bottom w:val="none"/>
            <w:right w:val="none"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)
    
    # Inner padding
    margins = parse_xml(f'''
        <w:tcMar {nsdecls("w")}>
            <w:top w:w="120" w:type="dxa"/>
            <w:bottom w:w="120" w:type="dxa"/>
            <w:left w:w="180" w:type="dxa"/>
            <w:right w:w="180" w:type="dxa"/>
        </w:tcMar>
    ''')
    tcPr.append(margins)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    
    trun = p.add_run(f"[{title}] ")
    trun.font.name = "Calibri"
    trun.font.size = Pt(9.5)
    trun.font.bold = True
    trun.font.color.rgb = COLOR_PRIMARY if callout_type == "info" else (RGBColor(5, 150, 105) if callout_type == "success" else RGBColor(220, 38, 38))
    
    crun = p.add_run(text)
    crun.font.name = "Calibri"
    crun.font.size = Pt(9.5)
    crun.font.color.rgb = COLOR_DARK_TEXT
    
    # Add trailing space after callout table
    sp = doc.add_paragraph()
    sp.paragraph_format.space_before = Pt(0)
    sp.paragraph_format.space_after = Pt(4)

def add_code_block(doc, code_str, caption=None):
    if caption:
        cp = doc.add_paragraph()
        cp.paragraph_format.space_before = Pt(6)
        cp.paragraph_format.space_after = Pt(2)
        cprun = cp.add_run(caption)
        cprun.font.name = "Calibri"
        cprun.font.size = Pt(9.5)
        cprun.font.bold = True
        cprun.font.color.rgb = COLOR_SECONDARY

    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="0F172A"/>')) # Dark IDE theme
    
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="6" w:space="0" w:color="334155"/>
            <w:left w:val="single" w:sz="18" w:space="0" w:color="38BDF8"/>
            <w:bottom w:val="single" w:sz="6" w:space="0" w:color="334155"/>
            <w:right w:val="single" w:sz="6" w:space="0" w:color="334155"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)
    
    margins = parse_xml(f'''
        <w:tcMar {nsdecls("w")}>
            <w:top w:w="120" w:type="dxa"/>
            <w:bottom w:w="120" w:type="dxa"/>
            <w:left w:w="160" w:type="dxa"/>
            <w:right w:w="160" w:type="dxa"/>
        </w:tcMar>
    ''')
    tcPr.append(margins)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.05
    
    crun = p.add_run(code_str.strip())
    crun.font.name = "Consolas"
    crun.font.size = Pt(8.5)
    crun.font.color.rgb = RGBColor(241, 245, 249) # Light text
    
    sp = doc.add_paragraph()
    sp.paragraph_format.space_before = Pt(0)
    sp.paragraph_format.space_after = Pt(5)

def add_figure(doc, image_path, caption_text, width_inches=6.2):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run()
    run.add_picture(image_path, width=Inches(width_inches))
    
    cp = doc.add_paragraph()
    cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cp.paragraph_format.space_before = Pt(0)
    cp.paragraph_format.space_after = Pt(10)
    crun = cp.add_run(caption_text)
    crun.font.name = "Calibri"
    crun.font.size = Pt(9.5)
    crun.font.italic = True
    crun.font.bold = True
    crun.font.color.rgb = COLOR_MUTED

def create_styled_table(doc, headers, rows_data, col_widths=None):
    tbl = doc.add_table(rows=len(rows_data) + 1, cols=len(headers))
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Table border XML
    tblPr = tbl._tbl.tblPr
    tblBorders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="6" w:space="0" w:color="CBD5E1"/>
            <w:bottom w:val="single" w:sz="8" w:space="0" w:color="1E3A8A"/>
            <w:left w:val="none"/>
            <w:right w:val="none"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(tblBorders)
    
    # Format Header Row
    hdr_row = tbl.rows[0]
    for idx, heading in enumerate(headers):
        cell = hdr_row.cells[idx]
        tcPr = cell._tc.get_or_add_tcPr()
        tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="1E3A8A"/>'))
        
        # Margins
        margins = parse_xml(f'''
            <w:tcMar {nsdecls("w")}>
                <w:top w:w="120" w:type="dxa"/>
                <w:bottom w:w="120" w:type="dxa"/>
                <w:left w:w="140" w:type="dxa"/>
                <w:right w:w="140" w:type="dxa"/>
            </w:tcMar>
        ''')
        tcPr.append(margins)
        
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(heading)
        run.font.name = "Calibri"
        run.font.size = Pt(9.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(255, 255, 255)
        
    # Format Data Rows
    for r_idx, row_values in enumerate(rows_data):
        row = tbl.rows[r_idx + 1]
        bg_fill = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(row_values):
            cell = row.cells[c_idx]
            tcPr = cell._tc.get_or_add_tcPr()
            if bg_fill != "FFFFFF":
                tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_fill}"/>'))
                
            margins = parse_xml(f'''
                <w:tcMar {nsdecls("w")}>
                    <w:top w:w="100" w:type="dxa"/>
                    <w:bottom w:w="100" w:type="dxa"/>
                    <w:left w:w="140" w:type="dxa"/>
                    <w:right w:w="140" w:type="dxa"/>
                </w:tcMar>
            ''')
            tcPr.append(margins)
            
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.1
            run = p.add_run(str(val))
            run.font.name = "Calibri"
            run.font.size = Pt(9)
            run.font.color.rgb = COLOR_DARK_TEXT
            
    # Set explicit column widths if provided
    if col_widths:
        for row in tbl.rows:
            for idx, width in enumerate(col_widths):
                row.cells[idx].width = Inches(width)

    # Trailing spacing
    sp = doc.add_paragraph()
    sp.paragraph_format.space_before = Pt(0)
    sp.paragraph_format.space_after = Pt(6)
    return tbl

def add_page_break(doc):
    doc.add_page_break()
