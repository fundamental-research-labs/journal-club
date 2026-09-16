import { Focus, GitFork, Map, RotateCcw } from "lucide-react";

import { cx } from "../lib/classNames";
import { useGraphStore } from "../store/graphStore";
import type { LayoutMode } from "../domain/types";

interface HeaderProps {
  onFit: () => void;
  onReset: () => void;
}

const layoutOptions: Array<{ mode: LayoutMode; label: string; icon: typeof GitFork }> = [
  { mode: "tech", label: "Tree", icon: GitFork },
  { mode: "map", label: "Map", icon: Map },
];

export function Header({ onFit, onReset }: HeaderProps) {
  const layoutMode = useGraphStore((state) => state.layoutMode);
  const setLayoutMode = useGraphStore((state) => state.setLayoutMode);
  const stats = useGraphStore((state) => state.model.data.stats);

  return (
    <header className="flex min-h-16 items-center justify-between gap-4 border-b border-slate-200 bg-white px-4 py-2.5 max-[760px]:flex-col max-[760px]:items-start">
      <div className="min-w-0">
        <h1 className="truncate text-xl font-semibold leading-tight text-slate-950">Literature Tech Tree</h1>
        <p className="mt-1 text-sm text-slate-500">
          {stats.paperCount} papers, {stats.bibliographyEdgeCount} bib edges, {stats.curatedMentionEdgeCount} note
          edges
        </p>
      </div>

      <div className="flex flex-wrap items-center justify-end gap-2" aria-label="Graph controls">
        <div className="grid grid-cols-2 gap-1 rounded-lg bg-slate-100 p-1" role="group" aria-label="View mode">
          {layoutOptions.map(({ mode, label, icon: Icon }) => (
            <button
              key={mode}
              type="button"
              className={cx(
                "inline-flex min-h-9 items-center justify-center gap-1.5 rounded-md px-3 text-sm font-medium text-slate-700 transition",
                layoutMode === mode && "bg-teal-900 text-white shadow-sm",
              )}
              onClick={() => setLayoutMode(mode)}
            >
              <Icon size={15} aria-hidden="true" />
              <span>{label}</span>
            </button>
          ))}
        </div>

        <button
          type="button"
          className="inline-flex min-h-9 items-center gap-1.5 rounded-md border border-slate-200 bg-white px-3 text-sm font-medium text-slate-800 hover:border-slate-400"
          onClick={onFit}
        >
          <Focus size={15} aria-hidden="true" />
          <span>Fit</span>
        </button>
        <button
          type="button"
          className="inline-flex min-h-9 items-center gap-1.5 rounded-md border border-slate-200 bg-white px-3 text-sm font-medium text-slate-800 hover:border-slate-400"
          onClick={onReset}
        >
          <RotateCcw size={15} aria-hidden="true" />
          <span>Reset</span>
        </button>
      </div>
    </header>
  );
}
