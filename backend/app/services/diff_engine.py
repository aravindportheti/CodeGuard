from typing import List, Dict, Any
from app.models.finding import Finding

def compute_scan_diff(baseline_findings: List[Finding], current_findings: List[Finding]) -> Dict[str, Any]:
    """
    Computes a mathematical two-way diff between two scans.
    Categorizes findings into New, Fixed, and Recurring issues.
    """
    def make_key(f: Finding) -> str:
        # Match based on tool, rule, file path, and approximate line
        return f"{f.tool_source}:{f.rule_id}:{f.file_path}:{f.line_number}"

    baseline_map = {make_key(f): f for f in baseline_findings}
    current_map = {make_key(f): f for f in current_findings}

    baseline_keys = set(baseline_map.keys())
    current_keys = set(current_map.keys())

    new_keys = current_keys - baseline_keys
    fixed_keys = baseline_keys - current_keys
    recurring_keys = current_keys & baseline_keys

    new_list = [current_map[k] for k in sorted(new_keys)]
    fixed_list = [baseline_map[k] for k in sorted(fixed_keys)]
    recurring_list = [current_map[k] for k in sorted(recurring_keys)]

    return {
        "new_findings": new_list,
        "fixed_findings": fixed_list,
        "recurring_findings": recurring_list,
        "metrics": {
            "new_count": len(new_list),
            "fixed_count": len(fixed_list),
            "recurring_count": len(recurring_list),
            "baseline_total": len(baseline_findings),
            "current_total": len(current_findings)
        }
    }
