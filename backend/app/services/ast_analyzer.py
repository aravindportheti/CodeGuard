import ast
from typing import List, Dict, Any, Optional

class FunctionComplexityVisitor(ast.NodeVisitor):
    def __init__(self):
        self.complexity = 1  # Base complexity is 1

    def visit_If(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_For(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_AsyncFor(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_ExceptHandler(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_With(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_AsyncWith(self, node):
        self.complexity += 1
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        self.complexity += len(node.values) - 1
        self.generic_visit(node)

    def visit_Assert(self, node):
        self.complexity += 1
        self.generic_visit(node)


class CodeGuardASTVisitor(ast.NodeVisitor):
    def __init__(self, relative_path: str):
        self.relative_path = relative_path
        self.findings: List[Dict[str, Any]] = []

    def visit_Call(self, node: ast.Call):
        # 1. Direct dangerous builtins: eval(), exec(), compile()
        if isinstance(node.func, ast.Name):
            fname = node.func.id
            if fname in {"eval", "exec"}:
                self.findings.append({
                    "tool_source": "AST",
                    "rule_id": f"AST-{fname.upper()}",
                    "rule_name": f"Dangerous Code Execution via {fname}()",
                    "severity": "CRITICAL",
                    "cwe_id": "CWE-95",
                    "file_path": self.relative_path,
                    "line_number": node.lineno,
                    "column_number": node.col_offset,
                    "description": f"Use of built-in '{fname}()' detected. Untrusted input passed to {fname}() enables remote code execution."
                })
            elif fname in {"compile", "__import__"}:
                self.findings.append({
                    "tool_source": "AST",
                    "rule_id": f"AST-{fname.upper().replace('_', '')}",
                    "rule_name": f"Dynamic Code Evaluation via {fname}()",
                    "severity": "HIGH",
                    "cwe_id": "CWE-95",
                    "file_path": self.relative_path,
                    "line_number": node.lineno,
                    "column_number": node.col_offset,
                    "description": f"Dynamic code loading with '{fname}()' poses security risks if expressions are derived from untrusted input."
                })

        # 2. Insecure deserialization: pickle.loads(), pickle.load()
        elif isinstance(node.func, ast.Attribute):
            attr_name = node.func.attr
            if attr_name in {"loads", "load"}:
                if isinstance(node.func.value, ast.Name) and node.func.value.id == "pickle":
                    self.findings.append({
                        "tool_source": "AST",
                        "rule_id": "AST-PICKLE-INSECURE",
                        "rule_name": "Insecure Deserialization via pickle",
                        "severity": "CRITICAL",
                        "cwe_id": "CWE-502",
                        "file_path": self.relative_path,
                        "line_number": node.lineno,
                        "column_number": node.col_offset,
                        "description": "Insecure deserialization using 'pickle' detected. Deserializing untrusted byte streams leads to arbitrary code execution."
                    })
            
            # 3. Insecure PyYAML loading
            if attr_name == "load" and isinstance(node.func.value, ast.Name) and node.func.value.id == "yaml":
                # Check if Loader=yaml.SafeLoader is provided
                has_safe_loader = any(kw.arg == "Loader" and "Safe" in ast.dump(kw.value) for kw in node.keywords)
                if not has_safe_loader:
                    self.findings.append({
                        "tool_source": "AST",
                        "rule_id": "AST-YAML-UNSAFE",
                        "rule_name": "Unsafe YAML Parsing",
                        "severity": "HIGH",
                        "cwe_id": "CWE-502",
                        "file_path": self.relative_path,
                        "line_number": node.lineno,
                        "column_number": node.col_offset,
                        "description": "Unsafe yaml.load() call without SafeLoader. Use yaml.safe_load() to prevent arbitrary object instantiation."
                    })

            # 4. Insecure cryptographic algorithms: hashlib.md5, hashlib.sha1
            if attr_name in {"md5", "sha1"} and isinstance(node.func.value, ast.Name) and node.func.value.id == "hashlib":
                self.findings.append({
                    "tool_source": "AST",
                    "rule_id": f"AST-WEAK-HASH-{attr_name.upper()}",
                    "rule_name": f"Weak Cryptographic Hash: {attr_name.upper()}",
                    "severity": "MEDIUM",
                    "cwe_id": "CWE-328",
                    "file_path": self.relative_path,
                    "line_number": node.lineno,
                    "column_number": node.col_offset,
                    "description": f"Use of cryptographically weak algorithm '{attr_name.upper()}' detected. MD5 and SHA1 are susceptible to collision attacks."
                })

        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign):
        # Detect hardcoded secret variables
        for target in node.targets:
            if isinstance(target, ast.Name):
                var_name = target.id.lower()
                suspicious_names = {"password", "passwd", "secret_key", "api_key", "access_token", "private_key"}
                if any(s in var_name for s in suspicious_names):
                    if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                        val_str = node.value.value
                        if len(val_str) > 3 and not val_str.startswith("env:") and not val_str.startswith("$"):
                            self.findings.append({
                                "tool_source": "AST",
                                "rule_id": "AST-HARDCODED-SECRET",
                                "rule_name": "Hardcoded Credential / Secret in Source",
                                "severity": "HIGH",
                                "cwe_id": "CWE-798",
                                "file_path": self.relative_path,
                                "line_number": node.lineno,
                                "column_number": node.col_offset,
                                "description": f"Potential hardcoded secret or credential assigned to variable '{target.id}'. Use environment variables instead."
                            })
        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef):
        # Calculate Cyclomatic Complexity
        sub_visitor = FunctionComplexityVisitor()
        for stmt in node.body:
            sub_visitor.visit(stmt)

        if sub_visitor.complexity > 10:
            self.findings.append({
                "tool_source": "AST",
                "rule_id": "AST-COMPLEXITY-C901",
                "rule_name": f"High Cyclomatic Complexity in '{node.name}'",
                "severity": "MEDIUM",
                "cwe_id": "CWE-1007",
                "file_path": self.relative_path,
                "line_number": node.lineno,
                "column_number": node.col_offset,
                "description": f"Function '{node.name}' has a McCabe cyclomatic complexity score of {sub_visitor.complexity} (threshold: 10). Consider modular refactoring."
            })
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        sub_visitor = FunctionComplexityVisitor()
        for stmt in node.body:
            sub_visitor.visit(stmt)

        if sub_visitor.complexity > 10:
            self.findings.append({
                "tool_source": "AST",
                "rule_id": "AST-COMPLEXITY-C901",
                "rule_name": f"High Cyclomatic Complexity in async '{node.name}'",
                "severity": "MEDIUM",
                "cwe_id": "CWE-1007",
                "file_path": self.relative_path,
                "line_number": node.lineno,
                "column_number": node.col_offset,
                "description": f"Async function '{node.name}' has a McCabe cyclomatic complexity of {sub_visitor.complexity} (threshold: 10)."
            })
        self.generic_visit(node)


def analyze_file_ast(relative_path: str, full_path: str) -> List[Dict[str, Any]]:
    """
    Parses a single Python file into an Abstract Syntax Tree.
    Detects syntax errors, dangerous builtins, insecure deserialization, and high complexity.
    NEVER executes the code.
    """
    try:
        with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
            source = f.read()
    except Exception as e:
        return [{
            "tool_source": "AST",
            "rule_id": "AST-FILE-READ-ERROR",
            "rule_name": "File Read Error",
            "severity": "HIGH",
            "cwe_id": "CWE-703",
            "file_path": relative_path,
            "line_number": 1,
            "column_number": 0,
            "description": f"Unable to read file: {str(e)}"
        }]

    try:
        tree = ast.parse(source, filename=relative_path)
    except SyntaxError as se:
        return [{
            "tool_source": "AST",
            "rule_id": "AST-SYNTAX-ERROR",
            "rule_name": "Python Syntax Error",
            "severity": "HIGH",
            "cwe_id": "CWE-398",
            "file_path": relative_path,
            "line_number": se.lineno or 1,
            "column_number": se.offset or 0,
            "description": f"Fatal syntax error: {se.msg} at line {se.lineno}, offset {se.offset}."
        }]

    visitor = CodeGuardASTVisitor(relative_path)
    visitor.visit(tree)
    return visitor.findings
