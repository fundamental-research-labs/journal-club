import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";
import { defineConfig } from "vite";

const repoRoot = new URL("..", import.meta.url).pathname.replace(/\/$/, "");

export default defineConfig({
  base: "./",
  define: {
    __LITERATURE_REPO_ROOT__: JSON.stringify(repoRoot),
  },
  plugins: [react(), tailwindcss()],
  server: {
    fs: {
      allow: [repoRoot],
    },
  },
});
