import React, { useState, useRef } from 'react';
import { X, UploadCloud, FileCode, CheckCircle2, AlertCircle, Loader2 } from 'lucide-react';
import { Project, ScanDetail } from '../types';
import { uploadScan, createProject } from '../api';

interface ScanUploadModalProps {
  isOpen: boolean;
  onClose: () => void;
  projects: Project[];
  onScanComplete: (scan: ScanDetail) => void;
  onProjectCreated: (newProj: Project) => void;
}

export const ScanUploadModal: React.FC<ScanUploadModalProps> = ({
  isOpen,
  onClose,
  projects,
  onScanComplete,
  onProjectCreated
}) => {
  const [selectedProjectId, setSelectedProjectId] = useState<number>(projects[0]?.id || 1);
  const [isCreatingNewProject, setIsCreatingNewProject] = useState(false);
  const [newProjectName, setNewProjectName] = useState('');
  const [newProjectDesc, setNewProjectDesc] = useState('');

  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [isDragging, setIsDragging] = useState(false);
  const [isScanning, setIsScanning] = useState(false);
  const [errorMsg, setErrorMsg] = useState<string | null>(null);

  const fileInputRef = useRef<HTMLInputElement>(null);

  if (!isOpen) return null;

  const handleFileDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      validateAndSetFile(e.dataTransfer.files[0]);
    }
  };

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      validateAndSetFile(e.target.files[0]);
    }
  };

  const validateAndSetFile = (file: File) => {
    setErrorMsg(null);
    const ext = file.name.split('.').pop()?.toLowerCase();
    if (ext !== 'py' && ext !== 'zip') {
      setErrorMsg('Invalid file format. Please upload a .py file or a .zip project archive.');
      return;
    }
    if (file.size > 25 * 1024 * 1024) {
      setErrorMsg('File exceeds 25 MB limit.');
      return;
    }
    setSelectedFile(file);
  };

  const handleStartScan = async () => {
    if (!selectedFile) {
      setErrorMsg('Please select a Python file or ZIP archive to scan.');
      return;
    }

    setIsScanning(true);
    setErrorMsg(null);

    try {
      let targetProjectId = selectedProjectId;

      // Create new project if selected
      if (isCreatingNewProject) {
        if (!newProjectName.trim()) {
          setErrorMsg('Please specify a name for the new project.');
          setIsScanning(false);
          return;
        }
        const createdProj = await createProject(newProjectName.trim(), newProjectDesc.trim());
        onProjectCreated(createdProj);
        targetProjectId = createdProj.id;
      }

      const scanResult = await uploadScan(targetProjectId, selectedFile);
      setIsScanning(false);
      onScanComplete(scanResult);
      onClose();
    } catch (err: any) {
      setIsScanning(false);
      setErrorMsg(err.message || 'An error occurred during static analysis.');
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-sm animate-fade-in">
      <div className="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-lg shadow-2xl overflow-hidden">
        {/* Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-slate-800">
          <div className="flex items-center space-x-2">
            <div className="w-8 h-8 rounded-lg bg-blue-600/20 text-blue-400 flex items-center justify-center">
              <UploadCloud className="w-5 h-5" />
            </div>
            <h3 className="text-lg font-bold text-white">Start New Code Scan</h3>
          </div>
          <button
            onClick={onClose}
            disabled={isScanning}
            className="text-slate-400 hover:text-white transition disabled:opacity-50"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Body */}
        <div className="p-6 space-y-5">
          {errorMsg && (
            <div className="flex items-start space-x-3 p-3 rounded-lg bg-red-500/15 border border-red-500/30 text-red-300 text-sm">
              <AlertCircle className="w-5 h-5 flex-shrink-0 mt-0.5 text-red-400" />
              <span>{errorMsg}</span>
            </div>
          )}

          {/* Project Selection */}
          <div>
            <div className="flex items-center justify-between mb-2">
              <label className="text-xs font-semibold uppercase tracking-wider text-slate-400">
                Target Project
              </label>
              <button
                type="button"
                onClick={() => setIsCreatingNewProject(!isCreatingNewProject)}
                className="text-xs text-blue-400 hover:text-blue-300 font-medium transition"
              >
                {isCreatingNewProject ? 'Choose Existing Project' : '+ Create New Project'}
              </button>
            </div>

            {!isCreatingNewProject ? (
              <select
                value={selectedProjectId}
                onChange={(e) => setSelectedProjectId(Number(e.target.value))}
                className="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
              >
                {projects.map((p) => (
                  <option key={p.id} value={p.id}>
                    {p.name} {p.scans_count > 0 ? `(${p.scans_count} scans)` : ''}
                  </option>
                ))}
              </select>
            ) : (
              <div className="space-y-3 bg-slate-950/60 p-3.5 rounded-xl border border-slate-800">
                <input
                  type="text"
                  placeholder="Project Name (e.g., Payment Gateway Service)"
                  value={newProjectName}
                  onChange={(e) => setNewProjectName(e.target.value)}
                  className="w-full bg-slate-900 border border-slate-700/80 rounded-lg px-3 py-2 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-blue-500"
                />
                <input
                  type="text"
                  placeholder="Optional description"
                  value={newProjectDesc}
                  onChange={(e) => setNewProjectDesc(e.target.value)}
                  className="w-full bg-slate-900 border border-slate-700/80 rounded-lg px-3 py-2 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-blue-500"
                />
              </div>
            )}
          </div>

          {/* File Upload Drop Zone */}
          <div>
            <label className="block text-xs font-semibold uppercase tracking-wider text-slate-400 mb-2">
              Source Code File or ZIP Package
            </label>
            <input
              type="file"
              ref={fileInputRef}
              onChange={handleFileSelect}
              accept=".py,.zip"
              className="hidden"
            />
            <div
              onDragOver={(e) => {
                e.preventDefault();
                setIsDragging(true);
              }}
              onDragLeave={() => setIsDragging(false)}
              onDrop={handleFileDrop}
              onClick={() => fileInputRef.current?.click()}
              className={`border-2 border-dashed rounded-2xl p-6 text-center cursor-pointer transition ${
                isDragging
                  ? 'border-blue-500 bg-blue-500/10'
                  : selectedFile
                  ? 'border-emerald-500/50 bg-emerald-500/5'
                  : 'border-slate-800 hover:border-slate-700 bg-slate-950/40 hover:bg-slate-950/70'
              }`}
            >
              {selectedFile ? (
                <div className="flex flex-col items-center space-y-2">
                  <div className="w-12 h-12 rounded-xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center">
                    <CheckCircle2 className="w-6 h-6" />
                  </div>
                  <div className="text-sm font-semibold text-white">{selectedFile.name}</div>
                  <div className="text-xs text-slate-400">
                    {(selectedFile.size / 1024).toFixed(1)} KB &bull; Ready to Analyze
                  </div>
                  <span className="text-xs text-blue-400 hover:underline pt-1">
                    Click or drop another file to replace
                  </span>
                </div>
              ) : (
                <div className="flex flex-col items-center space-y-2">
                  <div className="w-12 h-12 rounded-xl bg-slate-800 text-slate-400 flex items-center justify-center">
                    <FileCode className="w-6 h-6" />
                  </div>
                  <div className="text-sm font-semibold text-slate-200">
                    Click to browse or drag and drop
                  </div>
                  <div className="text-xs text-slate-400">
                    Supports standalone <b>.py</b> files or complete <b>.zip</b> project archives (Max 25 MB)
                  </div>
                </div>
              )}
            </div>
          </div>

          <div className="bg-slate-950/70 rounded-xl p-3 border border-slate-800 text-xs text-slate-400 space-y-1">
            <div className="font-semibold text-slate-300">Analysis Safety Guarantee:</div>
            <div>&bull; Static analysis only. Code is <b>NEVER executed</b>.</div>
            <div>&bull; Analyzed via native Python AST, Bandit SAST rules, and Ruff linter.</div>
          </div>
        </div>

        {/* Footer */}
        <div className="flex items-center justify-end space-x-3 px-6 py-4 bg-slate-900 border-t border-slate-800">
          <button
            type="button"
            onClick={onClose}
            disabled={isScanning}
            className="px-4 py-2 text-sm font-medium text-slate-400 hover:text-white transition disabled:opacity-50"
          >
            Cancel
          </button>
          <button
            type="button"
            onClick={handleStartScan}
            disabled={isScanning || !selectedFile}
            className="flex items-center space-x-2 px-5 py-2 rounded-xl bg-blue-600 hover:bg-blue-500 text-white text-sm font-semibold shadow-md shadow-blue-600/30 transition disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {isScanning ? (
              <>
                <Loader2 className="w-4 h-4 animate-spin" />
                <span>Running Multi-Engine Scan...</span>
              </>
            ) : (
              <span>Execute Scan</span>
            )}
          </button>
        </div>
      </div>
    </div>
  );
};
