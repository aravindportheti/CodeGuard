import os
import unittest
import tempfile
import sys

# Ensure backend root is in PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.services.ast_analyzer import analyze_file_ast
from app.services.bandit_scanner import run_bandit_scan
from app.services.ruff_scanner import run_ruff_scan
from app.services.normalizer import normalize_all_findings
from app.services.diff_engine import compute_scan_diff

class TestCodeGuardScanners(unittest.TestCase):
    def setUp(self):
        self.workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

    def test_ast_analyzer_on_vulnerable_app(self):
        sample_path = os.path.join(self.workspace_root, "samples", "vulnerable_app.py")
        self.assertTrue(os.path.exists(sample_path), f"File {sample_path} does not exist")
        
        findings = analyze_file_ast("vulnerable_app.py", sample_path)
        rule_ids = {f["rule_id"] for f in findings}
        
        self.assertIn("AST-EVAL", rule_ids)
        self.assertIn("AST-PICKLE-INSECURE", rule_ids)
        self.assertIn("AST-WEAK-HASH-MD5", rule_ids)

    def test_ast_analyzer_on_safe_calculator(self):
        sample_path = os.path.join(self.workspace_root, "samples", "safe_calculator.py")
        self.assertTrue(os.path.exists(sample_path))
        
        findings = analyze_file_ast("safe_calculator.py", sample_path)
        critical_findings = [f for f in findings if f["severity"] in {"CRITICAL", "HIGH"}]
        self.assertEqual(len(critical_findings), 0)

    def test_normalization_pipeline(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            test_file = os.path.join(temp_dir, "test.py")
            with open(test_file, "w") as f:
                f.write("def bad():\n    eval('1+1')\n")
                
            ast_f = analyze_file_ast("test.py", test_file)
            normalized = normalize_all_findings(temp_dir, ast_f, [], [])
            self.assertTrue(len(normalized) > 0)
            self.assertEqual(normalized[0]["severity"], "CRITICAL")
            self.assertIsNotNone(normalized[0]["code_snippet"])

if __name__ == "__main__":
    unittest.main()
