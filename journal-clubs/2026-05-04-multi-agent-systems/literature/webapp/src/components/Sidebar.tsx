import { Search } from "lucide-react";
import { useMemo } from "react";

import { shortTitle } from "../domain/graphModel";
import type { EdgeMode } from "../domain/types";
import { cx } from "../lib/classNames";
import { useGraphStore } from "../store/graphStore";

const edgeModes: Array<{ mode: EdgeMode; label: string }> = [
  { mode: "all", label: "All" },
  { mode: "bibliography", label: "Bib" },
  { mode: "curated-mention", label: "Notes" },
];

export function Sidebar() {
  const model = useGraphStore((state) => state.model);
  const search = useGraphStore((state) => state.search);
  const setSearch = useGraphStore((state) => state.setSearch);
  const edgeMode = useGraphStore((state) => state.edgeMode);
  const setEdgeMode = useGraphStore((state) => state.setEdgeMode);
  const selectedStatuses = useGraphStore((state) => state.selectedStatuses);
  const setStatus = useGraphStore((state) => state.setStatus);
  const hideIsolated = useGraphStore((state) => state.hideIsolated);
  const setHideIsolated = useGraphStore((state) => state.setHideIsolated);
  const showNeighborhood = useGraphStore((state) => state.showNeighborhood);
  const setShowNeighborhood = useGraphStore((state) => state.setShowNeighborhood);
  const selectedId = useGraphStore((state) => state.selectedId);
  const visibleNodeIds = useGraphStore((state) => state.visibleNodeIds);
  const selectNode = useGraphStore((state) => state.selectNode);

  const sortedPapers = useMemo(
    () =>
      model.nodes
        .filter((node) => visibleNodeIds.has(node.id))
        .sort((a, b) => b.degree - a.degree || (b.year || 0) - (a.year || 0) || a.title.localeCompare(b.title)),
    [model.nodes, visibleNodeIds],
  );

  return (
    <aside className="sidebar overflow-auto border-r border-slate-200 bg-white p-3.5" aria-label="Paper filters">
      <label className="mb-3.5 grid gap-1.5 text-xs font-semibold text-slate-500">
        <span>Search</span>
        <span className="relative">
          <Search className="pointer-events-none absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" size={15} />
          <input
            className="min-h-10 w-full rounded-md border border-slate-200 bg-white py-2 pl-9 pr-3 text-sm font-normal text-slate-950 outline-none focus:border-teal-700 focus:ring-2 focus:ring-teal-700/15"
            type="search"
            placeholder="title, author, topic"
            value={search}
            onChange={(event) => setSearch(event.target.value)}
          />
        </span>
      </label>

      <section className="border-t border-slate-200 py-3.5">
        <h2 className="text-xs font-semibold uppercase leading-tight text-slate-500">Edges</h2>
        <div className="my-2.5 grid grid-cols-3 gap-1 rounded-lg bg-slate-100 p-1" role="group" aria-label="Edge type">
          {edgeModes.map((option) => (
            <button
              key={option.mode}
              type="button"
              className={cx(
                "min-h-8 rounded-md px-2 text-sm font-medium text-slate-700",
                edgeMode === option.mode && "bg-teal-900 text-white shadow-sm",
              )}
              onClick={() => setEdgeMode(option.mode)}
            >
              {option.label}
            </button>
          ))}
        </div>
        <label className="flex min-h-7 items-center gap-2 text-sm text-slate-800">
          <input
            className="size-4 accent-teal-700"
            type="checkbox"
            checked={hideIsolated}
            onChange={(event) => setHideIsolated(event.target.checked)}
          />
          <span>Hide isolated papers</span>
        </label>
        <label className="mt-1.5 flex min-h-7 items-center gap-2 text-sm text-slate-800">
          <input
            className="size-4 accent-teal-700 disabled:opacity-40"
            type="checkbox"
            checked={showNeighborhood}
            disabled={!selectedId}
            onChange={(event) => setShowNeighborhood(event.target.checked)}
          />
          <span className={!selectedId ? "text-slate-400" : undefined}>Selected neighborhood</span>
        </label>
      </section>

      <section className="border-t border-slate-200 py-3.5">
        <h2 className="text-xs font-semibold uppercase leading-tight text-slate-500">Status</h2>
        <div className="mt-2.5 grid gap-2">
          {model.statuses.map((status) => (
            <label key={status} className="flex min-h-7 items-center gap-2 text-sm text-slate-800">
              <input
                className="size-4 accent-teal-700"
                type="checkbox"
                checked={selectedStatuses.has(status)}
                onChange={(event) => setStatus(status, event.target.checked)}
              />
              <span>
                {status} ({model.data.stats.statuses[status] || 0})
              </span>
            </label>
          ))}
        </div>
      </section>

      <section className="border-t border-slate-200 py-3.5">
        <div className="mb-2 flex items-center justify-between gap-2">
          <h2 className="text-xs font-semibold uppercase leading-tight text-slate-500">Papers</h2>
          <span className="text-xs text-slate-500">
            {visibleNodeIds.size}/{model.nodes.length}
          </span>
        </div>
        <div className="grid gap-1.5">
          {sortedPapers.map((node) => (
            <button
              key={node.id}
              type="button"
              className={cx(
                "grid min-h-14 w-full gap-1 rounded-md border border-transparent p-2 text-left hover:border-slate-200 hover:bg-slate-100",
                node.id === selectedId && "border-teal-700 bg-slate-100",
              )}
              onClick={() => selectNode(node.id)}
            >
              <strong className="text-sm font-semibold leading-tight text-slate-950 [overflow-wrap:anywhere]">
                {shortTitle(node.title, 78)}
              </strong>
              <span className="text-xs text-slate-500">
                {[node.year, node.classification.primarySubareaLabel, `${node.inDegree} in`, `${node.outDegree} out`]
                  .filter(Boolean)
                  .join(" · ")}
              </span>
            </button>
          ))}
        </div>
      </section>
    </aside>
  );
}
