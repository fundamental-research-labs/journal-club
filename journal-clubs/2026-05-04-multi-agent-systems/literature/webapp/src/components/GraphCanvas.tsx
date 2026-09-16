import { useEffect, useMemo, useRef, useState } from "react";
import type { PointerEvent as ReactPointerEvent, RefObject, WheelEvent as ReactWheelEvent } from "react";

import { edgePath, selectedNeighborIds, shortTitle, statusColor, tickMap, wrapTitle } from "../domain/graphModel";
import type { RuntimeNode, TaxonomyTerm, TechLayout } from "../domain/types";
import { cx } from "../lib/classNames";
import { useGraphStore } from "../store/graphStore";

interface GraphCanvasProps {
  stageRef: RefObject<HTMLDivElement | null>;
}

interface DragState {
  nodeId: string;
  pointerId: number;
  offsetX: number;
  offsetY: number;
}

interface PanState {
  pointerId: number;
  x: number;
  y: number;
}

const TREE_Y_AXIS_WIDTH = 204;

export function GraphCanvas({ stageRef }: GraphCanvasProps) {
  const svgRef = useRef<SVGSVGElement | null>(null);
  const dragRef = useRef<DragState | null>(null);
  const panRef = useRef<PanState | null>(null);
  const [, setRenderTick] = useState(0);
  const [scrollPosition, setScrollPosition] = useState({ left: 0, top: 0 });

  const model = useGraphStore((state) => state.model);
  const layoutMode = useGraphStore((state) => state.layoutMode);
  const visibleNodeIds = useGraphStore((state) => state.visibleNodeIds);
  const visibleEdges = useGraphStore((state) => state.visibleEdges);
  const selectedId = useGraphStore((state) => state.selectedId);
  const canvasWidth = useGraphStore((state) => state.canvasWidth);
  const canvasHeight = useGraphStore((state) => state.canvasHeight);
  const viewportWidth = useGraphStore((state) => state.viewportWidth);
  const viewportHeight = useGraphStore((state) => state.viewportHeight);
  const panX = useGraphStore((state) => state.panX);
  const panY = useGraphStore((state) => state.panY);
  const scale = useGraphStore((state) => state.scale);
  const techLayout = useGraphStore((state) => state.techLayout);
  const setViewport = useGraphStore((state) => state.setViewport);
  const selectNode = useGraphStore((state) => state.selectNode);
  const clearSelection = useGraphStore((state) => state.clearSelection);
  const fitGraph = useGraphStore((state) => state.fitGraph);

  const visibleNodes = useMemo(
    () => model.nodes.filter((node) => visibleNodeIds.has(node.id)),
    [model.nodes, visibleNodeIds],
  );
  const neighbors = useMemo(() => selectedNeighborIds(selectedId, model.edges), [model.edges, selectedId]);
  const labelThreshold = visibleNodes.length <= 55;

  useEffect(() => {
    const stage = stageRef.current;
    if (!stage) return;

    const observer = new ResizeObserver(([entry]) => {
      const rect = entry.contentRect;
      setViewport(rect.width, rect.height);
    });
    observer.observe(stage);
    return () => observer.disconnect();
  }, [setViewport, stageRef]);

  useEffect(() => {
    const stage = stageRef.current;
    if (!stage) return;

    const syncScroll = () => {
      setScrollPosition({ left: stage.scrollLeft, top: stage.scrollTop });
    };

    syncScroll();
    stage.addEventListener("scroll", syncScroll, { passive: true });
    return () => stage.removeEventListener("scroll", syncScroll);
  }, [stageRef]);

  useEffect(() => {
    const timer = window.setTimeout(() => fitGraph(stageRef.current), layoutMode === "tech" ? 120 : 180);
    return () => window.clearTimeout(timer);
  }, [fitGraph, layoutMode, stageRef]);

  useEffect(() => {
    let frameId = 0;
    const loop = () => {
      const state = useGraphStore.getState();
      if (state.layoutMode === "map") {
        tickMap(state.model, state.visibleNodeIds, state.visibleEdges, state.canvasWidth, state.canvasHeight);
        setRenderTick((tick) => (tick + 1) % 100000);
      }
      frameId = window.requestAnimationFrame(loop);
    };
    frameId = window.requestAnimationFrame(loop);
    return () => window.cancelAnimationFrame(frameId);
  }, []);

  const screenToGraph = (clientX: number, clientY: number) => {
    const svg = svgRef.current;
    const state = useGraphStore.getState();
    if (!svg) return { x: 0, y: 0 };
    const rect = svg.getBoundingClientRect();
    return {
      x: (clientX - rect.left - state.panX) / state.scale,
      y: (clientY - rect.top - state.panY) / state.scale,
    };
  };

  const startNodeDrag = (event: ReactPointerEvent<SVGGElement>, node: RuntimeNode) => {
    if (layoutMode === "tech") return;
    event.preventDefault();
    event.stopPropagation();
    const point = screenToGraph(event.clientX, event.clientY);
    node.fixed = true;
    dragRef.current = {
      nodeId: node.id,
      pointerId: event.pointerId,
      offsetX: node.x - point.x,
      offsetY: node.y - point.y,
    };
    svgRef.current?.setPointerCapture(event.pointerId);
  };

  const handleSvgPointerDown = (event: ReactPointerEvent<SVGSVGElement>) => {
    if (layoutMode === "tech") return;
    if (event.target instanceof Element && event.target.closest(".node")) return;
    panRef.current = { pointerId: event.pointerId, x: event.clientX, y: event.clientY };
    svgRef.current?.setPointerCapture(event.pointerId);
  };

  const handleSvgPointerMove = (event: ReactPointerEvent<SVGSVGElement>) => {
    if (layoutMode === "tech") return;
    const state = useGraphStore.getState();
    const drag = dragRef.current;
    if (drag) {
      const node = state.model.nodeById.get(drag.nodeId);
      if (!node) return;
      const point = screenToGraph(event.clientX, event.clientY);
      node.x = point.x + drag.offsetX;
      node.y = point.y + drag.offsetY;
      node.vx = 0;
      node.vy = 0;
      setRenderTick((tick) => (tick + 1) % 100000);
      return;
    }

    const pan = panRef.current;
    if (pan) {
      state.panBy(event.clientX - pan.x, event.clientY - pan.y);
      panRef.current = { ...pan, x: event.clientX, y: event.clientY };
    }
  };

  const finishPointer = (event: ReactPointerEvent<SVGSVGElement>) => {
    const state = useGraphStore.getState();
    if (dragRef.current) {
      const node = state.model.nodeById.get(dragRef.current.nodeId);
      if (node) node.fixed = false;
      dragRef.current = null;
    }
    panRef.current = null;
    try {
      svgRef.current?.releasePointerCapture(event.pointerId);
    } catch {
      // Browsers can release captures implicitly.
    }
  };

  const handleWheel = (event: ReactWheelEvent<SVGSVGElement>) => {
    if (layoutMode === "tech") return;
    event.preventDefault();
    const before = screenToGraph(event.clientX, event.clientY);
    const state = useGraphStore.getState();
    const nextScale = Math.max(0.35, Math.min(2.6, state.scale * (event.deltaY > 0 ? 0.9 : 1.1)));
    const rect = svgRef.current?.getBoundingClientRect();
    if (!rect) return;
    state.setPanZoom(
      event.clientX - rect.left - before.x * nextScale,
      event.clientY - rect.top - before.y * nextScale,
      nextScale,
    );
  };

  const viewportTransform = layoutMode === "tech" ? "translate(0, 0) scale(1)" : `translate(${panX}, ${panY}) scale(${scale})`;

  return (
    <section
      ref={stageRef}
      className={cx("graph-stage", layoutMode === "tech" ? "tech-mode" : "map-mode")}
      aria-label="Citation graph"
    >
      {layoutMode === "tech" && techLayout ? (
        <TreeAxes
          layout={techLayout}
          canvasWidth={canvasWidth}
          canvasHeight={canvasHeight}
          viewportWidth={viewportWidth}
          viewportHeight={viewportHeight}
          lanes={model.lanes}
          scrollLeft={scrollPosition.left}
          scrollTop={scrollPosition.top}
        />
      ) : null}

      <div
        className={cx(
          "absolute z-30 flex max-w-[calc(100%-1.5rem)] flex-wrap gap-2 rounded-md border border-slate-200 bg-white/90 px-2 py-1.5 text-xs text-slate-500 shadow-lg",
          layoutMode === "tech" ? "left-[13rem] top-12" : "left-3 top-3",
        )}
      >
        <span>
          <i className="legend-line bib" /> bibliography
        </span>
        <span>
          <i className="legend-line mention" /> notes
        </span>
        <span>
          <i className="legend-dot" /> paper
        </span>
      </div>

      <svg
        ref={svgRef}
        id="graph"
        role="img"
        aria-label="Interactive citation graph"
        viewBox={`0 0 ${canvasWidth} ${canvasHeight}`}
        style={layoutMode === "tech" ? { width: `${canvasWidth}px`, height: `${canvasHeight}px` } : undefined}
        onPointerDown={handleSvgPointerDown}
        onPointerMove={handleSvgPointerMove}
        onPointerUp={finishPointer}
        onPointerCancel={finishPointer}
        onClick={(event) => {
          if (event.target === svgRef.current) clearSelection();
        }}
        onWheel={handleWheel}
      >
        <g transform={viewportTransform}>
          {layoutMode === "tech" && techLayout ? (
            <TimelineGuides layout={techLayout} canvasHeight={canvasHeight} lanes={model.lanes} />
          ) : null}
          <g>
            {visibleEdges.map((edge, index) => (
              <path
                key={`${layoutMode}:${edge.source}->${edge.target}:${edge.kind}:${index}`}
                className={cx(
                  "edge",
                  edge.kind,
                  selectedId && (edge.source === selectedId || edge.target === selectedId) && "highlight",
                  selectedId && !neighbors.has(edge.source) && !neighbors.has(edge.target) && "dimmed",
                )}
                d={edgePath(edge, layoutMode)}
              />
            ))}
          </g>
          <g>
            {visibleNodes.map((node) => (
              <g
                key={`${layoutMode}:${node.id}`}
                className={cx(
                  "node",
                  layoutMode === "tech" ? "tech-node" : "map-node",
                  node.id === selectedId && "selected",
                  selectedId && !neighbors.has(node.id) && "dimmed",
                )}
                transform={`translate(${node.x}, ${node.y})`}
                onPointerDown={(event) => startNodeDrag(event, node)}
                onClick={(event) => {
                  event.stopPropagation();
                  selectNode(node.id);
                }}
              >
                <title>{node.title}</title>
                {layoutMode === "tech" ? (
                  <TechNode node={node} />
                ) : (
                  <MapNode node={node} selectedId={selectedId} labelThreshold={labelThreshold} neighbors={neighbors} />
                )}
              </g>
            ))}
          </g>
        </g>
      </svg>

      {visibleNodeIds.size === 0 ? (
        <div className="absolute left-1/2 top-1/2 rounded-md border border-slate-200 bg-white px-3.5 py-3 text-sm text-slate-500 shadow-sm [transform:translate(-50%,-50%)]">
          No papers match these filters.
        </div>
      ) : null}
    </section>
  );
}

function TreeAxes({
  layout,
  canvasWidth,
  canvasHeight,
  viewportWidth,
  viewportHeight,
  lanes,
  scrollLeft,
  scrollTop,
}: {
  layout: TechLayout;
  canvasWidth: number;
  canvasHeight: number;
  viewportWidth: number;
  viewportHeight: number;
  lanes: TaxonomyTerm[];
  scrollLeft: number;
  scrollTop: number;
}) {
  return (
    <div className="tree-axis-layer" aria-hidden="true">
      <div className="tree-axis-x" style={{ width: viewportWidth }}>
        <svg
          width={canvasWidth}
          height="44"
          viewBox={`0 0 ${canvasWidth} 44`}
          style={{ transform: `translateX(${-scrollLeft}px)` }}
        >
          {layout.years.map((year, index) => {
            const x = layout.marginX + index * layout.yearWidth;
            const labelX = x + layout.yearWidth / 2;
            return (
              <g key={year}>
                <line className="tree-axis-tick" x1={x} x2={x} y1={30} y2={44} />
                <text className="tree-axis-label" x={labelX} y={25} textAnchor="middle">
                  {year}
                </text>
              </g>
            );
          })}
        </svg>
      </div>

      <div className="tree-axis-y" style={{ width: TREE_Y_AXIS_WIDTH, height: viewportHeight }}>
        <svg
          width={TREE_Y_AXIS_WIDTH}
          height={canvasHeight}
          viewBox={`0 0 ${TREE_Y_AXIS_WIDTH} ${canvasHeight}`}
          style={{ transform: `translateY(${-scrollTop}px)` }}
        >
          {lanes.map((lane, index) => {
            const y = layout.laneTops[index] - 15;
            return (
              <g key={lane.id}>
                <line className="tree-axis-lane-rule" x1={0} x2={TREE_Y_AXIS_WIDTH} y1={y} y2={y} />
                <text className="tree-axis-lane-label" x={12} y={y - 7}>
                  {lane.label}
                </text>
              </g>
            );
          })}
        </svg>
      </div>
    </div>
  );
}

function TimelineGuides({
  layout,
  canvasHeight,
  lanes,
}: {
  layout: TechLayout;
  canvasHeight: number;
  lanes: TaxonomyTerm[];
}) {
  const endY = Math.max(layout.height, canvasHeight);
  return (
    <g>
      {layout.years.map((year, index) => {
        const x = layout.marginX + index * layout.yearWidth;
        return (
          <g key={year} className="year-column">
            <line x1={x} x2={x} y1={34} y2={endY} />
          </g>
        );
      })}
      {lanes.map((lane, index) => {
        const y = layout.laneTops[index] - 15;
        return (
          <g key={lane.id}>
            <line className="lane-guide" x1={28} x2={layout.width} y1={y} y2={y} />
          </g>
        );
      })}
    </g>
  );
}

function TechNode({ node }: { node: RuntimeNode }) {
  return (
    <>
      <rect className="card" width={node.cardWidth} height={node.cardHeight} rx={6} />
      <rect className="status-strip" width={6} height={node.cardHeight} rx={3} fill={statusColor(node.status)} />
      <text className="card-title" x={14} y={19}>
        {wrapTitle(node.title).map((line, lineIndex) => (
          <tspan key={`${line}-${lineIndex}`} x={14} dy={lineIndex === 0 ? 0 : 13}>
            {line}
          </tspan>
        ))}
      </text>
      <text className="card-meta" x={14} y={node.cardHeight - 12}>
        {[node.date || node.year || "n.d.", node.status, `${node.inDegree} in/${node.outDegree} out`]
          .filter(Boolean)
          .join(" · ")}
      </text>
    </>
  );
}

function MapNode({
  node,
  selectedId,
  labelThreshold,
  neighbors,
}: {
  node: RuntimeNode;
  selectedId: string | null;
  labelThreshold: boolean;
  neighbors: Set<string>;
}) {
  const shouldLabel = labelThreshold || node.degree >= 4 || node.id === selectedId || neighbors.has(node.id);
  return (
    <>
      <circle r={node.radius} fill={statusColor(node.status)} />
      <text x={11} y={4}>
        {shouldLabel ? shortTitle(node.title, 28) : ""}
      </text>
    </>
  );
}
