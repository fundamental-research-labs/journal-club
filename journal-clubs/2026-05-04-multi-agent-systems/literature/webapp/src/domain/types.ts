export type EdgeKind = "bibliography" | "curated-mention";
export type EdgeMode = "all" | EdgeKind;
export type LayoutMode = "tech" | "map";

export interface EdgeEvidence {
  file?: string;
  matchedBy?: string;
  matchedValue?: string;
  reference?: string;
}

export interface PaperPaths {
  folder: string;
  metadata: string;
  summary: string;
  notes: string;
  claims: string;
  pdf: string;
}

export interface PaperClassification {
  primarySubarea: string;
  primarySubareaLabel: string;
  secondarySubareas: string[];
  seedSubarea: string;
  role: string;
  roleLabel: string;
  artifactType: string;
  artifactTypeLabel: string;
  domains: string[];
  source: string;
  confidence: string;
}

export interface PaperNode {
  id: string;
  folder: string;
  slug: string;
  title: string;
  authors: string[];
  arxiv: string;
  date: string;
  year: number | null;
  venue: string;
  status: string;
  topics: string[];
  summary: string;
  classification: PaperClassification;
  paths: PaperPaths;
  bibliographyFiles: string[];
}

export interface GraphEdge {
  source: string;
  target: string;
  kind: EdgeKind;
  evidence: EdgeEvidence[];
}

export interface GraphStats {
  paperCount: number;
  edgeCount: number;
  bibliographyEdgeCount: number;
  curatedMentionEdgeCount: number;
  isolatedPaperCount: number;
  yearRange: number[];
  statuses: Record<string, number>;
  topTopics: Array<[string, number]>;
  subareas: Record<string, number>;
  roles: Record<string, number>;
  artifactTypes: Record<string, number>;
}

export interface TaxonomyTerm {
  id: string;
  label: string;
  description?: string;
}

export interface Taxonomy {
  version: number;
  default_subarea: string;
  subareas: TaxonomyTerm[];
  roles: TaxonomyTerm[];
  artifact_types: TaxonomyTerm[];
  domains: TaxonomyTerm[];
  classification_policy?: string[];
}

export interface LiteratureGraph {
  generatedAt: string;
  source: string;
  taxonomy: Taxonomy;
  nodes: PaperNode[];
  edges: GraphEdge[];
  stats: GraphStats;
}

export interface RuntimeNode extends PaperNode {
  index: number;
  x: number;
  y: number;
  vx: number;
  vy: number;
  radius: number;
  cardWidth: number;
  cardHeight: number;
  lane: number;
  row: number;
  degree: number;
  inDegree: number;
  outDegree: number;
  bibliographyDegree: number;
  mentionDegree: number;
  baseX: number;
  fixed: boolean;
}

export interface RuntimeEdge extends GraphEdge {
  sourceNode: RuntimeNode;
  targetNode: RuntimeNode;
}

export interface GraphModel {
  data: LiteratureGraph;
  nodes: RuntimeNode[];
  edges: RuntimeEdge[];
  nodeById: Map<string, RuntimeNode>;
  statuses: string[];
  lanes: TaxonomyTerm[];
}

export interface DateParts {
  year: number | null;
  month: number;
}

export interface TechLayout {
  years: number[];
  minYear: number;
  maxYear: number;
  laneTops: number[];
  laneHeights: number[];
  laneHeight: number;
  yearWidth: number;
  marginX: number;
  width: number;
  height: number;
}
