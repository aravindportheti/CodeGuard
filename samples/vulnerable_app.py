"""
Intentionally Vulnerable Python Application
Contains deliberate security flaws and code quality issues for CodeGuard SAST testing.
DO NOT DEPLOY TO PRODUCTION.
"""

import sys  # Ruff F401: Unused import
import os   # Ruff F401: Unused import
import hashlib
import pickle
import subprocess

# 1. Hardcoded Credentials (Bandit B105 / CWE-798)
DB_PASSWORD = "SuperSecretMasterAdminPassword123!"
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLESECRETKEY"

# 2. Insecure MD5 Hash (AST-WEAK-HASH / Bandit B303 / CWE-328)
def hash_user_password(raw_password: str) -> str:
    hasher = hashlib.md5()
    hasher.update(raw_password.encode('utf-8'))
    return hasher.hexdigest()

# 3. Dynamic Code Execution via eval() (AST-EVAL / Bandit S102 / CWE-95)
def dynamic_calculator(user_expression: str):
    # Untrusted user input evaluated directly
    return eval(user_expression)

# 4. Insecure Deserialization via pickle (AST-PICKLE / Bandit B301 / CWE-502)
def restore_session(serialized_data: bytes):
    # Arbitrary code execution vulnerability on deserialization
    return pickle.loads(serialized_data)

# 5. OS Command Injection via subprocess shell=True (Bandit B602 / CWE-78)
def ping_server(hostname: str):
    command = f"ping -c 1 {hostname}"
    # Dangerous shell execution
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    return proc.communicate()

# 6. SQL Injection via string formatting (Bandit B608 / CWE-89)
def authenticate_user(cursor, username: str, user_pin: str):
    # Dynamic raw SQL query without parameterized bind variables
    query = f"SELECT id, username FROM users WHERE username = '{username}' AND pin = '{user_pin}'"
    cursor.execute(query)
    return cursor.fetchone()

# 7. High McCabe Cyclomatic Complexity (Ruff C901 / AST-COMPLEXITY)
def complex_decision_matrix(a, b, c, d, e, f, g):
    score = 0
    if a > 0:
        score += 1
        if b > 10:
            score += 2
        elif b < 5:
            score += 3
    else:
        score -= 1
        if c == 1:
            score += 4
        elif c == 2:
            score += 5
        elif c == 3:
            score += 6
    if d and e:
        score += 7
    elif d or f:
        score += 8
    if g == "vip":
        score += 9
    return score
