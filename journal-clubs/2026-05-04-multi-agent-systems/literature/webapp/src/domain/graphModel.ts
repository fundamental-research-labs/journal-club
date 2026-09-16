import type {
  DateParts,
  EdgeMode,
  GraphModel,
  LiteratureGraph,
  RuntimeEdge,
  RuntimeNode,
  TaxonomyTerm,
  TechLayout,
} from "./types";

export const STATUS_COLORS: Record<string, string> = {
  seed: "#0f766e",
  top100: "#c2410c",
  reviewed: "#4b5563",
  candidate: "#7c3aed",
  unspecified: "#64748b",
};

export function statusColor(status: string | undefined): string {
  return STATUS_COLORS[status || "unspecified"] || STATUS_COLORS.unspecified;
}

export function createGraphModel(data: LiteratureGraph): GraphModel {
  const usedSubareas = new Set(data.nodes.map((node) => node.classification.primarySubarea));
  const lanes = data.taxonomy.subareas.filter(
    (subarea) => subarea.id !== "needs-classification" || usedSubareas.has(subarea.id),
  );

  const nodes: RuntimeNode[] = data.nodes.map((node, index) => ({
    ...node,
    index,
    x: 0,
    y: 0,
    vx: 0,
    vy: 0,
    radius: 7,
    cardWidth: 184,
    cardHeight: 66,
    lane: 0,
    row: 0,
    degree: 0,
    inDegree: 0,
    outDegree: 0,
    bibliographyDegree: 0,
    mentionDegree: 0,
    baseX: 0,
    fixed: false,
  }));

  const nodeById = new Map(nodes.map((node) => [node.id, node]));
  const edges: RuntimeEdge[] = data.edges
    .map((edge) => {
      const sourceNode = nodeById.get(edge.source);
      const targetNode = nodeById.get(edge.target);
      return sourceNode && targetNode ? { ...edge, sourceNode, targetNode } : null;
    })
    .filter((edge): edge is RuntimeEdge => edge !== null);

  edges.forEach((edge) => {
    edge.sourceNode.outDegree += 1;
    edge.targetNode.inDegree += 1;
    edge.sourceNode.degree += 1;
    edge.targetNode.degree += 1;
    if (edge.kind === "bibliography") {
      edge.sourceNode.bibliographyDegree += 1;
      edge.targetNode.bibliographyDegree += 1;
    } else {
      edge.sourceNode.mentionDegree += 1;
      edge.targetNode.mentionDegree += 1;
    }
  });

  nodes.forEach((node) => {
    node.radius = Math.max(6, Math.min(18, 6 + Math.sqrt(node.degree) * 2.4));
  });

  const statuses = [...new Set(nodes.map((node) => node.status || "unspecified"))].sort();
  return { data, nodes, edges, nodeById, statuses, lanes };
}

export function shortTitle(title: string | undefined, limit = 46): string {
  if (!title) return "Untitled";
  return title.length > limit ? `${title.slice(0, limit - 1)}...` : title;
}

export function searchableText(node: RuntimeNode): string {
  return [
    node.title,
    node.authors.join(" "),
    node.topics.join(" "),
    node.venue,
    node.status,
    node.classification.primarySubareaLabel,
    node.classification.roleLabel,
    node.classification.artifactTypeLabel,
    node.classification.seedSubarea,
    node.classification.domains.join(" "),
    node.summary,
    node.arxiv,
    node.id,
  ]
    .join(" ")
    .toLowerCase();
}

export function laneForNode(node: RuntimeNode, lanes: TaxonomyTerm[]): number {
  const lane = lanes.findIndex((item) => item.id === node.classification.primarySubarea);
  if (lane >= 0) return lane;
  const fallbackLane = lanes.findIndex((item) => item.id === "needs-classification");
  return fallbackLane >= 0 ? fallbackLane : 0;
}

export function dateParts(node: RuntimeNode): DateParts {
  const match = String(node.date || "").match(/^(\d{4})(?:-(\d{1,2}))?/);
  const year = match ? Number(match[1]) : Number(node.year);
  const month = match && match[2] ? Number(match[2]) : 6;
  return {
    year: Number.isFinite(year) ? year : null,
    month: Number.isFinite(month) ? Math.max(1, Math.min(12, month)) : 6,
  };
}

export function timeSortValue(node: RuntimeNode): number {
  const parts = dateParts(node);
  return parts.year ? parts.year * 12 + parts.month : 999999;
}

export function wrapTitle(title: string | undefined, maxChars = 25, maxLines = 2): string[] {
  const words = String(title || "Untitled").split(/\s+/);
  const lines: string[] = [];
  let line = "";

  words.forEach((word) => {
    const next = line ? `${line} ${word}` : word;
    if (next.length <= maxChars) {
      line = next;
    } else {
      if (line) lines.push(line);
      line = word;
    }
  });
  if (line) lines.push(line);

  if (lines.length > maxLines) {
    const kept = lines.slice(0, maxLines);
    kept[maxLines - 1] = `${kept[maxLines - 1].slice(0, Math.max(8, maxChars - 3))}...`;
    return kept;
  }
  return lines;
}

export function selectedNeighborIds(selectedId: string | null, edges: RuntimeEdge[]): Set<string> {
  const ids = new Set<string>();
  if (!selectedId) return ids;
  ids.add(selectedId);
  edges.forEach((edge) => {
    if (edge.source === selectedId) ids.add(edge.target);
    if (edge.target === selectedId) ids.add(edge.source);
  });
  return ids;
}

export function edgeAllowed(edge: RuntimeEdge, edgeMode: EdgeMode): boolean {
  return edgeMode === "all" || edge.kind === edgeMode;
}

export interface VisibilityOptions {
  edgeMode: EdgeMode;
  selectedStatuses: Set<string>;
  search: string;
  hideIsolated: boolean;
  showNeighborhood: boolean;
  selectedId: string | null;
}

export function computeVisibility(
  model: GraphModel,
  options: VisibilityOptions,
): { visibleNodeIds: Set<string>; visibleEdges: RuntimeEdge[] } {
  const query = options.search.trim().toLowerCase();
  const baseVisible = new Set(
    model.nodes
      .filter((node) => options.selectedStatuses.has(node.status || "unspecified"))
      .filter((node) => !query || searchableText(node).includes(query))
      .map((node) => node.id),
  );

  const relevantEdges = model.edges.filter(
    (edge) => edgeAllowed(edge, options.edgeMode) && baseVisible.has(edge.source) && baseVisible.has(edge.target),
  );

  if (options.hideIsolated) {
    const connected = new Set<string>();
    relevantEdges.forEach((edge) => {
      connected.add(edge.source);
      connected.add(edge.target);
    });
    [...baseVisible].forEach((id) => {
      if (!connected.has(id)) baseVisible.delete(id);
    });
  }

  if (options.showNeighborhood && options.selectedId) {
    const neighbors = selectedNeighborIds(options.selectedId, model.edges);
    [...baseVisible].forEach((id) => {
      if (!neighbors.has(id)) baseVisible.delete(id);
    });
  }

  return {
    visibleNodeIds: baseVisible,
    visibleEdges: relevantEdges.filter((edge) => baseVisible.has(edge.source) && baseVisible.has(edge.target)),
  };
}

export function initPositions(model: GraphModel, width: number, height: number): void {
  const years = model.nodes.map((node) => node.year).filter((year): year is number => Boolean(year));
  const minYear = years.length ? Math.min(...years) : 2020;
  const maxYear = years.length ? Math.max(...years) : minYear + 1;
  const span = Math.max(1, maxYear - minYear);

  model.nodes.forEach((node, index) => {
    const yearPosition = node.year ? (node.year - minYear) / span : 0.5;
    const ring = (index * 137.5 * Math.PI) / 180;
    node.x = 100 + yearPosition * Math.max(320, width - 200) + Math.cos(ring) * 80;
    node.y = 90 + ((index * 47) % Math.max(260, height - 180));
    node.vx = 0;
    node.vy = 0;
    node.fixed = false;
  });
}

export function applyTechTreeLayout(model: GraphModel, visibleNodeIds: Set<string>): TechLayout {
  const visible = model.nodes
    .filter((node) => visibleNodeIds.has(node.id))
    .sort((a, b) => timeSortValue(a) - timeSortValue(b) || b.degree - a.degree || a.title.localeCompare(b.title));
  const datedYears = visible.map((node) => dateParts(node).year).filter((year): year is number => Boolean(year));
  const minYear = datedYears.length ? Math.min(...datedYears) : 2020;
  const maxYear = datedYears.length ? Math.max(...datedYears) : minYear;
  const years = Array.from({ length: maxYear - minYear + 1 }, (_, index) => minYear + index);
  const yearWidth = 330;
  const marginX = 212;
  const marginY = 72;
  const rowGap = 12;
  const colGap = 18;
  const lanePad = 46;
  const cardHeight = model.nodes[0]?.cardHeight || 66;
  const laneBuckets = Array.from({ length: model.lanes.length }, () => [] as RuntimeNode[]);

  visible.forEach((node) => {
    node.lane = laneForNode(node, model.lanes);
    const parts = dateParts(node);
    const yearOffset = parts.year ? parts.year - minYear : maxYear - minYear + 1;
    const monthOffset = parts.year ? (parts.month - 1) / 12 : 0.45;
    node.baseX = marginX + (yearOffset + monthOffset) * yearWidth;
    laneBuckets[node.lane].push(node);
  });

  const laneRows = laneBuckets.map((laneNodes) => {
    const rowEnds: number[] = [];
    laneNodes
      .sort((a, b) => a.baseX - b.baseX || b.degree - a.degree || a.title.localeCompare(b.title))
      .forEach((node) => {
        const preferredRow = rowEnds.findIndex((endX) => node.baseX >= endX + colGap);
        const row = preferredRow >= 0 ? preferredRow : rowEnds.length;
        node.x = node.baseX;
        node.vx = 0;
        node.vy = 0;
        rowEnds[row] = node.baseX + node.cardWidth;
        node.row = row;
      });
    return Math.max(1, rowEnds.length);
  });

  const laneHeights = laneRows.map((rowCount) => lanePad + rowCount * cardHeight + Math.max(0, rowCount - 1) * rowGap);
  const laneTops: number[] = [];
  let nextLaneTop = marginY;
  laneHeights.forEach((height) => {
    laneTops.push(nextLaneTop);
    nextLaneTop += height;
  });

  laneBuckets.forEach((laneNodes, lane) => {
    laneNodes.forEach((node) => {
      node.y = laneTops[lane] + node.row * (node.cardHeight + rowGap);
    });
  });

  const contentMaxX = visible.reduce((maxX, node) => Math.max(maxX, node.x + node.cardWidth), marginX);
  const timelineMaxX = marginX + Math.max(1, years.length) * yearWidth;
  const laneHeight = Math.max(...laneHeights);

  return {
    years,
    minYear,
    maxYear,
    laneTops,
    laneHeights,
    laneHeight,
    yearWidth,
    marginX,
    height: nextLaneTop,
    width: Math.max(contentMaxX + marginX, timelineMaxX),
  };
}

export function tickMap(
  model: GraphModel,
  visibleNodeIds: Set<string>,
  visibleEdges: RuntimeEdge[],
  width: number,
  height: number,
): void {
  const visible = model.nodes.filter((node) => visibleNodeIds.has(node.id));
  const visibleSet = new Set(visible.map((node) => node.id));
  const years = visible.map((node) => node.year).filter((year): year is number => Boolean(year));
  const minYear = years.length ? Math.min(...years) : 2020;
  const maxYear = years.length ? Math.max(...years) : minYear + 1;
  const yearSpan = Math.max(1, maxYear - minYear);

  visibleEdges.forEach((edge) => {
    const source = edge.sourceNode;
    const target = edge.targetNode;
    const dx = target.x - source.x;
    const dy = target.y - source.y;
    const distance = Math.max(1, Math.hypot(dx, dy));
    const desired = edge.kind === "bibliography" ? 118 : 154;
    const strength = edge.kind === "bibliography" ? 0.012 : 0.006;
    const force = (distance - desired) * strength;
    const fx = (dx / distance) * force;
    const fy = (dy / distance) * force;
    if (!source.fixed) {
      source.vx += fx;
      source.vy += fy;
    }
    if (!target.fixed) {
      target.vx -= fx;
      target.vy -= fy;
    }
  });

  for (let i = 0; i < visible.length; i += 1) {
    for (let j = i + 1; j < visible.length; j += 1) {
      const a = visible[i];
      const b = visible[j];
      const dx = b.x - a.x || 0.1;
      const dy = b.y - a.y || 0.1;
      const distanceSq = Math.max(80, dx * dx + dy * dy);
      const distance = Math.sqrt(distanceSq);
      const minDistance = a.radius + b.radius + 14;
      const charge = Math.min(2.4, 940 / distanceSq);
      const pushX = (dx / distance) * charge;
      const pushY = (dy / distance) * charge;
      if (!a.fixed) {
        a.vx -= pushX;
        a.vy -= pushY;
      }
      if (!b.fixed) {
        b.vx += pushX;
        b.vy += pushY;
      }
      if (distance < minDistance) {
        const overlap = (minDistance - distance) * 0.015;
        if (!a.fixed) {
          a.vx -= (dx / distance) * overlap;
          a.vy -= (dy / distance) * overlap;
        }
        if (!b.fixed) {
          b.vx += (dx / distance) * overlap;
          b.vy += (dy / distance) * overlap;
        }
      }
    }
  }

  visible.forEach((node) => {
    const yearPosition = node.year ? (node.year - minYear) / yearSpan : 0.5;
    const desiredX = 90 + yearPosition * Math.max(260, width - 180);
    const desiredY = height / 2;
    if (!node.fixed) {
      node.vx += (desiredX - node.x) * 0.002;
      node.vy += (desiredY - node.y) * 0.0015;
      node.vx *= 0.86;
      node.vy *= 0.86;
      node.x += node.vx;
      node.y += node.vy;
      node.x = Math.max(36, Math.min(width - 36, node.x));
      node.y = Math.max(44, Math.min(height - 36, node.y));
    }
  });

  model.nodes.forEach((node) => {
    if (!visibleSet.has(node.id)) {
      node.vx *= 0.75;
      node.vy *= 0.75;
    }
  });
}

export function influenceEndpoints(edge: RuntimeEdge): [RuntimeNode, RuntimeNode] {
  const citing = edge.sourceNode;
  const cited = edge.targetNode;
  const citingTime = timeSortValue(citing);
  const citedTime = timeSortValue(cited);

  if (citedTime < citingTime) return [cited, citing];
  if (citingTime < citedTime) return [citing, cited];
  return [cited, citing];
}

export function edgePath(edge: RuntimeEdge, layoutMode: "tech" | "map"): string {
  if (layoutMode === "map") {
    return `M ${edge.sourceNode.x} ${edge.sourceNode.y} L ${edge.targetNode.x} ${edge.targetNode.y}`;
  }

  const [from, to] = influenceEndpoints(edge);
  const startX = from.x + from.cardWidth;
  const startY = from.y + from.cardHeight / 2;
  const endX = to.x;
  const endY = to.y + to.cardHeight / 2;
  const distance = endX - startX;
  const bend = Math.max(54, Math.abs(distance) / 2);
  return `M ${startX} ${startY} C ${startX + bend} ${startY}, ${endX - bend} ${endY}, ${endX} ${endY}`;
}

export function relatedEdges(model: GraphModel, nodeId: string): RuntimeEdge[] {
  return model.edges
    .filter((edge) => edge.source === nodeId || edge.target === nodeId)
    .sort((a, b) => {
      if (a.kind !== b.kind) return a.kind === "bibliography" ? -1 : 1;
      const aOther = model.nodeById.get(a.target === nodeId ? a.source : a.target);
      const bOther = model.nodeById.get(b.target === nodeId ? b.source : b.target);
      return (aOther?.title || "").localeCompare(bOther?.title || "");
    });
}
