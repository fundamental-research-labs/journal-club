import { useRef } from "react";

import { DetailsPanel } from "./components/DetailsPanel";
import { GraphCanvas } from "./components/GraphCanvas";
import { Header } from "./components/Header";
import { Sidebar } from "./components/Sidebar";
import { useGraphStore } from "./store/graphStore";

export function App() {
  const stageRef = useRef<HTMLDivElement | null>(null);
  const fitGraph = useGraphStore((state) => state.fitGraph);
  const resetView = useGraphStore((state) => state.resetView);

  return (
    <div className="min-h-screen bg-slate-100 text-slate-950">
      <Header onFit={() => fitGraph(stageRef.current)} onReset={() => resetView(stageRef.current)} />
      <main className="grid h-[calc(100vh-65px)] min-h-[620px] grid-cols-[minmax(250px,300px)_minmax(420px,1fr)_minmax(280px,340px)] max-[1100px]:h-auto max-[1100px]:grid-cols-[minmax(230px,280px)_1fr] max-[1100px]:grid-rows-[minmax(520px,62vh)_auto] max-[760px]:block">
        <Sidebar />
        <GraphCanvas stageRef={stageRef} />
        <DetailsPanel />
      </main>
    </div>
  );
}
