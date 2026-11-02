import React from 'react';
import { Terminal } from 'lucide-react';

interface CodeSnippetViewerProps {
  filePath: string;
  lineNumber: number;
  snippet: string | null;
}

export const CodeSnippetViewer: React.FC<CodeSnippetViewerProps> = ({ filePath, lineNumber, snippet }) => {
  if (!snippet) {
    return (
      <div className="bg-slate-900 border border-slate-800 rounded-lg p-4 text-xs text-slate-500 italic">
        Context code preview is not available for this finding.
      </div>
    );
  }

  const lines = snippet.split('\n');

  return (
    <div className="bg-slate-950 border border-slate-800 rounded-xl overflow-hidden shadow-inner">
      <div className="flex items-center justify-between px-4 py-2 bg-slate-900 border-b border-slate-800 text-xs font-mono text-slate-400">
        <div className="flex items-center space-x-2">
          <Terminal className="w-3.5 h-3.5 text-blue-400" />
          <span className="text-slate-200 font-semibold">{filePath}</span>
        </div>
        <span className="text-slate-400">Line {lineNumber}</span>
      </div>

      <div className="p-3 font-mono text-xs overflow-x-auto leading-relaxed">
        {lines.map((lineText, idx) => {
          const isTarget = lineText.startsWith('>>>');
          return (
            <div
              key={idx}
              className={`py-0.5 px-2 rounded font-mono ${
                isTarget
                  ? 'bg-red-500/20 text-red-200 border-l-2 border-red-500 font-bold'
                  : 'text-slate-300'
              }`}
            >
              {lineText}
            </div>
          );
        })}
      </div>
    </div>
  );
};
