import React from 'react';
import { X, GitCompare, ArrowRight, ShieldCheck, AlertCircle, RefreshCw } from 'lucide-react';
import { ScanDiffResult } from '../types';
import { SeverityBadge } from './SeverityBadge';

interface ScanDiffModalProps {
  isOpen: boolean;
  onClose: () => void;
  diffData: ScanDiffResult | null;
}

export const ScanDiffModal: React.FC<ScanDiffModalProps> = ({
  isOpen,
  onClose,
  diffData
}) => {
  if (!isOpen || !diffData) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-sm animate-fade-in">
      <div className="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-3xl max-h-[85vh] shadow-2xl overflow-hidden flex flex-col">
        {/* Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-slate-800">
          <div className="flex items-center space-x-2">
            <div className="w-8 h-8 rounded-lg bg-indigo-600/20 text-indigo-400 flex items-center justify-center">
              <GitCompare className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-lg font-bold text-white">Scan Comparison Diff</h3>
              <p className="text-xs text-slate-400">
                Comparing Baseline Scan #{diffData.baseline_scan_id} with Current Scan #{diffData.current_scan_id}
              </p>
            </div>
          </div>
          <button onClick={onClose} className="text-slate-400 hover:text-white transition">
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Diff Metrics Bar */}
        <div className="grid grid-cols-3 gap-3 p-5 bg-slate-950/60 border-b border-slate-800 text-center">
          <div className="p-3 rounded-xl bg-red-950/30 border border-red-800/40">
            <span className="text-xs font-semibold uppercase tracking-wider text-red-400">New (Regressions)</span>
            <div className="text-2xl font-bold text-red-400 mt-1">{diffData.metrics.new_count}</div>
          </div>
          <div className="p-3 rounded-xl bg-emerald-950/30 border border-emerald-800/40">
            <span className="text-xs font-semibold uppercase tracking-wider text-emerald-400">Fixed (Resolved)</span>
            <div className="text-2xl font-bold text-emerald-400 mt-1">{diffData.metrics.fixed_count}</div>
          </div>
          <div className="p-3 rounded-xl bg-slate-900 border border-slate-800">
            <span className="text-xs font-semibold uppercase tracking-wider text-slate-400">Recurring (Persistent)</span>
            <div className="text-2xl font-bold text-slate-200 mt-1">{diffData.metrics.recurring_count}</div>
          </div>
        </div>

        {/* Scrollable Findings Comparison Lists */}
        <div className="p-6 space-y-6 overflow-y-auto">
          {/* 1. Fixed Issues */}
          <div>
            <div className="flex items-center space-x-2 text-sm font-bold text-emerald-400 mb-2">
              <ShieldCheck className="w-4 h-4" />
              <span>Resolved / Fixed Findings ({diffData.fixed_findings.length})</span>
            </div>
            {diffData.fixed_findings.length === 0 ? (
              <p className="text-xs text-slate-500 italic">No previously existing findings were resolved in this revision.</p>
            ) : (
              <div className="space-y-2">
                {diffData.fixed_findings.map((f) => (
                  <div key={f.id} className="p-2.5 rounded-lg bg-emerald-950/10 border border-emerald-900/30 flex items-center justify-between text-xs">
                    <div className="flex items-center space-x-2">
                      <SeverityBadge severity={f.severity} size="sm" />
                      <span className="font-mono font-bold text-slate-300">{f.rule_id}</span>
                      <span className="text-slate-400 truncate max-w-xs">{f.description}</span>
                    </div>
                    <span className="font-mono text-slate-400">{f.file_path}:{f.line_number}</span>
                  </div>
                ))}
              </div>
            )}
          </div>

          {/* 2. New Issues */}
          <div>
            <div className="flex items-center space-x-2 text-sm font-bold text-red-400 mb-2">
              <AlertCircle className="w-4 h-4" />
              <span>Newly Introduced Vulnerabilities ({diffData.new_findings.length})</span>
            </div>
            {diffData.new_findings.length === 0 ? (
              <p className="text-xs text-slate-500 italic">No new vulnerabilities were introduced in this scan. Great job!</p>
            ) : (
              <div className="space-y-2">
                {diffData.new_findings.map((f) => (
                  <div key={f.id} className="p-2.5 rounded-lg bg-red-950/10 border border-red-900/30 flex items-center justify-between text-xs">
                    <div className="flex items-center space-x-2">
                      <SeverityBadge severity={f.severity} size="sm" />
                      <span className="font-mono font-bold text-slate-300">{f.rule_id}</span>
                      <span className="text-slate-400 truncate max-w-xs">{f.description}</span>
                    </div>
                    <span className="font-mono text-slate-400">{f.file_path}:{f.line_number}</span>
                  </div>
                ))}
              </div>
            )}
          </div>

          {/* 3. Recurring Issues */}
          <div>
            <div className="flex items-center space-x-2 text-sm font-bold text-slate-400 mb-2">
              <RefreshCw className="w-4 h-4" />
              <span>Recurring Technical Debt ({diffData.recurring_findings.length})</span>
            </div>
            {diffData.recurring_findings.length === 0 ? (
              <p className="text-xs text-slate-500 italic">No persistent findings.</p>
            ) : (
              <div className="space-y-2 max-h-48 overflow-y-auto pr-1">
                {diffData.recurring_findings.map((f) => (
                  <div key={f.id} className="p-2 rounded-lg bg-slate-950 border border-slate-800 flex items-center justify-between text-xs">
                    <div className="flex items-center space-x-2">
                      <SeverityBadge severity={f.severity} size="sm" />
                      <span className="font-mono text-slate-300">{f.rule_id}</span>
                      <span className="text-slate-400 truncate max-w-xs">{f.description}</span>
                    </div>
                    <span className="font-mono text-slate-400">{f.file_path}:{f.line_number}</span>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>

        {/* Footer */}
        <div className="px-6 py-3 bg-slate-950 border-t border-slate-800 flex justify-end">
          <button
            onClick={onClose}
            className="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-white text-xs font-semibold transition"
          >
            Close Diff View
          </button>
        </div>
      </div>
    </div>
  );
};
