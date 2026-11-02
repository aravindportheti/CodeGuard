import time
import os
from report_styles import init_document
from report_sections_part1 import build_part1
from report_sections_part2 import build_part2
from report_sections_part3 import build_part3
from report_sections_part4 import build_part4
from report_sections_part5 import build_part5

def generate_full_report():
    print("=" * 70)
    print("CodeGuard: Building Complete Internship Project Report (DOCX)")
    print("=" * 70)
    
    start_time = time.time()
    
    # Step 1: Initialize document and styles
    print("[1/6] Initializing document margins, typography, headers & footers...")
    doc = init_document()
    
    # Step 2: Part 1 (Sections 1 - 10)
    print("[2/6] Compiling Part 1: Cover Page, Certificate, Declaration, Acknowledgement, Abstract, TOC, Intro, Problem, Existing, Proposed...")
    build_part1(doc)
    
    # Step 3: Part 2 (Sections 11 - 16)
    print("[3/6] Compiling Part 2: Objectives & Scope, Feasibility, Requirements, Tech Stack, Architecture, UML Diagrams...")
    build_part2(doc)
    
    # Step 4: Part 3 (Sections 17 - 21)
    print("[4/6] Compiling Part 3: Database Design & ER, Module Descriptions, Workflows & Algorithms, Implementation, REST API Docs...")
    build_part3(doc)
    
    # Step 5: Part 4 (Sections 22 - 26)
    print("[5/6] Compiling Part 4: UI Design, Security & Privacy, Testing Methodology & Cases, Performance, Results & Discussion...")
    build_part4(doc)
    
    # Step 6: Part 5 (Sections 27 - 32)
    print("[6/6] Compiling Part 5: Limitations, Future Enhancements, Conclusion, References, Appendices, Technical Viva Q&A...")
    build_part5(doc)
    
    output_filename = "CodeGuard_Internship_Project_Report.docx"
    print(f"Saving compiled report to '{output_filename}'...")
    doc.save(output_filename)
    
    duration = time.time() - start_time
    file_size_mb = os.path.getsize(output_filename) / (1024 * 1024)
    print("=" * 70)
    print(f"SUCCESS: Report generated successfully in {duration:.2f} seconds!")
    print(f"File Name: {output_filename}")
    print(f"File Size: {file_size_mb:.2f} MB")
    print("=" * 70)

if __name__ == "__main__":
    generate_full_report()
