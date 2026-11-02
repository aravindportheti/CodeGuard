export type Severity = 'CRITICAL' | 'HIGH' | 'MEDIUM' | 'LOW';
export type ToolSource = 'BANDIT' | 'RUFF' | 'AST';
export type FindingStatus = 'OPEN' | 'RESOLVED' | 'FALSE_POSITIVE';

export interface Finding {
  id: number;
  scan_id: number;
  tool_source: ToolSource;
  rule_id: string;
  rule_name: string;
  severity: Severity;
  cwe_id: string | null;
  file_path: string;
  line_number: number;
  end_line?: number | null;
  column_number: number;
  description: string;
  code_snippet: string | null;
  status: FindingStatus;
  ai_explanation: string | null;
  created_at: string;
}

export interface ScanFile {
  id: number;
  relative_path: string;
  file_size_bytes: number;
  line_count: number;
  status: string;
}

export interface ScanSummary {
  id: number;
  project_id: number;
  scan_number: number;
  status: string;
  total_files: number;
  total_findings: number;
  critical_count: number;
  high_count: number;
  medium_count: number;
  low_count: number;
  duration_seconds: number;
  scan_type: string;
  created_at: string;
}

export interface ScanDetail extends ScanSummary {
  findings: Finding[];
  files: ScanFile[];
}

export interface Project {
  id: number;
  name: string;
  description: string | null;
  repo_url: string | null;
  created_at: string;
  updated_at: string;
  scans_count: number;
  latest_scan: ScanSummary | null;
}

export interface ScanDiffResult {
  baseline_scan_id: number;
  current_scan_id: number;
  new_findings: Finding[];
  fixed_findings: Finding[];
  recurring_findings: Finding[];
  metrics: {
    new_count: number;
    fixed_count: number;
    recurring_count: number;
    baseline_total: number;
    current_total: number;
  };
}
