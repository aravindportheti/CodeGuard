import React, { useState } from 'react';
import { 
  Download, FileText, CheckCircle, AlertTriangle, ShieldAlert, 
  ExternalLink, ArrowLeft, Filter, Search, Check, RefreshCw
} from 'lucide-react';
import { ScanDetail, Finding, Severity, FindingStatus } from '../types';
import { SeverityBadge } from './SeverityBadge';
import { CodeSnippetViewer } from './CodeSnippetViewer';
import { updateFindingStatus, getReportPdfUrl, getReportJsonUrl } from '../api';

interface ScanDetailViewProps {
  scan: ScanDetail;
  projectName?: string;
  onBack: () => void;
  onRefreshScan: () => void;
}

export const ScanDetailView: React.FC<ScanDetailViewProps> = ({
  scan,
  projectName = 'Project',
  onBack,
  onRefreshScan
}) => {
  const [selectedSeverity, setSelectedSeverity] = useState<Severity | 'ALL'>('ALL');
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedFinding, setSelectedFinding] = useState<Finding | null>(null);
  const [isUpdatingStatus, setIsUpdatingStatus] = useState(false);
  const [activeTab, setActiveTab] = useState<'findings' | 'files'>('findings');

  // Filter findings
  const filteredFindings = scan.findings.filter((f) => {
    const matchesSev = selectedSeverity === 'ALL' || f.severity === selectedSeverity;
    const matchesSearch = 
      f.description.toLowerCase().includes(searchQuery.toLowerCase()) ||
      f.rule_id.toLowerCase().includes(searchQuery.toLowerCase()) ||
      f.file_path.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesSev && matchesSearch;
  });

  const handleStatusChange = async (findingId: number, newStatus: FindingStatus) => {
    setIsUpdatingStatus(true);
    try {
      const updated = await updateFindingStatus(findingId, newStatus);
      // Update local state
      if (selectedFinding && selectedFinding.id === findingId) {
        setSelectedFinding(updated);
      }
      onRefreshScan();
    } catch (err) {
      console.error(err);
    } finally {
      setIsUpdatingStatus(false);
    }
  };

  return (
    <div className="space-y-6 animate-fade-in">
      {/* Top Breadcrumb & Action Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-4 border-b border-slate-800">
        <div>
          <button
            onClick={onBack}
            className="flex items-center space-x-1.5 text-xs font-semibold text-slate-400 hover:text-white transition mb-2"
          >
            <ArrowLeft className="w-4 h-4" />
            <span>Back to Explorer</span>
          </button>
          <div className="flex items-center space-x-3">
            <h2 className="text-2xl font-bold text-white tracking-tight">
              Scan #{scan.scan_number} Results
            </h2>
            <span className="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-blue-500/10 text-blue-400 border border-blue-500/20">
              {scan.scan_type}
            </span>
          </div>
          <div className="text-xs text-slate-400 mt-1">
            Project: <span className="text-slate-200 font-semibold">{projectName}</span> &bull; Scanned {scan.total_files} files in {scan.duration_seconds}s
          </div>
        </div>

        {/* Download Buttons */}
        <div className="flex items-center space-x-3">
          <a
            href={getReportPdfUrl(scan.id)}
            download
            className="flex items-center space-x-2 px-3.5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700 transition shadow-sm hover:text-white"
          >
            <Download className="w-3.5 h-3.5 text-red-400" />
            <span>Download PDF Report</span>
          </a>

          <a
            href={getReportJsonUrl(scan.id)}
            download
            className="flex items-center space-x-2 px-3.5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700 transition shadow-sm hover:text-white"
          >
            <FileText className="w-3.5 h-3.5 text-blue-400" />
            <span>Export JSON</span>
          </a>
        </div>
      </div>

      {/* Metric Cards Row */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div 
          onClick={() => setSelectedSeverity(selectedSeverity === 'CRITICAL' ? 'ALL' : 'CRITICAL')}
          className={`p-4 rounded-2xl border transition cursor-pointer ${
            selectedSeverity === 'CRITICAL' ? 'ring-2 ring-red-500 bg-red-950/40 border-red-500/50' : 'bg-slate-900 border-slate-800 hover:border-slate-700'
          }`}
        >
          <div className="flex items-center justify-between text-xs text-red-400 font-semibold uppercase tracking-wider">
            <span>Critical</span>
            <ShieldAlert className="w-4 h-4" />
          </div>
          <div className="text-3xl font-bold text-red-400 mt-2">{scan.critical_count}</div>
          <div className="text-xs text-slate-400 mt-1">Immediate exploit risk</div>
        </div>

        <div 
          onClick={() => setSelectedSeverity(selectedSeverity === 'HIGH' ? 'ALL' : 'HIGH')}
          className={`p-4 rounded-2xl border transition cursor-pointer ${
            selectedSeverity === 'HIGH' ? 'ring-2 ring-orange-500 bg-orange-950/40 border-orange-500/50' : 'bg-slate-900 border-slate-800 hover:border-slate-700'
          }`}
        >
          <div className="flex items-center justify-between text-xs text-orange-400 font-semibold uppercase tracking-wider">
            <span>High</span>
            <AlertTriangle className="w-4 h-4" />
          </div>
          <div className="text-3xl font-bold text-orange-400 mt-2">{scan.high_count}</div>
          <div className="text-xs text-slate-400 mt-1">Severe vulnerabilities</div>
        </div>

        <div 
          onClick={() => setSelectedSeverity(selectedSeverity === 'MEDIUM' ? 'ALL' : 'MEDIUM')}
          className={`p-4 rounded-2xl border transition cursor-pointer ${
            selectedSeverity === 'MEDIUM' ? 'ring-2 ring-amber-500 bg-amber-950/40 border-amber-500/50' : 'bg-slate-900 border-slate-800 hover:border-slate-700'
          }`}
        >
          <div className="flex items-center justify-between text-xs text-amber-400 font-semibold uppercase tracking-wider">
            <span>Medium</span>
            <AlertTriangle className="w-4 h-4" />
          </div>
          <div className="text-3xl font-bold text-amber-400 mt-2">{scan.medium_count}</div>
          <div className="text-xs text-slate-400 mt-1">Quality & crypto flaws</div>
        </div>

        <div 
          onClick={() => setSelectedSeverity(selectedSeverity === 'LOW' ? 'ALL' : 'LOW')}
          className={`p-4 rounded-2xl border transition cursor-pointer ${
            selectedSeverity === 'LOW' ? 'ring-2 ring-blue-500 bg-blue-950/40 border-blue-500/50' : 'bg-slate-900 border-slate-800 hover:border-slate-700'
          }`}
        >
          <div className="flex items-center justify-between text-xs text-blue-400 font-semibold uppercase tracking-wider">
            <span>Low / Style</span>
            <CheckCircle className="w-4 h-4" />
          </div>
          <div className="text-3xl font-bold text-blue-400 mt-2">{scan.low_count}</div>
          <div className="text-xs text-slate-400 mt-1">PEP 8 & dead code</div>
        </div>
      </div>

      {/* Tabs & Search Filter Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pt-2">
        <div className="flex items-center space-x-2">
          <button
            onClick={() => setActiveTab('findings')}
            className={`px-4 py-2 rounded-xl text-xs font-bold uppercase tracking-wider transition ${
              activeTab === 'findings'
                ? 'bg-blue-600 text-white'
                : 'bg-slate-900 text-slate-400 hover:text-white border border-slate-800'
            }`}
          >
            Findings Matrix ({scan.total_findings})
          </button>
          <button
            onClick={() => setActiveTab('files')}
            className={`px-4 py-2 rounded-xl text-xs font-bold uppercase tracking-wider transition ${
              activeTab === 'files'
                ? 'bg-blue-600 text-white'
                : 'bg-slate-900 text-slate-400 hover:text-white border border-slate-800'
            }`}
          >
            Scanned Files ({scan.total_files})
          </button>
        </div>

        {activeTab === 'findings' && (
          <div className="flex items-center space-x-3">
            <div className="relative">
              <Search className="w-4 h-4 text-slate-500 absolute left-3 top-2.5" />
              <input
                type="text"
                placeholder="Search findings by rule, message, or file..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="bg-slate-900 border border-slate-800 rounded-xl pl-9 pr-3 py-2 text-xs text-white placeholder-slate-500 w-64 focus:outline-none focus:border-blue-500"
              />
            </div>
            {selectedSeverity !== 'ALL' && (
              <button
                onClick={() => setSelectedSeverity('ALL')}
                className="text-xs text-blue-400 hover:text-blue-300 font-medium"
              >
                Clear Filter
              </button>
            )}
          </div>
        )}
      </div>

      {/* Main Content Area */}
      {activeTab === 'findings' ? (
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          {/* Findings Table List */}
          <div className={`space-y-3 ${selectedFinding ? 'lg:col-span-7' : 'lg:col-span-12'}`}>
            {filteredFindings.length === 0 ? (
              <div className="bg-slate-900 border border-slate-800 rounded-2xl p-10 text-center">
                <CheckCircle className="w-12 h-12 text-emerald-400 mx-auto mb-3" />
                <h4 className="text-base font-semibold text-white">No Issues Match Current Filter</h4>
                <p className="text-xs text-slate-400 mt-1">
                  Try adjusting severity filter or clear search terms.
                </p>
              </div>
            ) : (
              filteredFindings.map((finding) => {
                const isSelected = selectedFinding?.id === finding.id;
                return (
                  <div
                    key={finding.id}
                    onClick={() => setSelectedFinding(finding)}
                    className={`p-4 rounded-2xl border transition cursor-pointer ${
                      isSelected
                        ? 'bg-slate-850 border-blue-500 shadow-md ring-1 ring-blue-500/50'
                        : 'bg-slate-900 border-slate-800 hover:border-slate-700 hover:bg-slate-850/50'
                    }`}
                  >
                    <div className="flex items-start justify-between gap-3">
                      <div className="flex items-center space-x-2.5">
                        <SeverityBadge severity={finding.severity} size="sm" />
                        <span className="font-mono text-xs font-bold text-slate-200">
                          {finding.rule_id}
                        </span>
                        <span className="text-xs text-slate-400 px-1.5 py-0.5 rounded bg-slate-800 font-mono">
                          {finding.tool_source}
                        </span>
                        {finding.cwe_id && (
                          <span className="text-xs text-slate-400 px-1.5 py-0.5 rounded bg-slate-800/80 font-mono">
                            {finding.cwe_id}
                          </span>
                        )}
                      </div>

                      <span
                        className={`text-xs font-semibold px-2 py-0.5 rounded-full ${
                          finding.status === 'RESOLVED'
                            ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/30'
                            : finding.status === 'FALSE_POSITIVE'
                            ? 'bg-slate-700/50 text-slate-400 border border-slate-600/50'
                            : 'bg-red-500/10 text-red-400 border border-red-500/20'
                        }`}
                      >
                        {finding.status}
                      </span>
                    </div>

                    <div className="mt-2 text-sm text-slate-200 font-medium">
                      {finding.description}
                    </div>

                    <div className="mt-2 flex items-center justify-between text-xs text-slate-400 font-mono">
                      <span>{finding.file_path}:{finding.line_number}</span>
                      <span className="text-blue-400 hover:underline">Inspect details &rarr;</span>
                    </div>
                  </div>
                );
              })
            )}
          </div>

          {/* Finding Detail & Remediation Inspector (Right Drawer) */}
          {selectedFinding && (
            <div className="lg:col-span-5 bg-slate-900 border border-slate-800 rounded-2xl p-5 space-y-5 sticky top-24 shadow-2xl">
              <div className="flex items-start justify-between pb-3 border-b border-slate-800">
                <div>
                  <div className="flex items-center space-x-2">
                    <SeverityBadge severity={selectedFinding.severity} />
                    <span className="font-mono text-sm font-bold text-white">
                      {selectedFinding.rule_id}
                    </span>
                  </div>
                  <h3 className="text-base font-semibold text-slate-200 mt-2">
                    {selectedFinding.rule_name}
                  </h3>
                </div>
                <button
                  onClick={() => setSelectedFinding(null)}
                  className="text-slate-400 hover:text-white transition"
                >
                  &times;
                </button>
              </div>

              <div>
                <label className="text-xs font-semibold uppercase tracking-wider text-slate-400">
                  Diagnostic Message
                </label>
                <p className="text-xs text-slate-200 mt-1 leading-relaxed bg-slate-950 p-3 rounded-xl border border-slate-800">
                  {selectedFinding.description}
                </p>
              </div>

              {/* Code Snippet Viewer */}
              <div>
                <label className="text-xs font-semibold uppercase tracking-wider text-slate-400 mb-1.5 block">
                  Context Code (±2 Lines)
                </label>
                <CodeSnippetViewer
                  filePath={selectedFinding.file_path}
                  lineNumber={selectedFinding.line_number}
                  snippet={selectedFinding.code_snippet}
                />
              </div>

              {/* AI Remediation */}
              <div>
                <label className="text-xs font-semibold uppercase tracking-wider text-emerald-400 mb-1.5 block flex items-center space-x-1">
                  <span>AI Remediation & Patch Advice</span>
                </label>
                <div className="bg-emerald-950/20 border border-emerald-800/40 rounded-xl p-3 text-xs text-emerald-200 whitespace-pre-wrap leading-relaxed">
                  {selectedFinding.ai_explanation || 'No remediation guidance available.'}
                </div>
              </div>

              {/* Resolution Actions */}
              <div className="pt-2 border-t border-slate-800 flex items-center justify-between">
                <span className="text-xs text-slate-400">Resolution Status:</span>
                <div className="flex items-center space-x-2">
                  {selectedFinding.status !== 'RESOLVED' && (
                    <button
                      onClick={() => handleStatusChange(selectedFinding.id, 'RESOLVED')}
                      disabled={isUpdatingStatus}
                      className="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-semibold transition"
                    >
                      Mark Resolved
                    </button>
                  )}
                  {selectedFinding.status !== 'FALSE_POSITIVE' && (
                    <button
                      onClick={() => handleStatusChange(selectedFinding.id, 'FALSE_POSITIVE')}
                      disabled={isUpdatingStatus}
                      className="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold transition"
                    >
                      Mark False Positive
                    </button>
                  )}
                  {selectedFinding.status !== 'OPEN' && (
                    <button
                      onClick={() => handleStatusChange(selectedFinding.id, 'OPEN')}
                      disabled={isUpdatingStatus}
                      className="px-3 py-1.5 rounded-lg bg-red-600/80 hover:bg-red-500 text-white text-xs font-semibold transition"
                    >
                      Re-open Issue
                    </button>
                  )}
                </div>
              </div>
            </div>
          )}
        </div>
      ) : (
        /* Scanned Files Manifest View */
        <div className="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-850 border-b border-slate-800 text-slate-400 font-semibold uppercase">
              <tr>
                <th className="px-5 py-3">File Path</th>
                <th className="px-5 py-3">Lines of Code</th>
                <th className="px-5 py-3">File Size</th>
                <th className="px-5 py-3">Scan Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800">
              {scan.files.map((file) => (
                <tr key={file.id} className="hover:bg-slate-850/50">
                  <td className="px-5 py-3 font-mono text-slate-200">{file.relative_path}</td>
                  <td className="px-5 py-3 text-slate-400">{file.line_count} LOC</td>
                  <td className="px-5 py-3 text-slate-400">{(file.file_size_bytes / 1024).toFixed(1)} KB</td>
                  <td className="px-5 py-3">
                    <span className="px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 text-xs font-semibold">
                      {file.status}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};
