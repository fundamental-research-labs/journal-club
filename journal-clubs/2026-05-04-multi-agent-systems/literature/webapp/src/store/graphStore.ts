import { create } from "zustand";

import graphJson from "../data/graph-data.json";
import {
  applyTechTreeLayout,
  computeVisibility,
  createGraphModel,
  initPositions,
} from "../domain/graphModel";
import type {
  EdgeMode,
  GraphModel,
  LayoutMode,
  LiteratureGraph,
  RuntimeEdge,
  TechLayout,
} from "../domain/types";

interface GraphFields {
  model: GraphModel;
  layoutMode: LayoutMode;
  edgeMode: EdgeMode;
  selectedId: string | null;
  search: string;
  selectedStatuses: Set<string>;
  hideIsolated: boolean;
  showNeighborhood: boolean;
  visibleNodeIds: Set<string>;
  visibleEdges: RuntimeEdge[];
  viewportWidth: number;
  viewportHeight: number;
  canvasWidth: number;
  canvasHeight: number;
  panX: number;
  panY: number;
  scale: number;
  techLayout: TechLayout | null;
}

interface GraphActions {
  setSearch: (search: string) => void;
  setStatus: (status: string, enabled: boolean) => void;
  setEdgeMode: (edgeMode: EdgeMode) => void;
  setHideIsolated: (hideIsolated: boolean) => void;
  setShowNeighborhood: (showNeighborhood: boolean) => void;
  setLayoutMode: (layoutMode: LayoutMode) => void;
  selectNode: (selectedId: string | null) => void;
  clearSelection: () => void;
  setViewport: (width: number, height: number) => void;
  panBy: (dx: number, dy: number) => void;
  setPanZoom: (panX: number, panY: number, scale: number) => void;
  resetView: (stage?: HTMLElement | null) => void;
  fitGraph: (stage?: HTMLElement | null) => void;
}

export type GraphStore = GraphFields & GraphActions;

type DerivedInput = Pick<
  GraphFields,
  | "model"
  | "layoutMode"
  | "edgeMode"
  | "selectedId"
  | "search"
  | "selectedStatuses"
  | "hideIsolated"
  | "showNeighborhood"
  | "viewportWidth"
  | "viewportHeight"
  | "techLayout"
>;

function canvasSize(
  layoutMode: LayoutMode,
  viewportWidth: number,
  viewportHeight: number,
  techLayout: TechLayout | null,
): Pick<GraphFields, "canvasWidth" | "canvasHeight"> {
  if (layoutMode !== "tech") {
    return { canvasWidth: viewportWidth, canvasHeight: viewportHeight };
  }

  return {
    canvasWidth: Math.max(viewportWidth, Math.ceil(techLayout?.width || viewportWidth)),
    canvasHeight: Math.max(viewportHeight, Math.ceil(techLayout?.height || viewportHeight)),
  };
}

function deriveGraphState(state: DerivedInput): Pick<
  GraphFields,
  "visibleNodeIds" | "visibleEdges" | "techLayout" | "canvasWidth" | "canvasHeight"
> {
  const visibility = computeVisibility(state.model, {
    edgeMode: state.edgeMode,
    selectedStatuses: state.selectedStatuses,
    search: state.search,
    hideIsolated: state.hideIsolated,
    showNeighborhood: state.showNeighborhood,
    selectedId: state.selectedId,
  });

  const techLayout =
    state.layoutMode === "tech" ? applyTechTreeLayout(state.model, visibility.visibleNodeIds) : state.techLayout;
  return {
    ...visibility,
    techLayout,
    ...canvasSize(state.layoutMode, state.viewportWidth, state.viewportHeight, techLayout),
  };
}

function patchWithDerived(state: GraphStore, patch: Partial<GraphFields>): Partial<GraphStore> {
  const next = { ...state, ...patch };
  return {
    ...patch,
    ...deriveGraphState(next),
  };
}

const model = createGraphModel(graphJson as unknown as LiteratureGraph);
const initialFields: Omit<GraphFields, "visibleNodeIds" | "visibleEdges" | "canvasWidth" | "canvasHeight"> & {
  visibleNodeIds?: Set<string>;
  visibleEdges?: RuntimeEdge[];
  canvasWidth?: number;
  canvasHeight?: number;
} = {
  model,
  layoutMode: "tech",
  edgeMode: "all",
  selectedId: null,
  search: "",
  selectedStatuses: new Set(model.statuses),
  hideIsolated: false,
  showNeighborhood: false,
  viewportWidth: 800,
  viewportHeight: 600,
  panX: 0,
  panY: 0,
  scale: 1,
  techLayout: null,
};

const initialDerived = deriveGraphState(initialFields as DerivedInput);

export const useGraphStore = create<GraphStore>((set, get) => ({
  ...(initialFields as GraphFields),
  ...initialDerived,

  setSearch: (search) => set((state) => patchWithDerived(state, { search })),

  setStatus: (status, enabled) =>
    set((state) => {
      const selectedStatuses = new Set(state.selectedStatuses);
      if (enabled) {
        selectedStatuses.add(status);
      } else {
        selectedStatuses.delete(status);
      }
      return patchWithDerived(state, { selectedStatuses });
    }),

  setEdgeMode: (edgeMode) => set((state) => patchWithDerived(state, { edgeMode })),

  setHideIsolated: (hideIsolated) => set((state) => patchWithDerived(state, { hideIsolated })),

  setShowNeighborhood: (showNeighborhood) =>
    set((state) => patchWithDerived(state, { showNeighborhood: showNeighborhood && Boolean(state.selectedId) })),

  setLayoutMode: (layoutMode) =>
    set((state) => {
      if (layoutMode === "map") {
        initPositions(state.model, state.viewportWidth, state.viewportHeight);
      }
      state.model.nodes.forEach((node) => {
        node.fixed = false;
      });
      return patchWithDerived(state, { layoutMode, panX: 0, panY: 0, scale: 1 });
    }),

  selectNode: (selectedId) => set((state) => patchWithDerived(state, { selectedId })),

  clearSelection: () => set((state) => patchWithDerived(state, { selectedId: null, showNeighborhood: false })),

  setViewport: (width, height) =>
    set((state) =>
      patchWithDerived(state, {
        viewportWidth: Math.max(320, width),
        viewportHeight: Math.max(320, height),
      }),
    ),

  panBy: (dx, dy) => set((state) => ({ panX: state.panX + dx, panY: state.panY + dy })),

  setPanZoom: (panX, panY, scale) => set({ panX, panY, scale }),

  resetView: (stage) => {
    const state = get();
    state.model.nodes.forEach((node) => {
      node.fixed = false;
    });
    if (state.layoutMode === "tech") {
      stage?.scrollTo({ left: 0, top: 0, behavior: "smooth" });
    }
    set({ panX: 0, panY: 0, scale: 1 });
  },

  fitGraph: (stage) => {
    const state = get();
    const visible = state.model.nodes.filter((node) => state.visibleNodeIds.has(node.id));
    if (!visible.length) return;

    if (state.layoutMode === "tech") {
      const selected = state.selectedId ? state.model.nodeById.get(state.selectedId) : null;
      if (selected && state.visibleNodeIds.has(selected.id)) {
        stage?.scrollTo({
          left: Math.max(0, selected.x - state.viewportWidth / 2 + selected.cardWidth / 2),
          top: Math.max(0, selected.y - state.viewportHeight / 2 + selected.cardHeight / 2),
          behavior: "smooth",
        });
      } else {
        stage?.scrollTo({ left: 0, top: 0, behavior: "smooth" });
      }
      return;
    }

    const bounds = visible.map((node) => ({
      minX: node.x - node.radius,
      maxX: node.x + node.radius,
      minY: node.y - node.radius,
      maxY: node.y + node.radius,
    }));
    const minX = Math.min(...bounds.map((bound) => bound.minX));
    const maxX = Math.max(...bounds.map((bound) => bound.maxX));
    const minY = Math.min(...bounds.map((bound) => bound.minY));
    const maxY = Math.max(...bounds.map((bound) => bound.maxY));
    const graphWidth = Math.max(1, maxX - minX);
    const graphHeight = Math.max(1, maxY - minY);
    const scale = Math.min(
      1.8,
      Math.max(0.22, Math.min((state.canvasWidth - 80) / graphWidth, (state.canvasHeight - 80) / graphHeight)),
    );
    set({
      scale,
      panX: (state.canvasWidth - graphWidth * scale) / 2 - minX * scale,
      panY: (state.canvasHeight - graphHeight * scale) / 2 - minY * scale,
    });
  },
}));
