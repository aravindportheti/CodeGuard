import React, { useState, useEffect } from 'react';
import { Header } from './components/Header';
import { Dashboard } from './components/Dashboard';
import { ScanDetailView } from './components/ScanDetailView';
import { ScanHistoryView } from './components/ScanHistoryView';
import { ScanUploadModal } from './components/ScanUploadModal';
import { ScanDiffModal } from './components/ScanDiffModal';
import { Project, ScanSummary, ScanDetail, ScanDiffResult } from './types';
import { fetchProjects, fetchScans, fetchScanDetail } from './api';

export const App: React.FC = () => {
  const [currentTab, setCurrentTab] = useState<'dashboard' | 'scans' | 'history'>('dashboard');
  const [projects, setProjects] = useState<Project[]>([]);
  const [scans, setScans] = useState<ScanSummary[]>([]);
  
  const [selectedScanDetail, setSelectedScanDetail] = useState<ScanDetail | null>(null);
  const [isLoadingDetail, setIsLoadingDetail] = useState(false);

  const [isUploadOpen, setIsUploadOpen] = useState(false);
  const [diffModalData, setDiffModalData] = useState<ScanDiffResult | null>(null);

  // Load initial projects & scans
  const loadData = async () => {
    try {
      const [projList, scanList] = await Promise.all([
        fetchProjects(),
        fetchScans()
      ]);
      setProjects(projList);
      setScans(scanList);
    } catch (err) {
      console.error('Failed to load initial data:', err);
    }
  };

  useEffect(() => {
    loadData();
  }, []);

  const handleSelectScan = async (scanId: number) => {
    setIsLoadingDetail(true);
    try {
      const detail = await fetchScanDetail(scanId);
      setSelectedScanDetail(detail);
      setCurrentTab('scans');
    } catch (err) {
      console.error('Failed to load scan detail:', err);
    } finally {
      setIsLoadingDetail(false);
    }
  };

  const handleScanComplete = (newScan: ScanDetail) => {
    setSelectedScanDetail(newScan);
    setCurrentTab('scans');
    loadData();
  };

  const handleRefreshScan = async () => {
    if (selectedScanDetail) {
      const updated = await fetchScanDetail(selectedScanDetail.id);
      setSelectedScanDetail(updated);
    }
    loadData();
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col font-sans">
      <Header
        currentTab={currentTab}
        onTabChange={(tab) => {
          setCurrentTab(tab);
          if (tab === 'dashboard' || tab === 'history') {
            setSelectedScanDetail(null);
          }
        }}
        onOpenUpload={() => setIsUploadOpen(true)}
      />

      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {currentTab === 'dashboard' && (
          <Dashboard
            projects={projects}
            scans={scans}
            onOpenUpload={() => setIsUploadOpen(true)}
            onSelectScan={handleSelectScan}
            onNavigateTab={(tab) => setCurrentTab(tab)}
          />
        )}

        {currentTab === 'scans' && (
          <>
            {isLoadingDetail ? (
              <div className="py-20 text-center text-slate-400">
                <div className="w-8 h-8 border-2 border-blue-500 border-t-transparent rounded-full animate-spin mx-auto mb-3"></div>
                <p className="text-xs">Loading scan details and findings...</p>
              </div>
            ) : selectedScanDetail ? (
              <ScanDetailView
                scan={selectedScanDetail}
                projectName={projects.find((p) => p.id === selectedScanDetail.project_id)?.name}
                onBack={() => {
                  setSelectedScanDetail(null);
                  setCurrentTab('dashboard');
                }}
                onRefreshScan={handleRefreshScan}
              />
            ) : (
              <div className="py-20 text-center">
                <h3 className="text-lg font-semibold text-white">Select a Scan to Inspect Findings</h3>
                <p className="text-xs text-slate-400 mt-1 mb-6">
                  Pick a scan from the dashboard or history, or upload new source code.
                </p>
                <button
                  onClick={() => setIsUploadOpen(true)}
                  className="px-5 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white text-xs font-bold transition shadow-lg shadow-blue-600/30"
                >
                  Start New Scan
                </button>
              </div>
            )}
          </>
        )}

        {currentTab === 'history' && (
          <ScanHistoryView
            scans={scans}
            projects={projects}
            onSelectScan={handleSelectScan}
            onRefresh={loadData}
            onOpenDiff={(diff) => setDiffModalData(diff)}
          />
        )}
      </main>

      {/* Upload Modal */}
      <ScanUploadModal
        isOpen={isUploadOpen}
        onClose={() => setIsUploadOpen(false)}
        projects={projects}
        onScanComplete={handleScanComplete}
        onProjectCreated={(newP) => setProjects([newP, ...projects])}
      />

      {/* Diff Comparison Modal */}
      <ScanDiffModal
        isOpen={Boolean(diffModalData)}
        onClose={() => setDiffModalData(null)}
        diffData={diffModalData}
      />

      {/* Footer */}
      <footer className="border-t border-slate-900 bg-slate-950 py-6 text-center text-xs text-slate-500">
        <div>CodeGuard Platform &bull; Intelligent Python Security &amp; Code Quality Assessment</div>
        <div className="text-[11px] text-slate-600 mt-1">
          Engines: Python Abstract Syntax Tree (AST) &bull; Bandit SAST (OWASP/CWE) &bull; Ruff Rust Linter &bull; ReportLab Vector PDF
        </div>
      </footer>
    </div>
  );
};

export default App;
