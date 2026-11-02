import React, { useState } from 'react';
import { History, GitCompare, Download, Eye, Trash2, ArrowRight } from 'lucide-react';
import { ScanSummary, Project, ScanDiffResult } from '../types';
import { fetchScanDiff, deleteScan, getReportPdfUrl } from '../api';

interface ScanHistoryViewProps {
  scans: ScanSummary[];
  projects: Project[];
  onSelectScan: (scanId: number) => void;
  onRefresh: () => void;
  onOpenDiff: (diff: ScanDiffResult) => void;
}

export const ScanHistoryView: React.FC<ScanHistoryViewProps> = ({
  scans,
  projects,
  onSelectScan,
  onRefresh,
  onOpenDiff
}) => {
  const [selectedProjectId, setSelectedProjectId] = useState<number | 'ALL'>('ALL');
  const [isComparing, setIsComparing] = useState(false);

  const projectMap = new Map(projects.map((p) => [p.id, p.name]));

  const filteredScans = scans.filter((s) => {
    return selectedProjectId === 'ALL' || s.project_id === selectedProjectId;
  });

  const handleCompareWithPrevious = async (currentScan: ScanSummary, idx: number) => {
    // Find the next older scan in the same project
    const previousScan = filteredScans.slice(idx + 1).find((s) => s.project_id === currentScan.project_id);
    if (!previousScan) {
      alert('No earlier baseline scan exists in this project to compare against.');
      return;
    }

    setIsComparing(true);
    try {
      const diffResult = await fetchScanDiff(currentScan.id, previousScan.id);
      setIsComparing(false);
      onOpenDiff(diffResult);
    } catch (err: any) {
      setIsComparing(false);
      alert(err.message || 'Failed to compare scans');
    }
  };

  const handleDelete = async (scanId: number, e: React.MouseEvent) => {
    e.stopPropagation();
    if (confirm('Are you sure you want to delete this scan record?')) {
      await deleteScan(scanId);
      onRefresh();
    }
  };

  return (
    <div className="space-y-6 animate-fade-in">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-800">
        <div>
          <h2 className="text-2xl font-bold text-white tracking-tight flex items-center space-x-2">
            <History className="w-6 h-6 text-blue-400" />
            <span>Scan Audit History & Comparisons</span>
          </h2>
          <p className="text-xs text-slate-400 mt-1">
            Track code evolution across revisions and compare changes against baseline audits.
          </p>
        </div>

        {/* Project Filter */}
        <div className="flex items-center space-x-2">
          <span className="text-xs text-slate-400 font-semibold">Filter:</span>
          <select
            value={selectedProjectId}
            onChange={(e) => setSelectedProjectId(e.target.value === 'ALL' ? 'ALL' : Number(e.target.value))}
            className="bg-slate-900 border border-slate-800 rounded-xl px-3 py-1.5 text-xs text-white focus:outline-none focus:border-blue-500"
          >
            <option value="ALL">All Projects ({scans.length} scans)</option>
            {projects.map((p) => (
              <option key={p.id} value={p.id}>
                {p.name}
              </option>
            ))}
          </select>
        </div>
      </div>

      {/* History Table */}
      {filteredScans.length === 0 ? (
        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-12 text-center text-slate-400">
          No scans found for this selection. Upload a new code package to generate your first audit record!
        </div>
      ) : (
        <div className="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden shadow-xl">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-850 border-b border-slate-800 text-slate-400 font-semibold uppercase">
              <tr>
                <th className="px-5 py-3.5">Scan</th>
                <th className="px-5 py-3.5">Project</th>
                <th className="px-5 py-3.5">Date</th>
                <th className="px-5 py-3.5">Files & Duration</th>
                <th className="px-5 py-3.5">Severity Metrics</th>
                <th className="px-5 py-3.5 text-right">Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800">
              {filteredScans.map((scan, idx) => {
                const projectName = projectMap.get(scan.project_id) || `Project #${scan.project_id}`;
                return (
                  <tr
                    key={scan.id}
                    onClick={() => onSelectScan(scan.id)}
                    className="hover:bg-slate-850/60 transition cursor-pointer"
                  >
                    <td className="px-5 py-4">
                      <div className="font-bold text-white">Scan #{scan.scan_number}</div>
                      <div className="text-[11px] text-slate-500 font-mono">ID: {scan.id}</div>
                    </td>

                    <td className="px-5 py-4 font-semibold text-slate-200">
                      {projectName}
                    </td>

                    <td className="px-5 py-4 text-slate-400">
                      {new Date(scan.created_at).toLocaleString()}
                    </td>

                    <td className="px-5 py-4 text-slate-300">
                      <div>{scan.total_files} files</div>
                      <div className="text-[11px] text-slate-500">{scan.duration_seconds}s execution</div>
                    </td>

                    <td className="px-5 py-4">
                      <div className="flex items-center space-x-1.5">
                        <span className="px-2 py-0.5 rounded text-[11px] font-bold bg-red-500/20 text-red-400 border border-red-500/30">
                          {scan.critical_count} Crit
                        </span>
                        <span className="px-2 py-0.5 rounded text-[11px] font-bold bg-orange-500/20 text-orange-400 border border-orange-500/30">
                          {scan.high_count} High
                        </span>
                        <span className="px-2 py-0.5 rounded text-[11px] font-bold bg-amber-500/20 text-amber-400 border border-amber-500/30">
                          {scan.medium_count} Med
                        </span>
                        <span className="px-2 py-0.5 rounded text-[11px] font-bold bg-blue-500/20 text-blue-400 border border-blue-500/30">
                          {scan.low_count} Low
                        </span>
                      </div>
                    </td>

                    <td className="px-5 py-4 text-right">
                      <div className="flex items-center justify-end space-x-2" onClick={(e) => e.stopPropagation()}>
                        <button
                          onClick={() => handleCompareWithPrevious(scan, idx)}
                          title="Compare with earlier baseline scan"
                          className="p-1.5 rounded-lg bg-slate-800 hover:bg-indigo-600 text-slate-300 hover:text-white transition"
                        >
                          <GitCompare className="w-3.5 h-3.5" />
                        </button>

                        <a
                          href={getReportPdfUrl(scan.id)}
                          download
                          title="Download PDF Audit Report"
                          className="p-1.5 rounded-lg bg-slate-800 hover:bg-blue-600 text-slate-300 hover:text-white transition"
                        >
                          <Download className="w-3.5 h-3.5" />
                        </a>

                        <button
                          onClick={() => onSelectScan(scan.id)}
                          title="Inspect Findings"
                          className="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white transition"
                        >
                          <Eye className="w-3.5 h-3.5" />
                        </button>

                        <button
                          onClick={(e) => handleDelete(scan.id, e)}
                          title="Delete Scan"
                          className="p-1.5 rounded-lg bg-slate-800 hover:bg-red-600/80 text-slate-400 hover:text-white transition"
                        >
                          <Trash2 className="w-3.5 h-3.5" />
                        </button>
                      </div>
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};
