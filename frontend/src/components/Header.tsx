import React from 'react';
import { Shield, PlusCircle, Activity, History, FolderKanban, CheckCircle } from 'lucide-react';

interface HeaderProps {
  currentTab: 'dashboard' | 'scans' | 'history';
  onTabChange: (tab: 'dashboard' | 'scans' | 'history') => void;
  onOpenUpload: () => void;
}

export const Header: React.FC<HeaderProps> = ({ currentTab, onTabChange, onOpenUpload }) => {
  return (
    <header className="border-b border-slate-800 bg-slate-900/80 backdrop-blur sticky top-0 z-30">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Brand Logo & Name */}
          <div className="flex items-center space-x-3 cursor-pointer" onClick={() => onTabChange('dashboard')}>
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-blue-700 via-blue-600 to-cyan-500 flex items-center justify-center shadow-lg shadow-blue-500/20">
              <Shield className="w-6 h-6 text-white" />
            </div>
            <div>
              <span className="text-xl font-bold bg-gradient-to-r from-white via-slate-100 to-slate-400 bg-clip-text text-transparent">
                CodeGuard
              </span>
              <span className="ml-2 text-xs font-semibold px-2 py-0.5 rounded-full bg-blue-500/10 text-blue-400 border border-blue-500/20">
                SAST & Quality
              </span>
            </div>
          </div>

          {/* Navigation Links */}
          <nav className="hidden md:flex space-x-1">
            <button
              onClick={() => onTabChange('dashboard')}
              className={`flex items-center space-x-2 px-3 py-2 rounded-lg text-sm font-medium transition ${
                currentTab === 'dashboard'
                  ? 'bg-blue-600 text-white shadow-md shadow-blue-600/30'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              }`}
            >
              <Activity className="w-4 h-4" />
              <span>Dashboard</span>
            </button>

            <button
              onClick={() => onTabChange('scans')}
              className={`flex items-center space-x-2 px-3 py-2 rounded-lg text-sm font-medium transition ${
                currentTab === 'scans'
                  ? 'bg-blue-600 text-white shadow-md shadow-blue-600/30'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              }`}
            >
              <FolderKanban className="w-4 h-4" />
              <span>Scan Explorer</span>
            </button>

            <button
              onClick={() => onTabChange('history')}
              className={`flex items-center space-x-2 px-3 py-2 rounded-lg text-sm font-medium transition ${
                currentTab === 'history'
                  ? 'bg-blue-600 text-white shadow-md shadow-blue-600/30'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              }`}
            >
              <History className="w-4 h-4" />
              <span>Scan History & Diff</span>
            </button>
          </nav>

          {/* Action Button & Status */}
          <div className="flex items-center space-x-4">
            <div className="hidden lg:flex items-center space-x-1.5 text-xs text-emerald-400 font-medium px-2.5 py-1 rounded-full bg-emerald-950/60 border border-emerald-800/50">
              <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
              <span>Engines Active (AST, Bandit, Ruff)</span>
            </div>

            <button
              onClick={onOpenUpload}
              className="flex items-center space-x-2 px-4 py-2 rounded-lg bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 text-white text-sm font-semibold shadow-md shadow-blue-600/20 transition hover:shadow-blue-600/40 active:scale-95"
            >
              <PlusCircle className="w-4 h-4" />
              <span>New Code Scan</span>
            </button>
          </div>
        </div>
      </div>
    </header>
  );
};
