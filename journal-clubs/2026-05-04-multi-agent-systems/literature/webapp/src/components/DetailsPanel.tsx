import { FileText } from "lucide-react";

import { relatedEdges, shortTitle } from "../domain/graphModel";
import type { RuntimeEdge } from "../domain/types";
import { useGraphStore } from "../store/graphStore";

function pathLink(path: string): string {
  if (import.meta.env.DEV) {
    return `/@fs/${__LITERATURE_REPO_ROOT__}/${path}`;
  }
  return `../../${path}`;
}

export function DetailsPanel() {
  const model = useGraphStore((state) => state.model);
  const selectedId = useGraphStore((state) => state.selectedId);
  const selectNode = useGraphStore((state) => state.selectNode);
  const node = selectedId ? model.nodeById.get(selectedId) : null;

  if (!node) {
    return (
      <aside className="details overflow-auto border-l border-slate-200 bg-white p-4" aria-label="Selected paper">
        <div className="grid gap-3 text-sm leading-relaxed text-slate-500">
          <h2 className="text-xs font-semibold uppercase leading-tight text-slate-500">Selection</h2>
          <p>Choose a paper in the graph or list to inspect incoming and outgoing citation structure.</p>
          <p>Bibliography edges come from local .bib/.bbl files. Note edges come from curated summaries, notes, and claims.</p>
        </div>
      </aside>
    );
  }

  const related = relatedEdges(model, node.id);
  const incoming = related.filter((edge) => edge.target === node.id);
  const outgoing = related.filter((edge) => edge.source === node.id);
  const authors = node.authors.slice(0, 4).join(", ") + (node.authors.length > 4 ? " et al." : "");
  const topics = node.topics.slice(0, 10);

  return (
    <aside className="details overflow-auto border-l border-slate-200 bg-white p-4" aria-label="Selected paper">
      <h2 className="text-lg font-semibold leading-tight text-slate-950">{node.title}</h2>
      <div className="my-3 grid gap-1.5 text-sm leading-snug text-slate-500">
        <span>{authors || "Unknown authors"}</span>
        <span>{[node.year, node.venue, node.status].filter(Boolean).join(" · ")}</span>
        {node.arxiv ? <span>arXiv {node.arxiv}</span> : null}
        <span>
          {node.classification.primarySubareaLabel} · {node.classification.roleLabel} ·{" "}
          {node.classification.artifactTypeLabel}
        </span>
        {node.classification.seedSubarea ? <span>Seed sub-area: {node.classification.seedSubarea}</span> : null}
        <span>
          Classification: {node.classification.confidence} via {node.classification.source}
        </span>
        <span>
          {node.inDegree} incoming · {node.outDegree} outgoing · {node.degree} total
        </span>
      </div>

      <div className="my-3 flex flex-wrap gap-1.5">
        {topics.map((topic) => (
          <span key={topic} className="max-w-full rounded-full bg-slate-100 px-2 py-1 text-xs leading-tight text-slate-700 [overflow-wrap:anywhere]">
            {topic}
          </span>
        ))}
        {node.classification.domains.map((domain) => (
          <span
            key={domain}
            className="max-w-full rounded-full bg-teal-50 px-2 py-1 text-xs leading-tight text-teal-900 [overflow-wrap:anywhere]"
          >
            {domain}
          </span>
        ))}
      </div>

      <p className="my-3 text-sm leading-relaxed text-slate-700">{node.summary || "No summary in metadata."}</p>

      <SectionTitle>Files</SectionTitle>
      <div className="my-2.5 grid gap-2">
        <FileLink href={pathLink(node.paths.pdf)} label="PDF" />
        <FileLink href={pathLink(node.paths.summary)} label="Summary" />
        <FileLink href={pathLink(node.paths.metadata)} label="Metadata" />
      </div>

      <SectionTitle>Outgoing</SectionTitle>
      <div className="my-2.5 grid gap-2">
        {outgoing.length ? (
          outgoing.map((edge) => <EdgeButton key={`${edge.source}->${edge.target}:${edge.kind}`} edge={edge} otherId={edge.target} onSelect={selectNode} />)
        ) : (
          <span className="text-xs text-slate-500">No outgoing local citation edges yet.</span>
        )}
      </div>

      <SectionTitle>Incoming</SectionTitle>
      <div className="my-2.5 grid gap-2">
        {incoming.length ? (
          incoming.map((edge) => <EdgeButton key={`${edge.source}->${edge.target}:${edge.kind}`} edge={edge} otherId={edge.source} onSelect={selectNode} />)
        ) : (
          <span className="text-xs text-slate-500">No incoming local citation edges yet.</span>
        )}
      </div>
    </aside>
  );
}

function SectionTitle({ children }: { children: string }) {
  return <h3 className="mt-4 text-xs font-semibold uppercase leading-tight text-slate-500">{children}</h3>;
}

function FileLink({ href, label }: { href: string; label: string }) {
  return (
    <a
      className="flex min-h-9 items-center gap-2 rounded-md border border-slate-200 bg-white px-2.5 py-2 text-sm leading-snug text-slate-800 no-underline hover:border-teal-700 hover:text-teal-900"
      href={href}
    >
      <FileText size={15} aria-hidden="true" />
      <span>{label}</span>
    </a>
  );
}

function EdgeButton({
  edge,
  otherId,
  onSelect,
}: {
  edge: RuntimeEdge;
  otherId: string;
  onSelect: (id: string) => void;
}) {
  const other = edge.source === otherId ? edge.sourceNode : edge.targetNode;
  const firstEvidence = edge.evidence[0] || {};
  const label = edge.kind === "bibliography" ? "Bib" : "Note";
  const file = firstEvidence.file ? firstEvidence.file.replace(/^papers\//, "") : "local files";

  return (
    <button
      type="button"
      className="grid min-h-11 w-full gap-1 rounded-md border border-slate-200 bg-white px-2.5 py-2 text-left text-sm leading-snug text-slate-800 hover:border-teal-700 hover:text-teal-900"
      onClick={() => onSelect(otherId)}
    >
      <span>
        <span className="mr-1.5 inline-block min-w-14 text-xs uppercase text-slate-500">{label}</span>
        {shortTitle(other.title, 76)}
      </span>
      <span className="text-xs text-slate-500">{file}</span>
    </button>
  );
}
