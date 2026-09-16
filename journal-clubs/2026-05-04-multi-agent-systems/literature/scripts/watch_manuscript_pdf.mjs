#!/usr/bin/env node

import { spawn } from "node:child_process";
import { existsSync, watch } from "node:fs";
import path from "node:path";
import process from "node:process";

const repoRoot = process.cwd();
const manuscriptDir = path.join(repoRoot, "manuscript", "multi-agent-review-draft");
const entrypoint = path.join(manuscriptDir, "index.qmd");
const outputPdf = path.join(manuscriptDir, "build", "index.pdf");
const debounceMs = 350;
const debug = process.env.PDF_WATCH_DEBUG === "1";

const ignoredPathParts = new Set([
  ".quarto",
  "build",
  ".git",
  "index_files",
  "node_modules",
]);

const ignoredFilenames = new Set([
  "index.pdf",
  "index.typ",
]);

let building = false;
let rerunRequested = false;
let debounceTimer = null;
let watcher = null;

function relative(filePath) {
  return path.relative(repoRoot, filePath) || ".";
}

function timestamp() {
  return new Date().toLocaleTimeString([], {
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  });
}

function shouldIgnore(filePath) {
  const relativePath = path.relative(manuscriptDir, filePath);

  if (!relativePath || relativePath.startsWith("..")) {
    return false;
  }

  const pathParts = relativePath.split(path.sep);
  const basename = pathParts.at(-1);

  return (
    ignoredFilenames.has(basename) ||
    pathParts.some((part) => ignoredPathParts.has(part))
  );
}

function runBuild(reason = "initial build") {
  if (building) {
    rerunRequested = true;
    return;
  }

  building = true;
  rerunRequested = false;

  console.log(`[${timestamp()}] Rendering PDF (${reason})`);

  const child = spawn(
    "quarto",
    ["render", entrypoint, "--to", "typst"],
    {
      cwd: repoRoot,
      stdio: "inherit",
    },
  );

  child.on("close", (code) => {
    building = false;

    if (code === 0) {
      console.log(`[${timestamp()}] PDF ready: ${relative(outputPdf)}`);
    } else {
      console.log(`[${timestamp()}] Render failed with exit code ${code}`);
    }

    if (rerunRequested) {
      runBuild("changes saved during previous render");
    }
  });
}

function scheduleBuild(reason) {
  if (debug) {
    console.log(`[watch] queued: ${reason}`);
  }

  clearTimeout(debounceTimer);
  debounceTimer = setTimeout(() => runBuild(reason), debounceMs);
}

function startWatcher() {
  if (!existsSync(entrypoint)) {
    console.error(`Cannot find manuscript entrypoint: ${relative(entrypoint)}`);
    process.exit(1);
  }

  watcher = watch(
    manuscriptDir,
    {
      recursive: true,
      persistent: true,
    },
    (_eventType, filename) => {
      if (!filename) {
        scheduleBuild("manuscript changed");
        return;
      }

      const filenamePath = filename.toString();
      const changedPath = path.isAbsolute(filenamePath)
        ? filenamePath
        : path.join(manuscriptDir, filenamePath);

      if (shouldIgnore(changedPath)) {
        if (debug) {
          console.log(`[watch] ignored: ${relative(changedPath)}`);
        }
        return;
      }

      scheduleBuild(`${relative(changedPath)} changed`);
    },
  );

  watcher.on("error", (error) => {
    console.error(`File watcher failed: ${error.message}`);
    process.exit(1);
  });

  console.log(`Watching ${relative(manuscriptDir)} for PDF changes`);
  console.log("Press Ctrl-C to stop.");
  runBuild();
}

process.on("SIGINT", () => {
  watcher?.close();
  process.exit(0);
});

startWatcher();
