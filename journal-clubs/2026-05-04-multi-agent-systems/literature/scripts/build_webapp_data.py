#!/usr/bin/env python3
"""Build static data for the literature navigation webapp.

The citation graph is intentionally local-first: it links papers in this repo
when a local bibliography entry, bbl item, or curated note mentions another
paper already present in papers/.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PAPERS_DIR = ROOT / "papers"
OUTPUT = ROOT / "webapp" / "src" / "data" / "graph-data.json"
SEEDS_PATH = ROOT / "docs" / "seeds.md"
TAXONOMY_PATH = ROOT / "docs" / "taxonomy.yaml"

DEFAULT_TAXONOMY: dict[str, Any] = {
    "version": 1,
    "default_subarea": "needs-classification",
    "subareas": [
        {"id": "llm-mas-coordination", "label": "LLM MAS & Coordination"},
        {"id": "debate-reasoning", "label": "Debate & Reasoning"},
        {"id": "software-web-computer-use", "label": "Software, Web & Computer-Use"},
        {"id": "benchmarks-evaluation", "label": "Benchmarks & Evaluation"},
        {"id": "science-domain-agents", "label": "Science & Domain Agents"},
        {"id": "safety-reliability", "label": "Safety & Reliability"},
        {"id": "marl-foundations", "label": "MARL & Foundations"},
        {"id": "memory-infrastructure", "label": "Memory & Infrastructure"},
        {"id": "scaling-optimization", "label": "Scaling & Optimization"},
        {"id": "surveys-taxonomies", "label": "Surveys & Taxonomies"},
        {"id": "needs-classification", "label": "Needs Classification"},
    ],
    "roles": [
        {"id": "core", "label": "Core"},
        {"id": "trend", "label": "Trend"},
        {"id": "bridge", "label": "Bridge"},
        {"id": "anchor", "label": "Anchor"},
        {"id": "survey", "label": "Survey"},
        {"id": "unclassified", "label": "Unclassified"},
    ],
    "artifact_types": [
        {"id": "framework", "label": "Framework/System"},
        {"id": "benchmark", "label": "Benchmark/Dataset"},
        {"id": "method", "label": "Method/Algorithm"},
        {"id": "empirical-study", "label": "Empirical Study"},
        {"id": "survey", "label": "Survey/Taxonomy"},
        {"id": "infrastructure", "label": "Infrastructure/Codebase"},
        {"id": "unclassified", "label": "Unclassified"},
    ],
}

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - the fallback keeps the repo dependency-free.
    yaml = None


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def fallback_yaml(path: Path) -> dict[str, Any]:
    data: dict[str, Any] = {}
    current_key: str | None = None

    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        if raw_line.startswith("  - ") and current_key:
            data.setdefault(current_key, []).append(strip_quotes(raw_line[4:]))
            continue

        if raw_line.startswith("  ") and current_key == "artifacts":
            if ":" in raw_line:
                key, value = raw_line.strip().split(":", 1)
                data.setdefault("artifacts", {})[key.strip()] = strip_quotes(value)
            continue

        if ":" not in raw_line:
            continue

        key, value = raw_line.split(":", 1)
        key = key.strip()
        value = value.strip()
        current_key = key

        if not value:
            if key in {"authors", "topics"}:
                data[key] = []
            elif key == "artifacts":
                data[key] = {}
            else:
                data[key] = []
        else:
            data[key] = strip_quotes(value)

    return data


def load_metadata(path: Path) -> dict[str, Any]:
    if yaml is not None:
        loaded = yaml.safe_load(path.read_text(encoding="utf-8", errors="replace"))
        return loaded or {}
    return fallback_yaml(path)


def load_taxonomy() -> dict[str, Any]:
    if yaml is None or not TAXONOMY_PATH.exists():
        return DEFAULT_TAXONOMY
    loaded = yaml.safe_load(TAXONOMY_PATH.read_text(encoding="utf-8", errors="replace"))
    return loaded or DEFAULT_TAXONOMY


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def clean_latex(text: str) -> str:
    text = re.sub(r"\\url\{([^}]*)\}", r"\1", text)
    text = re.sub(r"\\doi\{([^}]*)\}", r"\1", text)
    text = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?(?:\{([^{}]*)\})?", r"\1", text)
    text = text.replace("{", "").replace("}", "")
    text = text.replace("~", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def normalize(text: str) -> str:
    text = clean_latex(text).lower()
    text = text.replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def year_from_date(value: Any) -> int | None:
    match = re.search(r"(19|20)\d{2}", str(value or ""))
    return int(match.group(0)) if match else None


def coerce_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def taxonomy_labels(taxonomy: dict[str, Any], key: str) -> dict[str, str]:
    return {str(item.get("id")): str(item.get("label") or item.get("id")) for item in taxonomy.get(key, [])}


def parse_seed_index(path: Path) -> dict[str, dict[str, str]]:
    if not path.exists():
        return {}

    index: dict[str, dict[str, str]] = {}
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.startswith("|") or line.startswith("| #") or line.startswith("|---"):
            continue
        columns = [column.strip() for column in line.strip("|").split("|")]
        if len(columns) < 6 or not columns[0].isdigit():
            continue

        paper, year, identifier, subarea, role = columns[1:6]
        entry = {
            "paper": paper,
            "year": year,
            "identifier": identifier,
            "seedSubarea": subarea,
            "role": normalize_role(role),
        }
        if re.fullmatch(r"\d{4}\.\d{4,5}", identifier):
            index[f"arxiv:{identifier}"] = entry
        index[f"title:{normalize(paper)}"] = entry

    return index


def normalize_role(value: Any) -> str:
    role = normalize(str(value or ""))
    return role if role in {"core", "trend", "bridge", "anchor", "survey"} else "unclassified"


def seed_entry_for(metadata: dict[str, Any], seed_index: dict[str, dict[str, str]]) -> dict[str, str] | None:
    arxiv = str(metadata.get("arxiv") or "").strip()
    if arxiv and f"arxiv:{arxiv}" in seed_index:
        return seed_index[f"arxiv:{arxiv}"]

    title = normalize(str(metadata.get("title") or ""))
    if title and f"title:{title}" in seed_index:
        return seed_index[f"title:{title}"]

    return None


def text_has(text: str, *patterns: str) -> bool:
    return any(re.search(pattern, text) for pattern in patterns)


def subarea_from_text(seed_subarea: str, topics: list[str], title: str, summary: str) -> str:
    seed_text = normalize(seed_subarea)
    topic_text = normalize(" ".join(topics))
    full_text = normalize(f"{seed_subarea} {title} {topic_text} {summary}")

    if seed_text:
        if text_has(seed_text, r"\bsurvey\b", r"\btaxonom"):
            return "surveys-taxonomies"
        if text_has(seed_text, r"\bsafety\b", r"\bsecurity\b", r"\bfailure\b", r"\bfail\b", r"\breliab", r"\brisk\b", r"\bdelegation\b", r"\bdegradation\b"):
            return "safety-reliability"
        if text_has(seed_text, r"\bscience\b", r"\bscientific\b", r"\bresearch\b", r"\bexperiment", r"\bmedical\b", r"\bdomain\b", r"\breplication\b"):
            return "science-domain-agents"
        if text_has(seed_text, r"\bsoftware\b", r"\bswe\b", r"\bcoding\b", r"\bcode\b", r"\bweb\b", r"\bbrowser\b", r"\bcomputer use\b", r"\bcomputer-use\b", r"\bmobile\b", r"\bworkplace\b", r"\btool user\b", r"\btool interaction\b"):
            return "software-web-computer-use"
        if text_has(seed_text, r"\bmarl\b", r"\breinforcement\b", r"\bemergent\b", r"\bself play\b", r"\bself-play\b", r"\bsocial dilemma", r"\blearned communication\b", r"\btargeted communication\b", r"\bvalue\b", r"\bpolicy\b", r"\bactor critic\b", r"\bcredit assignment\b", r"\bpopulation\b", r"\bleague\b"):
            return "marl-foundations"
        if text_has(seed_text, r"\bbenchmark\b", r"\bevaluation\b", r"\bdataset\b", r"\bbench\b"):
            return "benchmarks-evaluation"
        if text_has(seed_text, r"\bmemory\b", r"\btool use\b", r"\btool-use\b", r"\bfoundation\b", r"\binfrastructure\b", r"\becosystem\b", r"\binterface\b"):
            return "memory-infrastructure"
        if text_has(seed_text, r"\bscaling\b", r"\bdiversity\b", r"\barchitecture search\b", r"\boptimization\b", r"\btopolog", r"\btraining\b", r"\btest time\b", r"\btest-time\b"):
            return "scaling-optimization"
        if text_has(seed_text, r"\bdebate\b", r"\breasoning\b", r"\baggregation\b", r"\bfactuality\b", r"\bdeliberat"):
            return "debate-reasoning"
        if text_has(seed_text, r"\bframework\b", r"\bplatform\b", r"\bcoordination\b", r"\bcollaboration\b", r"\borchestration\b", r"\bconversation\b", r"\bcommunication\b", r"\bsociety\b", r"\bsimulation\b", r"\bgeneration\b", r"\bmas\b", r"\bmulti agent\b"):
            return "llm-mas-coordination"

    if text_has(full_text, r"\bsurvey\b", r"\btaxonom"):
        return "surveys-taxonomies"
    if text_has(full_text, r"\bsafety\b", r"\bsecurity\b", r"\bfailure\b", r"\bfail\b", r"\breliab", r"\brisk\b", r"\bexploit", r"\bvulnerab", r"\bdelegate\b", r"\bdegradation\b", r"\bcorrupt"):
        return "safety-reliability"
    if text_has(full_text, r"\bscience\b", r"\bscientific\b", r"\bresearch\b", r"\bexperiment", r"\bmedical\b", r"\bhospital\b", r"\bbiomedical\b", r"\bpaperbench\b", r"\bmlgym\b"):
        return "science-domain-agents"
    if text_has(full_text, r"\bswe\b", r"\bsoftware\b", r"\bcoding\b", r"\bcode\b", r"\brepo", r"\bgithub\b", r"\bprogram repair\b", r"\bweb\b", r"\bbrowser\b", r"\bcomputer use\b", r"\bcomputer-use\b", r"\bmobile\b", r"\bandroid\b", r"\bworkplace\b", r"\bgui\b", r"\bui\b", r"\bdesktop\b", r"\btool user\b"):
        return "software-web-computer-use"
    if text_has(full_text, r"\bmarl\b", r"\bmulti agent reinforcement\b", r"\breinforcement learning\b", r"\bemergent\b", r"\bself play\b", r"\bself-play\b", r"\bsocial dilemma", r"\bmarkov game", r"\bvalue factor", r"\bpolicy gradient", r"\bactor critic", r"\bcentralized training", r"\bdecentralized execution", r"\bstarcraft\b", r"\bdota\b", r"\bcommunication with backpropagation\b"):
        return "marl-foundations"
    if text_has(seed_text, r"\bbenchmark\b", r"\bevaluation\b", r"\bdataset\b", r"\bbench\b") or text_has(topic_text, r"\bagent benchmark", r"\bbenchmark evaluation\b"):
        return "benchmarks-evaluation"
    if text_has(full_text, r"\bmemory\b", r"\bretrieval\b", r"\brag\b", r"\btool use\b", r"\btool-use\b", r"\bruntime\b", r"\binterface\b", r"\binfrastructure\b", r"\becosystem\b", r"\boperating system\b"):
        return "memory-infrastructure"
    if text_has(full_text, r"\bscaling\b", r"\bdiversity\b", r"\barchitecture search\b", r"\boptimization\b", r"\btopolog", r"\bcost\b", r"\bpost training\b", r"\bpost-training\b", r"\btest time\b", r"\btest-time\b", r"\btraining\b"):
        return "scaling-optimization"
    if text_has(full_text, r"\bdebate\b", r"\bdeliberat", r"\breasoning\b", r"\bfactuality\b", r"\baggregation\b", r"\bcollaborative reasoning\b"):
        return "debate-reasoning"
    if text_has(full_text, r"\bframework\b", r"\bplatform\b", r"\borchestration\b", r"\bcollaboration\b", r"\bcoordination\b", r"\bconversation\b", r"\bcommunicative\b", r"\bagent society\b", r"\bsociety\b", r"\bsimulation\b", r"\bgeneration\b", r"\bmulti agent systems\b", r"\bmas\b"):
        return "llm-mas-coordination"

    return "needs-classification"


def infer_artifact_type(seed_subarea: str, topics: list[str], title: str, summary: str) -> str:
    seed_text = normalize(seed_subarea)
    text = normalize(f"{seed_subarea} {title} {' '.join(topics)} {summary}")
    if text_has(seed_text, r"\bsurvey\b", r"\btaxonom"):
        return "survey"
    if text_has(seed_text, r"\bbenchmark\b", r"\bbench\b", r"\bdataset\b", r"\bevaluation\b"):
        return "benchmark"
    if text_has(seed_text, r"\bframework\b", r"\bplatform\b", r"\bsystem\b", r"\bcodebase\b", r"\blaboratory\b", r"\bconstruction\b", r"\bgeneration\b"):
        return "framework"
    if text_has(seed_text, r"\binfrastructure\b", r"\becosystem\b", r"\binterface\b"):
        return "infrastructure"
    if text_has(text, r"\bsurvey\b", r"\btaxonom"):
        return "survey"
    if text_has(text, r"\bbenchmark\b", r"\bbench\b", r"\bdataset\b", r"\bevaluation board\b", r"\benvironment\b", r"\barena\b", r"\bgym\b"):
        return "benchmark"
    if text_has(text, r"\bframework\b", r"\bplatform\b", r"\bsystem\b", r"\becosystem\b", r"\bcodebase\b", r"\blaboratory\b"):
        return "framework"
    if text_has(text, r"\bwhy\b", r"\bfail\b", r"\boutperform\b", r"\bmatter\b", r"\bstudy\b", r"\banalysis\b"):
        return "empirical-study"
    if text_has(text, r"\binfrastructure\b", r"\bruntime\b", r"\binterface\b"):
        return "infrastructure"
    return "method"


def infer_domains(seed_subarea: str, topics: list[str], title: str, summary: str) -> list[str]:
    text = normalize(f"{seed_subarea} {title} {' '.join(topics)} {summary}")
    domains: list[tuple[str, tuple[str, ...]]] = [
        ("software-engineering", (r"\bswe\b", r"\bsoftware\b", r"\bcoding\b", r"\bcode\b", r"\brepo", r"\bgithub\b", r"\bprogram repair\b")),
        ("web", (r"\bweb\b", r"\bbrowser\b")),
        ("computer-use", (r"\bcomputer use\b", r"\bcomputer-use\b", r"\bgui\b", r"\bdesktop\b", r"\bui\b")),
        ("mobile", (r"\bmobile\b", r"\bandroid\b")),
        ("science", (r"\bscience\b", r"\bscientific\b", r"\bresearch\b", r"\bexperiment", r"\bmedical\b", r"\bhospital\b", r"\bbiomedical\b")),
        ("safety", (r"\bsafety\b", r"\bsecurity\b", r"\bfailure\b", r"\bfail\b", r"\brisk\b", r"\bexploit", r"\bvulnerab")),
        ("marl", (r"\bmarl\b", r"\breinforcement learning\b", r"\bself play\b", r"\bself-play\b", r"\bmarkov game", r"\bcentralized training\b")),
        ("memory", (r"\bmemory\b", r"\bretrieval\b", r"\brag\b")),
        ("tool-use", (r"\btool\b", r"\bapi\b")),
        ("multimodal", (r"\bmultimodal\b", r"\bvisual\b", r"\bvision\b")),
        ("simulation", (r"\bsimulation\b", r"\bsimulacrum\b", r"\bsociety\b", r"\bsocial\b")),
        ("reasoning", (r"\breasoning\b", r"\bdebate\b", r"\bdeliberat")),
        ("evaluation", (r"\bbenchmark\b", r"\bevaluation\b", r"\bdataset\b")),
        ("llm-agents", (r"\bllm\b", r"\blanguage model\b", r"\blanguage agents\b")),
    ]
    inferred = [domain for domain, patterns in domains if text_has(text, *patterns)]
    return inferred[:6]


def classify_paper(
    metadata: dict[str, Any],
    seed_index: dict[str, dict[str, str]],
    labels: dict[str, dict[str, str]],
) -> dict[str, Any]:
    explicit = metadata.get("classification")
    if isinstance(explicit, dict):
        seed_subarea = str(explicit.get("seedSubarea") or explicit.get("seed_subarea") or "")
        primary = str(explicit.get("primarySubarea") or explicit.get("primary_subarea") or "")
        role = normalize_role(explicit.get("role"))
        artifact_type = str(explicit.get("artifactType") or explicit.get("artifact_type") or "unclassified")
        secondary = coerce_list(explicit.get("secondarySubareas") or explicit.get("secondary_subareas"))
        domains = coerce_list(explicit.get("domains"))
        source = "metadata"
        confidence = "curated"
    else:
        seed_entry = seed_entry_for(metadata, seed_index)
        seed_subarea = seed_entry["seedSubarea"] if seed_entry else ""
        topics = coerce_list(metadata.get("topics"))
        title = str(metadata.get("title") or "")
        summary = str(metadata.get("summary") or "")
        primary = subarea_from_text(seed_subarea, topics, title, summary)
        role = seed_entry["role"] if seed_entry else "unclassified"
        artifact_type = infer_artifact_type(seed_subarea, topics, title, summary)
        secondary = []
        domains = infer_domains(seed_subarea, topics, title, summary)
        source = "docs/seeds.md" if seed_entry else "metadata-topics"
        confidence = "seed" if seed_entry else ("inferred" if primary != "needs-classification" else "needs-review")

    subarea_labels = labels["subareas"]
    role_labels = labels["roles"]
    artifact_labels = labels["artifact_types"]
    if primary not in subarea_labels:
        primary = "needs-classification"
        confidence = "needs-review"

    return {
        "primarySubarea": primary,
        "primarySubareaLabel": subarea_labels.get(primary, primary),
        "secondarySubareas": [subarea for subarea in secondary if subarea in subarea_labels and subarea != primary],
        "seedSubarea": seed_subarea,
        "role": role,
        "roleLabel": role_labels.get(role, role),
        "artifactType": artifact_type if artifact_type in artifact_labels else "unclassified",
        "artifactTypeLabel": artifact_labels.get(artifact_type, artifact_type),
        "domains": domains,
        "source": source,
        "confidence": confidence,
    }


def paper_root_for(path: Path) -> Path | None:
    try:
        relative = path.relative_to(PAPERS_DIR)
    except ValueError:
        return None
    if not relative.parts:
        return None
    return PAPERS_DIR / relative.parts[0]


def find_arxiv_ids(text: str) -> list[str]:
    patterns = [
        r"arxiv\s*[:/]\s*(\d{4}\.\d{4,5})(?:v\d+)?",
        r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?",
        r"\beprint\s*=\s*[\{\"]?(\d{4}\.\d{4,5})(?:v\d+)?",
    ]
    found: list[str] = []
    for pattern in patterns:
        found.extend(re.findall(pattern, text, flags=re.IGNORECASE))
    return sorted(set(found))


def split_bib_entries(text: str) -> list[str]:
    starts = [match.start() for match in re.finditer(r"@\w+\s*[\{\(]", text)]
    entries: list[str] = []
    for index, start in enumerate(starts):
        end = starts[index + 1] if index + 1 < len(starts) else len(text)
        entries.append(text[start:end].strip())
    return entries


def bib_key(entry: str) -> str:
    match = re.match(r"@\w+\s*[\{\(]\s*([^,\s]+)", entry)
    return match.group(1) if match else ""


def bib_field(entry: str, field: str) -> str:
    match = re.search(rf"\b{re.escape(field)}\s*=", entry, flags=re.IGNORECASE)
    if not match:
        return ""

    index = match.end()
    while index < len(entry) and entry[index].isspace():
        index += 1
    if index >= len(entry):
        return ""

    opener = entry[index]
    if opener in "{(":
        closer = "}" if opener == "{" else ")"
        index += 1
        depth = 1
        start = index
        while index < len(entry):
            char = entry[index]
            if char == opener:
                depth += 1
            elif char == closer:
                depth -= 1
                if depth == 0:
                    return clean_latex(entry[start:index])
            index += 1
    if opener == '"':
        index += 1
        start = index
        while index < len(entry):
            if entry[index] == '"' and entry[index - 1] != "\\":
                return clean_latex(entry[start:index])
            index += 1

    start = index
    while index < len(entry) and entry[index] not in ",\n":
        index += 1
    return clean_latex(entry[start:index])


def iter_bbl_items(text: str) -> list[tuple[str, str, str]]:
    items: list[tuple[str, str, str]] = []
    for chunk in re.split(r"\\bibitem", text):
        if not chunk.strip():
            continue
        key_match = re.search(r"\{([^{}]+)\}", chunk)
        key = key_match.group(1) if key_match else ""
        blocks = re.split(r"\\newblock\s*", chunk)
        title = clean_latex(blocks[1].split("\n", 1)[0]) if len(blocks) > 1 else ""
        items.append((key, title, chunk))
    return items


def build_nodes(
    seed_index: dict[str, dict[str, str]],
    labels: dict[str, dict[str, str]],
) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    nodes: list[dict[str, Any]] = []
    by_folder: dict[str, dict[str, Any]] = {}

    for metadata_path in sorted(PAPERS_DIR.glob("*/metadata.yaml")):
        folder = metadata_path.parent.name
        metadata = load_metadata(metadata_path)
        artifacts = metadata.get("artifacts") or {}
        if not isinstance(artifacts, dict):
            artifacts = {}

        node_id = str(metadata.get("id") or folder)
        title = str(metadata.get("title") or folder.replace("_", " "))
        date = str(metadata.get("date") or "")
        arxiv = str(metadata.get("arxiv") or "").strip()
        topics = coerce_list(metadata.get("topics"))

        node = {
            "id": node_id,
            "folder": folder,
            "slug": folder.rsplit("_", 1)[0],
            "title": title,
            "authors": coerce_list(metadata.get("authors")),
            "arxiv": arxiv,
            "date": date,
            "year": year_from_date(date),
            "venue": str(metadata.get("venue") or ""),
            "status": str(metadata.get("status") or "unspecified"),
            "topics": topics,
            "summary": str(metadata.get("summary") or ""),
            "classification": classify_paper(metadata, seed_index, labels),
            "paths": {
                "folder": rel(metadata_path.parent),
                "metadata": rel(metadata_path),
                "summary": rel(metadata_path.parent / "summary.md"),
                "notes": rel(metadata_path.parent / "notes.md"),
                "claims": rel(metadata_path.parent / "claims.md"),
                "pdf": rel(metadata_path.parent / str(artifacts.get("pdf") or "paper.pdf")),
            },
            "bibliographyFiles": [
                rel(path)
                for path in sorted((metadata_path.parent / "source").glob("**/*"))
                if path.suffix.lower() in {".bib", ".bbl"}
            ],
        }
        nodes.append(node)
        by_folder[folder] = node

    return nodes, by_folder


def alias_maps(nodes: list[dict[str, Any]]) -> dict[str, dict[str, str]]:
    aliases = {
        "arxiv": {},
        "title": {},
        "id": {},
        "slug": {},
    }

    slug_counts = Counter(normalize(node["slug"]) for node in nodes)
    for node in nodes:
        if node["arxiv"]:
            aliases["arxiv"][node["arxiv"]] = node["id"]
        aliases["title"][normalize(node["title"])] = node["id"]
        aliases["id"][normalize(node["id"])] = node["id"]
        slug = normalize(node["slug"])
        if len(slug) >= 5 and slug_counts[slug] == 1:
            aliases["slug"][slug] = node["id"]

    return aliases


def match_reference(
    reference_text: str,
    title: str,
    aliases: dict[str, dict[str, str]],
) -> tuple[str | None, str, str]:
    for arxiv_id in find_arxiv_ids(reference_text):
        if arxiv_id in aliases["arxiv"]:
            return aliases["arxiv"][arxiv_id], "arxiv", arxiv_id

    normalized_title = normalize(title)
    if normalized_title and normalized_title in aliases["title"]:
        return aliases["title"][normalized_title], "title", title

    return None, "", ""


def add_edge(
    edges: dict[tuple[str, str, str], dict[str, Any]],
    source: str,
    target: str,
    kind: str,
    evidence: dict[str, str],
) -> None:
    if source == target:
        return
    key = (source, target, kind)
    edge = edges.setdefault(
        key,
        {
            "source": source,
            "target": target,
            "kind": kind,
            "evidence": [],
        },
    )
    if evidence not in edge["evidence"]:
        edge["evidence"].append(evidence)


def bibliography_edges(
    nodes_by_folder: dict[str, dict[str, Any]],
    aliases: dict[str, dict[str, str]],
) -> dict[tuple[str, str, str], dict[str, Any]]:
    edges: dict[tuple[str, str, str], dict[str, Any]] = {}

    for path in sorted(PAPERS_DIR.glob("*/source/**/*")):
        if path.suffix.lower() not in {".bib", ".bbl"}:
            continue
        root = paper_root_for(path)
        if root is None or root.name not in nodes_by_folder:
            continue
        source_id = nodes_by_folder[root.name]["id"]
        text = path.read_text(encoding="utf-8", errors="replace")

        if path.suffix.lower() == ".bib":
            for entry in split_bib_entries(text):
                title = bib_field(entry, "title")
                target_id, matched_by, matched_value = match_reference(entry, title, aliases)
                if target_id:
                    add_edge(
                        edges,
                        source_id,
                        target_id,
                        "bibliography",
                        {
                            "file": rel(path),
                            "reference": bib_key(entry),
                            "matchedBy": matched_by,
                            "matchedValue": matched_value,
                        },
                    )
        else:
            for key, title, chunk in iter_bbl_items(text):
                target_id, matched_by, matched_value = match_reference(chunk, title, aliases)
                if target_id:
                    add_edge(
                        edges,
                        source_id,
                        target_id,
                        "bibliography",
                        {
                            "file": rel(path),
                            "reference": key,
                            "matchedBy": matched_by,
                            "matchedValue": matched_value,
                        },
                    )

    return edges


def curated_edges(
    nodes: list[dict[str, Any]],
    nodes_by_folder: dict[str, dict[str, Any]],
    aliases: dict[str, dict[str, str]],
) -> dict[tuple[str, str, str], dict[str, Any]]:
    edges: dict[tuple[str, str, str], dict[str, Any]] = {}
    mention_files = ("summary.md", "notes.md", "claims.md")

    mention_aliases: dict[str, tuple[str, str]] = {}
    for value, node_id in aliases["id"].items():
        mention_aliases[value] = (node_id, "id")
    for value, node_id in aliases["slug"].items():
        mention_aliases[value] = (node_id, "slug")
    for node in nodes:
        if node["arxiv"]:
            mention_aliases[normalize(node["arxiv"])] = (node["id"], "arxiv")
        title_alias = normalize(node["title"])
        if len(title_alias) >= 28:
            mention_aliases[title_alias] = (node["id"], "title")

    for folder, source_node in nodes_by_folder.items():
        for file_name in mention_files:
            path = PAPERS_DIR / folder / file_name
            if not path.exists():
                continue
            normalized_text = normalize(path.read_text(encoding="utf-8", errors="replace"))
            padded_text = f" {normalized_text} "

            for alias, (target_id, matched_by) in mention_aliases.items():
                if target_id == source_node["id"]:
                    continue
                if f" {alias} " not in padded_text:
                    continue
                add_edge(
                    edges,
                    source_node["id"],
                    target_id,
                    "curated-mention",
                    {
                        "file": rel(path),
                        "matchedBy": matched_by,
                        "matchedValue": alias,
                    },
                )

    return edges


def aggregate_stats(nodes: list[dict[str, Any]], edges: list[dict[str, Any]]) -> dict[str, Any]:
    degree: dict[str, Counter[str]] = defaultdict(Counter)
    for edge in edges:
        degree[edge["source"]]["out"] += 1
        degree[edge["target"]]["in"] += 1

    years = [node["year"] for node in nodes if node.get("year")]
    topics = Counter(topic for node in nodes for topic in node.get("topics", []))
    subareas = Counter(node["classification"]["primarySubarea"] for node in nodes)
    roles = Counter(node["classification"]["role"] for node in nodes)
    artifact_types = Counter(node["classification"]["artifactType"] for node in nodes)

    return {
        "paperCount": len(nodes),
        "edgeCount": len(edges),
        "bibliographyEdgeCount": sum(1 for edge in edges if edge["kind"] == "bibliography"),
        "curatedMentionEdgeCount": sum(1 for edge in edges if edge["kind"] == "curated-mention"),
        "isolatedPaperCount": sum(1 for node in nodes if not degree[node["id"]]),
        "yearRange": [min(years), max(years)] if years else [],
        "statuses": dict(sorted(Counter(node["status"] for node in nodes).items())),
        "topTopics": topics.most_common(18),
        "subareas": dict(sorted(subareas.items())),
        "roles": dict(sorted(roles.items())),
        "artifactTypes": dict(sorted(artifact_types.items())),
    }


def main() -> None:
    taxonomy = load_taxonomy()
    labels = {
        "subareas": taxonomy_labels(taxonomy, "subareas"),
        "roles": taxonomy_labels(taxonomy, "roles"),
        "artifact_types": taxonomy_labels(taxonomy, "artifact_types"),
    }
    seed_index = parse_seed_index(SEEDS_PATH)
    nodes, nodes_by_folder = build_nodes(seed_index, labels)
    aliases = alias_maps(nodes)

    edge_map = bibliography_edges(nodes_by_folder, aliases)
    for key, edge in curated_edges(nodes, nodes_by_folder, aliases).items():
        if key not in edge_map:
            edge_map[key] = edge

    edges = sorted(
        edge_map.values(),
        key=lambda edge: (edge["kind"], edge["source"], edge["target"]),
    )

    payload = {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "source": "local metadata, local source bibliographies, and curated note mentions",
        "taxonomy": taxonomy,
        "nodes": nodes,
        "edges": edges,
        "stats": aggregate_stats(nodes, edges),
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    json_payload = json.dumps(payload, indent=2, sort_keys=True)
    OUTPUT.write_text(json_payload + "\n", encoding="utf-8")
    print(
        f"Wrote {rel(OUTPUT)} with {payload['stats']['paperCount']} papers "
        f"and {payload['stats']['edgeCount']} edges."
    )


if __name__ == "__main__":
    main()
