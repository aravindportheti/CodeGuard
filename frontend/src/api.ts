import { Project, ScanDetail, ScanSummary, Finding, ScanDiffResult, FindingStatus } from './types';

const API_BASE = '/api/v1';

export async function fetchProjects(): Promise<Project[]> {
  const res = await fetch(`${API_BASE}/projects`);
  if (!res.ok) throw new Error('Failed to load projects');
  return res.json();
}

export async function createProject(name: string, description?: string, repo_url?: string): Promise<Project> {
  const res = await fetch(`${API_BASE}/projects`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name, description, repo_url })
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: 'Failed to create project' }));
    throw new Error(err.detail || 'Failed to create project');
  }
  return res.json();
}

export async function deleteProject(projectId: number): Promise<void> {
  const res = await fetch(`${API_BASE}/projects/${projectId}`, { method: 'DELETE' });
  if (!res.ok) throw new Error('Failed to delete project');
}

export async function fetchScans(projectId?: number): Promise<ScanSummary[]> {
  const url = projectId ? `${API_BASE}/scans?project_id=${projectId}` : `${API_BASE}/scans`;
  const res = await fetch(url);
  if (!res.ok) throw new Error('Failed to load scans');
  return res.json();
}

export async function fetchScanDetail(scanId: number): Promise<ScanDetail> {
  const res = await fetch(`${API_BASE}/scans/${scanId}`);
  if (!res.ok) throw new Error('Failed to load scan details');
  return res.json();
}

export async function uploadScan(projectId: number, file: File): Promise<ScanDetail> {
  const formData = new FormData();
  formData.append('project_id', projectId.toString());
  formData.append('file', file);

  const res = await fetch(`${API_BASE}/scans/upload`, {
    method: 'POST',
    body: formData
  });

  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: 'Scan upload failed' }));
    throw new Error(err.detail || 'Scan upload failed');
  }

  return res.json();
}

export async function deleteScan(scanId: number): Promise<void> {
  const res = await fetch(`${API_BASE}/scans/${scanId}`, { method: 'DELETE' });
  if (!res.ok) throw new Error('Failed to delete scan');
}

export async function updateFindingStatus(findingId: number, status: FindingStatus): Promise<Finding> {
  const res = await fetch(`${API_BASE}/findings/${findingId}/status`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ status })
  });
  if (!res.ok) throw new Error('Failed to update finding status');
  return res.json();
}

export async function fetchScanDiff(scanId: number, baselineId: number): Promise<ScanDiffResult> {
  const res = await fetch(`${API_BASE}/scans/${scanId}/diff/${baselineId}`);
  if (!res.ok) throw new Error('Failed to compare scans');
  return res.json();
}

export function getReportPdfUrl(scanId: number): string {
  return `${API_BASE}/reports/${scanId}/pdf`;
}

export function getReportJsonUrl(scanId: number): string {
  return `${API_BASE}/reports/${scanId}/json`;
}
