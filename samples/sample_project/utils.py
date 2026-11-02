import os  # Unused import

def run_dynamic_command(cmd: str):
    # Dynamic execution vulnerability
    exec(cmd)
