import React from 'react';
import { 
  ShieldCheck, AlertOctagon, Activity, FolderGit2, Plus, 
  ArrowRight, Clock, FileCode, CheckCircle, Zap
} from 'lucide-react';
import { Project, ScanSummary } from '../types';

interface DashboardProps {
  projects: Project[];
  scans: ScanSummary[];
  onOpenUpload: () => void;
  onSelectScan: (scanId: number) => void;
  onNavigateTab: (tab: 'scans' | 'history') => void;
}

export const Dashboard: React.FC<DashboardProps> = ({
  projects,
  scans,
  onOpenUpload,
  onSelectScan,
  onNavigateTab
}) => {
  // Aggregate statistics
  const totalScans = scans.length;
  const totalFindings = scans.reduce((acc, s) => acc + s.total_findings, 0);
  const totalCritical = scans.reduce((acc, s) => acc + s.critical_count, 0);
  const totalHigh = scans.reduce((acc, s) => acc + s.high_count, 0);
  const totalFiles = scans.reduce((acc, s) => acc + s.total_files, 0);

  const recentScans = scans.slice(0, 5);

  return (
    <div className="space-y-8 animate-fade-in">
      {/* Hero Welcome Banner */}
      <div className="relative overflow-hidden rounded-3xl bg-gradient-to-r from-blue-900/60 via-slate-900 to-indigo-950 border border-slate-800 p-8 shadow-2xl">
        <div className="relative z-10 max-w-2xl">
          <span className="px-3 py-1 rounded-full text-xs font-bold tracking-wider uppercase bg-blue-500/20 text-blue-300 border border-blue-500/30">
            DevSecOps Shift-Left Security
          </span>
          <h1 className="text-3xl font-extrabold text-white tracking-tight mt-3">
            Intelligent Source Code Quality & Vulnerability Detection
          </h1>
          <p className="text-sm text-slate-300 mt-2 leading-relaxed">
            Multi-engine static code assessment powered by Python AST, Bandit SAST rules, and Ruff. 
            Catch SQL injections, remote code execution vectors, and maintainability smells before deployment.
          </p>

          <div className="flex flex-wrap items-center gap-3 mt-6">
            <button
              onClick={onOpenUpload}
              className="flex items-center space-x-2 px-5 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white text-sm font-bold shadow-lg shadow-blue-600/30 transition hover:shadow-blue-600/50"
            >
              <Zap className="w-4 h-4" />
              <span>Upload & Scan Code</span>
            </button>
            <button
              onClick={() => onNavigateTab('history')}
              className="flex items-center space-x-2 px-5 py-2.5 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-200 text-sm font-semibold border border-slate-700/80 transition"
            >
              <Clock className="w-4 h-4" />
              <span>View Scan History</span>
            </button>
          </div>
        </div>

        {/* Ambient background decoration */}
        <div className="absolute right-0 top-0 bottom-0 w-1/3 bg-gradient-to-l from-blue-600/10 to-transparent pointer-events-none"></div>
      </div>

      {/* Aggregate Stat Metric Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 shadow-sm">
          <div className="flex items-center justify-between text-xs font-semibold text-slate-400 uppercase tracking-wider">
            <span>Active Projects</span>
            <FolderGit2 className="w-5 h-5 text-blue-400" />
          </div>
          <div className="text-3xl font-extrabold text-white mt-3">{projects.length}</div>
          <div className="text-xs text-slate-400 mt-1">Configured repositories</div>
        </div>

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 shadow-sm">
          <div className="flex items-center justify-between text-xs font-semibold text-slate-400 uppercase tracking-wider">
            <span>Total Code Audits</span>
            <Activity className="w-5 h-5 text-indigo-400" />
          </div>
          <div className="text-3xl font-extrabold text-white mt-3">{totalScans}</div>
          <div className="text-xs text-slate-400 mt-1">{totalFiles} total files processed</div>
        </div>

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 shadow-sm">
          <div className="flex items-center justify-between text-xs font-semibold text-red-400 uppercase tracking-wider">
            <span>Critical Threats</span>
            <AlertOctagon className="w-5 h-5 text-red-400" />
          </div>
          <div className="text-3xl font-extrabold text-red-400 mt-3">{totalCritical}</div>
          <div className="text-xs text-slate-400 mt-1">High-risk vulnerabilities detected</div>
        </div>

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-5 shadow-sm">
          <div className="flex items-center justify-between text-xs font-semibold text-emerald-400 uppercase tracking-wider">
            <span>Security Engine</span>
            <ShieldCheck className="w-5 h-5 text-emerald-400" />
          </div>
          <div className="text-3xl font-extrabold text-emerald-400 mt-3">3 Engines</div>
          <div className="text-xs text-slate-400 mt-1">AST &bull; Bandit &bull; Ruff</div>
        </div>
      </div>

      {/* Grid: Recent Scans & Projects */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
        {/* Recent Scans (8 cols) */}
        <div className="lg:col-span-8 bg-slate-900 border border-slate-800 rounded-3xl p-6 shadow-xl space-y-4">
          <div className="flex items-center justify-between pb-3 border-b border-slate-800">
            <div>
              <h3 className="text-base font-bold text-white">Recent Security Audits</h3>
              <p className="text-xs text-slate-400">Latest analysis runs across your workspaces</p>
            </div>
            <button
              onClick={() => onNavigateTab('history')}
              className="text-xs text-blue-400 hover:text-blue-300 font-semibold flex items-center space-x-1"
            >
              <span>See all history</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </button>
          </div>

          {recentScans.length === 0 ? (
            <div className="py-12 text-center text-slate-400 text-xs">
              No scans recorded yet. Click &quot;Upload &amp; Scan Code&quot; to test a Python file or project archive.
            </div>
          ) : (
            <div className="space-y-3">
              {recentScans.map((scan) => (
                <div
                  key={scan.id}
                  onClick={() => onSelectScan(scan.id)}
                  className="flex items-center justify-between p-3.5 rounded-xl bg-slate-950/60 border border-slate-800/80 hover:border-slate-700 hover:bg-slate-850/80 transition cursor-pointer"
                >
                  <div className="flex items-center space-x-3">
                    <div className="w-9 h-9 rounded-xl bg-blue-500/10 text-blue-400 flex items-center justify-center font-bold text-xs font-mono">
                      #{scan.scan_number}
                    </div>
                    <div>
                      <div className="text-sm font-semibold text-slate-200">
                        Scan #{scan.scan_number} &bull; {scan.scan_type}
                      </div>
                      <div className="text-xs text-slate-400">
                        {scan.total_files} files &bull; Duration {scan.duration_seconds}s
                      </div>
                    </div>
                  </div>

                  <div className="flex items-center space-x-3">
                    <div className="flex items-center space-x-1.5 text-xs">
                      {scan.critical_count > 0 && (
                        <span className="px-2 py-0.5 rounded font-bold bg-red-500/20 text-red-400 border border-red-500/30">
                          {scan.critical_count} Crit
                        </span>
                      )}
                      {scan.high_count > 0 && (
                        <span className="px-2 py-0.5 rounded font-bold bg-orange-500/20 text-orange-400 border border-orange-500/30">
                          {scan.high_count} High
                        </span>
                      )}
                      {scan.total_findings === 0 && (
                        <span className="px-2 py-0.5 rounded font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                          All Clean
                        </span>
                      )}
                    </div>
                    <ArrowRight className="w-4 h-4 text-slate-500" />
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Project Workspaces (4 cols) */}
        <div className="lg:col-span-4 bg-slate-900 border border-slate-800 rounded-3xl p-6 shadow-xl space-y-4">
          <div className="flex items-center justify-between pb-3 border-b border-slate-800">
            <div>
              <h3 className="text-base font-bold text-white">Project Registry</h3>
              <p className="text-xs text-slate-400">Active workspaces</p>
            </div>
            <button
              onClick={onOpenUpload}
              className="text-xs text-blue-400 hover:text-blue-300 font-semibold"
            >
              + New
            </button>
          </div>

          <div className="space-y-3">
            {projects.map((proj) => (
              <div
                key={proj.id}
                className="p-3.5 rounded-xl bg-slate-950/60 border border-slate-800 text-xs space-y-1.5"
              >
                <div className="font-bold text-slate-200 text-sm">{proj.name}</div>
                {proj.description && (
                  <p className="text-slate-400 truncate">{proj.description}</p>
                )}
                <div className="flex items-center justify-between text-slate-500 pt-1 font-mono">
                  <span>{proj.scans_count} scans conducted</span>
                  <span>ID: {proj.id}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
