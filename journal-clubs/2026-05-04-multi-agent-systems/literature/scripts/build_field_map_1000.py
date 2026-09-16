#!/usr/bin/env python3
"""Build a 1000-paper field map for multi-agent literature.

The current repo has a curated 400-paper candidate list. This script keeps
those rows as trusted inputs, expands with arXiv and OpenAlex metadata, applies
lightweight relevance/tagging heuristics, and writes a reproducible field-map
snapshot.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import math
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CURATED_CANDIDATES = ROOT / "docs" / "candidates.md"
OUT_CSV = ROOT / "docs" / "field-map-1000.csv"
OUT_YAML = ROOT / "docs" / "field-map-1000.yaml"
OUT_MD = ROOT / "docs" / "field-map-1000.md"

SNAPSHOT_DATE = "2026-05-04"
USER_AGENT = "LiteratureFieldMap/1.0 (multi-agent literature mapping)"

SUBAREA_TARGETS = {
    "LLM Multi-Agent Frameworks and Coordination": 160,
    "Debate, Reasoning, and Aggregation": 90,
    "Agent Foundations and Infrastructure": 100,
    "Benchmarks and Evaluation": 110,
    "Software, Web, and Computer-Use Agents": 140,
    "Scientific and Domain Agents": 100,
    "Safety, Security, and Reliability": 100,
    "MARL, Emergent Communication, and Social Behavior": 140,
    "Surveys and Taxonomies": 40,
    "Classical MAS and Game-Theoretic Foundations": 20,
}

CSV_FIELDS = [
    "rank",
    "title",
    "authors",
    "year",
    "id",
    "status",
    "role",
    "sub_area",
    "provenance",
    "source",
    "citation_count",
    "confidence",
    "url",
    "notes",
]


ARXIV_QUERIES = [
    ('all:"multi-agent" AND all:"large language model"', "arxiv:llm-multi-agent"),
    ('all:"LLM" AND all:"multi-agent"', "arxiv:llm-multi-agent"),
    ('all:"LLM-based multi-agent"', "arxiv:llm-mas"),
    ('all:"multi-agent collaboration" AND all:"large language model"', "arxiv:collaboration"),
    ('all:"multi-agent debate" AND all:"language model"', "arxiv:debate"),
    ('all:"multi-agent reasoning" AND all:"LLM"', "arxiv:reasoning"),
    ('all:"agent society" AND all:"large language model"', "arxiv:society"),
    ('all:"generative agents" AND all:"large language model"', "arxiv:generative-agents"),
    ('all:"language agents" AND all:"multi-agent"', "arxiv:language-agents"),
    ('all:"agentic workflow" AND all:"language model"', "arxiv:workflow"),
    ('all:"software engineering agents" OR all:"coding agents"', "arxiv:software-agents"),
    ('all:"web agent" AND all:"large language model"', "arxiv:web-agents"),
    ('all:"computer-use agents" OR all:"GUI agents"', "arxiv:computer-use"),
    ('all:"mobile agent" AND all:"large language model"', "arxiv:mobile-agents"),
    ('all:"tool use" AND all:"language agents"', "arxiv:tool-use"),
    ('all:"function calling" AND all:"agents"', "arxiv:function-calling"),
    ('all:"agent safety" AND all:"large language model"', "arxiv:agent-safety"),
    ('all:"prompt injection" AND all:"agents"', "arxiv:prompt-injection"),
    ('all:"LLM agents" AND all:"security"', "arxiv:agent-security"),
    ('all:"AI scientist" AND all:"agent"', "arxiv:ai-scientist"),
    ('all:"scientific discovery" AND all:"language agents"', "arxiv:scientific-agents"),
    ('all:"medical agents" AND all:"large language model"', "arxiv:medical-agents"),
    ('all:"multi-agent reinforcement learning"', "arxiv:marl"),
    ('all:"emergent communication" AND all:"multi-agent"', "arxiv:emergent-communication"),
    ('all:"human-ai coordination" AND all:"agents"', "arxiv:human-ai-coordination"),
    ('all:"social dilemmas" AND all:"multi-agent"', "arxiv:social-dilemmas"),
    ('all:"multi-agent systems" AND all:"survey"', "arxiv:surveys"),
    ('all:"LLM agents" AND all:"survey"', "arxiv:llm-agent-surveys"),
]

OPENALEX_QUERIES = [
    ("LLM multi-agent systems", "openalex:llm-mas"),
    ("large language model multi agent collaboration", "openalex:collaboration"),
    ("large language model multi agent debate", "openalex:debate"),
    ("LLM multi agent reasoning", "openalex:reasoning"),
    ("LLM multi agent framework", "openalex:frameworks"),
    ("multi agent LLM orchestration", "openalex:orchestration"),
    ("multi agent LLM communication topology", "openalex:topology"),
    ("LLM agent society generative agents", "openalex:society"),
    ("multi agent software engineering agents", "openalex:software-agents"),
    ("coding agents multi agent", "openalex:coding-agents"),
    ("web agents large language models", "openalex:web-agents"),
    ("GUI agents large language models", "openalex:gui-agents"),
    ("computer use agents multimodal", "openalex:computer-use"),
    ("mobile agents large language models", "openalex:mobile-agents"),
    ("autonomous agents benchmark large language model", "openalex:agent-benchmarks"),
    ("agent safety large language model", "openalex:agent-safety"),
    ("prompt injection agents", "openalex:prompt-injection"),
    ("LLM agents cybersecurity", "openalex:cybersecurity"),
    ("scientific discovery agents large language models", "openalex:scientific-agents"),
    ("AI scientist agents", "openalex:ai-scientist"),
    ("medical multi agent large language models", "openalex:medical-agents"),
    ("financial trading multi agent LLM", "openalex:finance-agents"),
    ("multi agent reinforcement learning", "openalex:marl"),
    ("emergent communication multi agent", "openalex:emergent-communication"),
    ("human AI coordination agents", "openalex:human-ai-coordination"),
    ("multi agent social dilemmas", "openalex:social-dilemmas"),
    ("agent communication language KQML", "openalex:classical-acl"),
    ("decentralized POMDP multiagent", "openalex:dec-pomdp"),
    ("multi agent systems survey", "openalex:surveys"),
    ("LLM based multi agent systems survey", "openalex:llm-mas-surveys"),
    ("agentic workflow generation", "openalex:workflow-generation"),
    ("automated design of agentic systems", "openalex:agentic-design"),
    ("tool use language agents benchmark", "openalex:tool-use"),
    ("function calling agent benchmark", "openalex:function-calling"),
    ("software engineering benchmark LLM agents", "openalex:swe-benchmarks"),
    ("workplace agents benchmark", "openalex:workplace-agents"),
    ("computer control benchmark agents", "openalex:computer-control"),
    ("web navigation agents", "openalex:web-navigation"),
    ("multi robot collaboration large language models", "openalex:robot-collaboration"),
    ("minecraft multi agent large language model", "openalex:minecraft-agents"),
    ("multi agent planning large language models", "openalex:planning"),
]


def clean_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value)
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("\n", " ").replace("\r", " ").replace("|", "/")
    return re.sub(r"\s+", " ", text).strip()


def norm_title(title: str) -> str:
    text = clean_text(title).lower()
    text = re.sub(r"\([^)]*\)", " ", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    stop = {"a", "an", "the", "towards", "toward"}
    return " ".join(tok for tok in text.split() if tok not in stop)


def parse_year(value: Any) -> int | None:
    match = re.search(r"(19|20)\d{2}", str(value or ""))
    if not match:
        return None
    return int(match.group(0))


def extract_arxiv_id(text: str) -> str:
    if not text:
        return ""
    patterns = [
        r"arxiv[.:/ ]+([0-9]{4}\.[0-9]{4,5})",
        r"arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5})",
        r"\b([0-9]{4}\.[0-9]{4,5})(?:v\d+)?\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.I)
        if match:
            return match.group(1)
    return ""


def clean_identifier(value: str, url: str = "") -> str:
    value = clean_text(value)
    arxiv_id = extract_arxiv_id(value) or extract_arxiv_id(url)
    if arxiv_id:
        return arxiv_id
    return value


def canonical_keys(entry: dict[str, Any]) -> list[str]:
    keys: list[str] = []
    identifier = str(entry.get("id", "")).strip().lower()
    title_key = norm_title(entry.get("title", ""))
    if identifier:
        keys.append("id:" + identifier)
        arxiv_id = extract_arxiv_id(identifier)
        if arxiv_id:
            keys.append("arxiv:" + arxiv_id)
        doi_match = re.search(r"10\.\d{4,9}/[-._;()/:a-z0-9]+", identifier, re.I)
        if doi_match:
            keys.append("doi:" + doi_match.group(0).lower())
    url = str(entry.get("url", "")).lower()
    arxiv_id = extract_arxiv_id(url)
    if arxiv_id:
        keys.append("arxiv:" + arxiv_id)
    if title_key:
        keys.append("title:" + title_key)
    return keys


def entry_key(entry: dict[str, Any]) -> str:
    for key in canonical_keys(entry):
        if key.startswith(("arxiv:", "doi:", "title:")):
            return key
    return canonical_keys(entry)[0]


def add_entry(entries: dict[str, dict[str, Any]], entry: dict[str, Any]) -> None:
    title = clean_text(entry.get("title", ""))
    if len(title) < 8:
        return
    entry["title"] = title
    entry["authors"] = clean_text(entry.get("authors", "")) or "Unknown"
    entry["id"] = clean_identifier(entry.get("id", ""), entry.get("url", ""))
    entry["url"] = clean_text(entry.get("url", ""))
    entry["notes"] = clean_text(entry.get("notes", ""))
    entry["provenance"] = clean_text(entry.get("provenance", "auto-map"))
    entry["source"] = clean_text(entry.get("source", ""))
    entry["status"] = clean_text(entry.get("status", "candidate")) or "candidate"
    entry["role"] = clean_text(entry.get("role", "")) or classify_role(entry)
    entry["sub_area"] = clean_text(entry.get("sub_area", "")) or classify_subarea(entry)
    entry["year"] = parse_year(entry.get("year")) or ""
    entry["citation_count"] = int(entry.get("citation_count") or 0)
    entry["relevance_score"] = int(entry.get("relevance_score") or relevance_score(entry))
    entry["confidence"] = float(entry.get("confidence") or confidence(entry))

    keys = canonical_keys(entry)
    existing_key = next((key for key in keys if key in entries), None)
    if existing_key is None:
        for key in keys:
            entries[key] = entry
        return

    existing = entries[existing_key]
    if existing.get("status") == "seed" or existing.get("curated_rank"):
        winner, loser = existing, entry
    elif entry.get("curated_rank"):
        winner, loser = entry, existing
        entries[existing_key] = winner
    else:
        winner, loser = (
            (existing, entry)
            if rank_sort_key(existing) >= rank_sort_key(entry)
            else (entry, existing)
        )
        entries[existing_key] = winner

    for field in ("source", "provenance"):
        values = {part for part in str(winner.get(field, "")).split(";") if part}
        values.update(part for part in str(loser.get(field, "")).split(";") if part)
        winner[field] = ";".join(sorted(values))
    if not winner.get("url") and loser.get("url"):
        winner["url"] = loser["url"]
    if not winner.get("id") and loser.get("id"):
        winner["id"] = loser["id"]
    winner["citation_count"] = max(int(winner.get("citation_count") or 0), int(loser.get("citation_count") or 0))
    winner["relevance_score"] = max(int(winner.get("relevance_score") or 0), int(loser.get("relevance_score") or 0))
    winner["confidence"] = max(float(winner.get("confidence") or 0.0), float(loser.get("confidence") or 0.0))
    for key in keys:
        entries[key] = winner


def parse_curated_candidates() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    current_section = ""
    for raw_line in CURATED_CANDIDATES.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("## "):
            current_section = re.sub(r"^##\s+\d+\.\s+", "", line).strip()
            continue
        if not re.match(r"^\|\s*\d+\s*\|", line):
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) < 10:
            continue
        rows.append(
            {
                "curated_rank": int(parts[0]),
                "title": parts[1],
                "authors": parts[2],
                "year": parts[3],
                "id": parts[4],
                "status": parts[5],
                "role": parts[6],
                "provenance": parts[7],
                "source": "curated-400",
                "local_refs": parts[8],
                "notes": parts[9],
                "sub_area": current_section,
                "citation_count": 0,
                "confidence": 1.0,
                "relevance_score": 100,
            }
        )
    return rows


def fetch_url(url: str, timeout: int = 40) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.read()


def fetch_arxiv(query: str, max_results: int) -> list[dict[str, Any]]:
    params = urllib.parse.urlencode(
        {
            "search_query": query,
            "start": 0,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    url = "https://export.arxiv.org/api/query?" + params
    data = fetch_url(url, timeout=60)
    root = ET.fromstring(data)
    ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    rows = []
    for item in root.findall("atom:entry", ns):
        title = clean_text(item.findtext("atom:title", default="", namespaces=ns))
        abstract = clean_text(item.findtext("atom:summary", default="", namespaces=ns))
        url_text = clean_text(item.findtext("atom:id", default="", namespaces=ns))
        published = clean_text(item.findtext("atom:published", default="", namespaces=ns))
        authors = [clean_text(author.findtext("atom:name", default="", namespaces=ns)) for author in item.findall("atom:author", ns)]
        author_label = authors[0] + (" et al" if len(authors) > 1 else "") if authors else "Unknown"
        arxiv_id = extract_arxiv_id(url_text)
        rows.append(
            {
                "title": title,
                "authors": author_label,
                "year": parse_year(published) or "",
                "id": arxiv_id,
                "status": "candidate",
                "provenance": "auto-map",
                "source": "arxiv",
                "url": "https://arxiv.org/abs/" + arxiv_id if arxiv_id else url_text,
                "abstract": abstract,
                "notes": "arXiv query expansion",
            }
        )
    return rows


def fetch_openalex(query: str, per_page: int) -> list[dict[str, Any]]:
    params = urllib.parse.urlencode(
        {
            "search": query,
            "filter": "from_publication_date:2015-01-01,is_retracted:false",
            "per-page": per_page,
            "select": "id,display_name,publication_year,authorships,doi,cited_by_count,primary_location,abstract_inverted_index",
        }
    )
    url = "https://api.openalex.org/works?" + params
    payload = json.loads(fetch_url(url, timeout=60).decode("utf-8"))
    rows = []
    for item in payload.get("results", []):
        title = clean_text(item.get("display_name"))
        authorships = item.get("authorships") or []
        author_names = []
        for author in authorships[:3]:
            raw_name = author.get("raw_author_name") or (author.get("author") or {}).get("display_name")
            if raw_name:
                author_names.append(clean_text(raw_name))
        author_label = ", ".join(author_names)
        if len(authorships) > 3:
            author_label += " et al"
        landing_url = ""
        location = item.get("primary_location") or {}
        if isinstance(location, dict):
            landing_url = location.get("landing_page_url") or location.get("pdf_url") or ""
        doi = item.get("doi") or ""
        identifier = clean_identifier(doi, landing_url) or clean_text(item.get("id", ""))
        rows.append(
            {
                "title": title,
                "authors": author_label or "Unknown",
                "year": item.get("publication_year") or "",
                "id": identifier,
                "status": "candidate",
                "provenance": "auto-map",
                "source": "openalex",
                "url": landing_url or clean_text(item.get("id", "")),
                "citation_count": int(item.get("cited_by_count") or 0),
                "abstract": abstract_from_openalex(item.get("abstract_inverted_index")),
                "notes": "OpenAlex query expansion",
            }
        )
    return rows


def abstract_from_openalex(index: Any) -> str:
    if not isinstance(index, dict):
        return ""
    positions: dict[int, str] = {}
    for word, offsets in index.items():
        for offset in offsets:
            if isinstance(offset, int):
                positions[offset] = word
    return clean_text(" ".join(positions[i] for i in sorted(positions)))


def parse_local_bib() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted((ROOT / "papers").glob("*/source/*.bib")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for chunk in re.split(r"\n\s*@", text):
            if "title" not in chunk.lower():
                continue
            title = bib_field(chunk, "title")
            if not title:
                continue
            author = bib_field(chunk, "author")
            year = bib_field(chunk, "year")
            eprint = bib_field(chunk, "eprint") or bib_field(chunk, "arxiv")
            doi = bib_field(chunk, "doi")
            identifier = eprint or ("DOI:" + doi if doi else "")
            author_label = compact_bib_authors(author)
            rows.append(
                {
                    "title": title,
                    "authors": author_label,
                    "year": year,
                    "id": identifier,
                    "status": "candidate",
                    "provenance": "local-bib-auto",
                    "source": "local-bib",
                    "notes": f"Referenced in {path.parent.parent.name}",
                }
            )
    return rows


def bib_field(chunk: str, field: str) -> str:
    pattern = rf"\b{re.escape(field)}\s*=\s*([{{\"])(.*?)(?<!\\)\1\s*,"
    match = re.search(pattern, chunk, flags=re.I | re.S)
    if not match:
        return ""
    value = match.group(2)
    value = value.replace("{", "").replace("}", "")
    return clean_text(value)


def compact_bib_authors(author: str) -> str:
    if not author:
        return "Unknown"
    parts = [clean_text(part) for part in re.split(r"\s+and\s+", author) if clean_text(part)]
    if not parts:
        return "Unknown"
    first = parts[0]
    if "," in first:
        last, rest = [part.strip() for part in first.split(",", 1)]
        first = f"{rest} {last}".strip()
    return first + (" et al" if len(parts) > 1 else "")


def has_any(text: str, patterns: list[str]) -> bool:
    return any(pattern in text for pattern in patterns)


def relevance_score(entry: dict[str, Any]) -> int:
    title = clean_text(entry.get("title", "")).lower()
    abstract = clean_text(entry.get("abstract", "")).lower()
    text = f"{title} {abstract}"
    score = 0

    if re.search(r"\bmulti[- ]?agent\b|\bmultiagent\b", text):
        score += 34
    if re.search(r"\bllm\b|\bllms\b|large language model|language models", text):
        score += 12
    if has_any(text, ["llm agent", "language agent", "autonomous agent", "agentic"]):
        score += 14
    if has_any(text, ["collaboration", "coordination", "orchestration", "delegation", "communication topology"]):
        score += 8
    if has_any(text, ["debate", "peer review", "consensus", "voting", "aggregation", "mixture-of-agents", "mixture of agents"]):
        score += 10
    if has_any(text, ["benchmark", "evaluation", "evaluating", "arena", "bench"]):
        score += 8
    if has_any(text, ["software engineering", "coding agent", "code agent", "swe-bench", "github issue", "repository"]):
        score += 13
    if has_any(text, ["web agent", "browser", "gui agent", "computer use", "computer-use", "mobile agent", "android", "desktop"]):
        score += 12
    if has_any(text, ["tool use", "tool-use", "function calling", "api", "workflow", "agentic system"]):
        score += 8
    if has_any(text, ["scientific discovery", "ai scientist", "research agent", "co-scientist", "laboratory", "medical", "clinical"]):
        score += 11
    if has_any(text, ["safety", "security", "prompt injection", "cyber", "harm", "red-team", "backdoor", "poison"]):
        score += 11
    if has_any(text, ["multi-agent reinforcement learning", "marl", "markov game", "decentralized pomdp", "self-play"]):
        score += 15
    if has_any(text, ["emergent communication", "emergent language", "social dilemma", "human-ai coordination", "ad hoc teamwork"]):
        score += 14
    if has_any(text, ["survey", "review", "taxonomy", "roadmap"]):
        score += 6
    if has_any(text, ["agent communication language", "contract net", "bdi", "joint intention", "shared plan"]):
        score += 10

    if has_any(text, ["multi-agent path finding", "coverage control", "formation control", "swarm robotics"]):
        score -= 16
    if has_any(text, ["wireless", "uav", "vehicular", "power system", "smart grid", "traffic signal"]):
        score -= 8
    if "agent-based model" in text and not has_any(text, ["large language model", "llm", "generative agent"]):
        score -= 12
    if parse_year(entry.get("year")) and parse_year(entry.get("year")) > 2026:
        score -= 100

    return max(score, 0)


def classify_subarea(entry: dict[str, Any]) -> str:
    title = clean_text(entry.get("title", "")).lower()
    abstract = clean_text(entry.get("abstract", "")).lower()
    text = f"{title} {abstract}"
    if has_any(text, ["survey", "review", "taxonomy", "roadmap"]):
        return "Surveys and Taxonomies"
    if has_any(text, ["prompt injection", "safety", "security", "cyber", "harm", "backdoor", "poison", "red-team", "risk"]):
        return "Safety, Security, and Reliability"
    if has_any(text, ["software engineering", "coding agent", "code agent", "github issue", "repository", "swe-bench", "web agent", "browser", "web navigation", "gui agent", "computer use", "computer-use", "desktop", "android", "mobile agent", "smartphone", "function calling"]):
        return "Software, Web, and Computer-Use Agents"
    if has_any(text, ["benchmark", "evaluation", "evaluating", "arena", "bench", "leaderboard"]):
        return "Benchmarks and Evaluation"
    if has_any(text, ["scientific discovery", "ai scientist", "co-scientist", "research agent", "laboratory", "clinical", "medical", "chemistry", "biology", "finance", "financial", "geospatial", "radiology"]):
        return "Scientific and Domain Agents"
    if has_any(text, ["debate", "consensus", "voting", "aggregation", "reasoning", "reflection", "peer review", "mixture-of-agents", "mixture of agents"]):
        return "Debate, Reasoning, and Aggregation"
    if has_any(text, ["multi-agent reinforcement learning", "marl", "emergent communication", "emergent language", "social dilemma", "self-play", "markov game", "hanabi", "starcraft", "overcooked", "human-ai coordination"]):
        return "MARL, Emergent Communication, and Social Behavior"
    if has_any(text, ["contract net", "bdi", "kqml", "agent communication language", "joint intention", "shared plan", "decentralized pomdp", "game-theoretic"]):
        return "Classical MAS and Game-Theoretic Foundations"
    if has_any(text, ["tool use", "tool-use", "memory", "workflow", "agentic system", "autonomous agent", "language agent"]):
        return "Agent Foundations and Infrastructure"
    return "LLM Multi-Agent Frameworks and Coordination"


def classify_role(entry: dict[str, Any]) -> str:
    text = f"{entry.get('title', '')} {entry.get('abstract', '')}".lower()
    year = parse_year(entry.get("year")) or 0
    if has_any(text, ["survey", "review", "taxonomy", "roadmap"]):
        return "survey"
    if year and year < 2023 and has_any(
        text,
        [
            "multi-agent reinforcement learning",
            "marl",
            "emergent communication",
            "markov game",
            "self-play",
            "decentralized pomdp",
            "contract net",
            "bdi",
            "kqml",
        ],
    ):
        return "anchor"
    if re.search(r"\bmulti[- ]?agent\b|\bmultiagent\b", text) and has_any(text, ["llm", "large language model", "language model"]):
        return "trend" if year >= 2025 else "core"
    if classify_subarea(entry) in {
        "Agent Foundations and Infrastructure",
        "Benchmarks and Evaluation",
        "Software, Web, and Computer-Use Agents",
        "Safety, Security, and Reliability",
    }:
        return "bridge"
    if year >= 2025:
        return "trend"
    return "anchor" if classify_subarea(entry).startswith(("MARL", "Classical")) else "bridge"


def confidence(entry: dict[str, Any]) -> float:
    if entry.get("curated_rank"):
        return 1.0
    score = relevance_score(entry)
    source_count = len([part for part in str(entry.get("source", "")).split(";") if part])
    citation_bonus = min(math.log10(int(entry.get("citation_count") or 0) + 1) / 5, 0.18)
    base = 0.42 + min(score, 80) / 160 + min(source_count, 3) * 0.04 + citation_bonus
    if not entry.get("id"):
        base -= 0.06
    return round(max(0.35, min(base, 0.92)), 2)


def rank_sort_key(entry: dict[str, Any]) -> tuple[float, int, int, int]:
    source_count = len([part for part in str(entry.get("source", "")).split(";") if part])
    return (
        float(entry.get("confidence") or 0.0),
        int(entry.get("relevance_score") or 0),
        source_count,
        int(entry.get("citation_count") or 0),
    )


def generated_sort_key(entry: dict[str, Any]) -> tuple[int, float, int, int, int]:
    year = parse_year(entry.get("year")) or 0
    source_count = len([part for part in str(entry.get("source", "")).split(";") if part])
    return (
        int(entry.get("relevance_score") or 0),
        float(entry.get("confidence") or 0),
        source_count,
        int(entry.get("citation_count") or 0),
        year,
    )


def collect_external(args: argparse.Namespace) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if args.offline:
        return rows

    for idx, (query, label) in enumerate(ARXIV_QUERIES, start=1):
        print(f"arXiv {idx:02d}/{len(ARXIV_QUERIES)} {label}", flush=True)
        try:
            for row in fetch_arxiv(query, args.arxiv_results):
                row["source"] = label
                row["provenance"] = "auto-map:arxiv-query"
                rows.append(row)
        except Exception as exc:  # noqa: BLE001
            print(f"  skipped {label}: {exc}", flush=True)
        if idx != len(ARXIV_QUERIES):
            time.sleep(args.arxiv_delay)

    for idx, (query, label) in enumerate(OPENALEX_QUERIES, start=1):
        print(f"OpenAlex {idx:02d}/{len(OPENALEX_QUERIES)} {label}", flush=True)
        try:
            for row in fetch_openalex(query, args.openalex_results):
                row["source"] = label
                row["provenance"] = "auto-map:openalex-query"
                rows.append(row)
        except Exception as exc:  # noqa: BLE001
            print(f"  skipped {label}: {exc}", flush=True)
        time.sleep(args.openalex_delay)

    return rows


def select_entries(entries: dict[str, dict[str, Any]], target: int) -> list[dict[str, Any]]:
    unique: dict[str, dict[str, Any]] = {}
    seen_titles: set[str] = set()
    for entry in entries.values():
        title_key = norm_title(entry.get("title", ""))
        if title_key in seen_titles:
            continue
        seen_titles.add(title_key)
        unique[entry_key(entry)] = entry
    curated = sorted(
        [entry for entry in unique.values() if entry.get("curated_rank")],
        key=lambda entry: int(entry["curated_rank"]),
    )
    generated = [
        entry
        for entry in unique.values()
        if not entry.get("curated_rank")
        and int(entry.get("relevance_score") or 0) >= 28
        and (parse_year(entry.get("year")) or 0) <= 2026
    ]
    generated.sort(key=generated_sort_key, reverse=True)

    selected = list(curated)
    selected_keys = {entry_key(entry) for entry in selected}
    current_counts = Counter(entry["sub_area"] for entry in selected)
    by_subarea: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in generated:
        by_subarea[entry["sub_area"]].append(entry)

    for subarea, desired_total in SUBAREA_TARGETS.items():
        needed = max(desired_total - current_counts[subarea], 0)
        for entry in by_subarea.get(subarea, [])[:needed]:
            key = entry_key(entry)
            if key in selected_keys:
                continue
            selected.append(entry)
            selected_keys.add(key)
            current_counts[subarea] += 1
            if len(selected) >= target:
                break
        if len(selected) >= target:
            break

    if len(selected) < target:
        for entry in generated:
            key = entry_key(entry)
            if key in selected_keys:
                continue
            selected.append(entry)
            selected_keys.add(key)
            if len(selected) >= target:
                break

    if len(selected) < target:
        relaxed = [
            entry
            for entry in unique.values()
            if not entry.get("curated_rank")
            and entry_key(entry) not in selected_keys
            and int(entry.get("relevance_score") or 0) >= 22
            and (parse_year(entry.get("year")) or 0) <= 2026
        ]
        relaxed.sort(key=generated_sort_key, reverse=True)
        for entry in relaxed:
            selected.append(entry)
            selected_keys.add(entry_key(entry))
            if len(selected) >= target:
                break

    selected = selected[:target]
    for rank, entry in enumerate(selected, start=1):
        entry["rank"] = rank
        entry["confidence"] = confidence(entry)
        entry["role"] = entry.get("role") or classify_role(entry)
        entry["sub_area"] = entry.get("sub_area") or classify_subarea(entry)
    return selected


def write_csv(entries: list[dict[str, Any]]) -> None:
    with OUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS, lineterminator="\n")
        writer.writeheader()
        for entry in entries:
            writer.writerow({field: entry.get(field, "") for field in CSV_FIELDS})


def yaml_key(value: str) -> str:
    if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", value):
        return value
    return json.dumps(value, ensure_ascii=False)


def yaml_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int | float):
        return str(value)
    return json.dumps(str(value), ensure_ascii=False)


def write_yaml_value(handle: Any, value: Any, indent: int = 0) -> None:
    prefix = " " * indent
    if isinstance(value, dict):
        if not value:
            handle.write("{}\n")
            return
        for key, item in value.items():
            if isinstance(item, dict | list):
                handle.write(f"{prefix}{yaml_key(str(key))}:\n")
                write_yaml_value(handle, item, indent + 2)
            else:
                handle.write(f"{prefix}{yaml_key(str(key))}: {yaml_scalar(item)}\n")
        return
    if isinstance(value, list):
        if not value:
            handle.write(f"{prefix}[]\n")
            return
        for item in value:
            if isinstance(item, dict):
                handle.write(f"{prefix}- ")
                if not item:
                    handle.write("{}\n")
                    continue
                first = True
                for key, nested in item.items():
                    if isinstance(nested, dict | list):
                        if first:
                            handle.write(f"{yaml_key(str(key))}:\n")
                            first = False
                        else:
                            handle.write(f"{prefix}  {yaml_key(str(key))}:\n")
                        write_yaml_value(handle, nested, indent + 4)
                    else:
                        if first:
                            handle.write(f"{yaml_key(str(key))}: {yaml_scalar(nested)}\n")
                            first = False
                        else:
                            handle.write(f"{prefix}  {yaml_key(str(key))}: {yaml_scalar(nested)}\n")
            elif isinstance(item, list | dict):
                handle.write(f"{prefix}-\n")
                write_yaml_value(handle, item, indent + 2)
            else:
                handle.write(f"{prefix}- {yaml_scalar(item)}\n")
        return
    handle.write(f"{prefix}{yaml_scalar(value)}\n")


def write_yaml(entries: list[dict[str, Any]], args: argparse.Namespace) -> None:
    data = {
        "metadata": {
            "snapshot_date": SNAPSHOT_DATE,
            "target": args.target,
            "generated_at": dt.datetime.now(dt.UTC).isoformat(),
            "sources": [
                "docs/candidates.md curated 400-paper candidate universe",
                "arXiv API query expansion",
                "OpenAlex Works API search expansion",
                "Local BibTeX references under papers/*/source/*.bib",
            ],
        },
        "stats": stats(entries),
        "entries": [{field: entry.get(field, "") for field in CSV_FIELDS} for entry in entries],
    }
    with OUT_YAML.open("w", encoding="utf-8") as handle:
        handle.write("# 1000-paper multi-agent field map. Generated by scripts/build_field_map_1000.py.\n")
        write_yaml_value(handle, data)


def stats(entries: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "total": len(entries),
        "by_status": dict(Counter(entry.get("status", "") for entry in entries)),
        "by_role": dict(Counter(entry.get("role", "") for entry in entries)),
        "by_sub_area": dict(Counter(entry.get("sub_area", "") for entry in entries)),
        "by_source_family": dict(source_family_counts(entries)),
        "by_year_band": dict(year_band_counts(entries)),
    }


def source_family_counts(entries: list[dict[str, Any]]) -> Counter:
    counts: Counter = Counter()
    for entry in entries:
        source = str(entry.get("source", ""))
        if "curated-400" in source:
            counts["curated-400"] += 1
        elif "arxiv" in source and "openalex" in source:
            counts["arxiv+openalex"] += 1
        elif "arxiv" in source:
            counts["arxiv"] += 1
        elif "openalex" in source:
            counts["openalex"] += 1
        elif "local-bib" in source:
            counts["local-bib"] += 1
        else:
            counts["other"] += 1
    return counts


def year_band_counts(entries: list[dict[str, Any]]) -> Counter:
    counts: Counter = Counter()
    for entry in entries:
        year = parse_year(entry.get("year"))
        if year is None:
            counts["unknown"] += 1
        elif year < 2020:
            counts["pre-2020"] += 1
        elif year <= 2022:
            counts["2020-2022"] += 1
        elif year == 2023:
            counts["2023"] += 1
        elif year == 2024:
            counts["2024"] += 1
        elif year == 2025:
            counts["2025"] += 1
        elif year == 2026:
            counts["2026"] += 1
    return counts


def md_table(counter: dict[str, int], key_label: str) -> str:
    lines = [f"| {key_label} | Count |", "|---|---:|"]
    for key, value in sorted(counter.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"| {key or 'unknown'} | {value} |")
    return "\n".join(lines)


def write_markdown(entries: list[dict[str, Any]], args: argparse.Namespace) -> None:
    summary = stats(entries)
    by_subarea = summary["by_sub_area"]
    by_year = summary["by_year_band"]
    recent = [entry for entry in entries if (parse_year(entry.get("year")) or 0) >= 2025]
    recent_subareas = Counter(entry.get("sub_area", "") for entry in recent)
    auto_count = len([entry for entry in entries if "curated-400" not in str(entry.get("source", ""))])

    lines = [
        "# 1000-Paper Multi-Agent Field Map",
        "",
        f"Snapshot date: {SNAPSHOT_DATE}",
        "",
        "This is a field map, not a top-1000 ranking. The first 400 rows are the curated candidate universe from `docs/candidates.md`; rows 401-1000 are automatically expanded candidates from arXiv, OpenAlex, and local BibTeX snowballing. Generated rows are intended for mapping and triage before any top-100 promotion.",
        "",
        "## Files",
        "",
        "- `docs/field-map-1000.csv`: full 1000-row table for spreadsheet analysis.",
        "- `docs/field-map-1000.yaml`: same entries plus generation metadata and stats.",
        "- `scripts/build_field_map_1000.py`: regeneration script.",
        "",
        "## Snapshot Stats",
        "",
        f"- Total entries: {len(entries)}",
        "- Curated base entries: 400",
        f"- Auto-expanded entries: {auto_count}",
        f"- Recent entries from 2025-2026: {len(recent)}",
        "",
        "### By Sub-Area",
        "",
        md_table(by_subarea, "Sub-area"),
        "",
        "### By Role",
        "",
        md_table(summary["by_role"], "Role"),
        "",
        "### By Year Band",
        "",
        md_table(by_year, "Year band"),
        "",
        "### By Source Family",
        "",
        md_table(summary["by_source_family"], "Source family"),
        "",
        "## Trend Readout",
        "",
        "The 1000-paper map makes the current direction of the field easier to inspect:",
        "",
        f"- Recent growth is concentrated in `{recent_subareas.most_common(1)[0][0]}` and `{recent_subareas.most_common(2)[1][0]}` among the 2025-2026 entries.",
        "- Multi-agent work is moving from static role-play/framework papers toward orchestration, topology search, scaling laws, verification, and failure attribution.",
        "- Software, web, GUI, and computer-use agents form a major bridge lane: many papers are not multi-agent papers by title, but they define the environments where multi-agent systems are now being tested.",
        "- Safety and reliability are no longer peripheral: prompt injection, tool misuse, cyber tasks, delegation failures, and benchmark validity now form a distinct research front.",
        "- Scientific and domain-agent papers are expanding quickly, but the map keeps them separate from core MAS papers so application volume does not swamp architecture and evaluation work.",
        "- MARL and emergent-communication anchors remain important as conceptual foundations, but they are capped to avoid lifetime-citation dominance over recent LLM-agent work.",
        "",
        "## Regeneration",
        "",
        "```bash",
        "python3 scripts/build_field_map_1000.py",
        "```",
        "",
        "Use `--offline` only for parser/debug checks from the curated candidate list and local BibTeX references; it is not expected to reach 1000 rows without online sources. The online path uses public APIs and may change as arXiv/OpenAlex metadata updates.",
        "",
        "## Provenance Notes",
        "",
        "- `curated-400`: manually curated candidate list already in this repo.",
        "- `auto-map:arxiv-query`: arXiv API query expansion.",
        "- `auto-map:openalex-query`: OpenAlex Works API search expansion.",
        "- `local-bib-auto`: paper discovered in checked-in BibTeX references.",
        "",
        "## Source APIs",
        "",
        "- arXiv API User's Manual: https://info.arxiv.org/help/api/user-manual.html",
        "- OpenAlex API overview: https://developers.openalex.org/api-reference/introduction",
        "- OpenAlex Works API: https://developers.openalex.org/api-reference/works",
        "",
        "## Quality Caveats",
        "",
        "- Rows 401-1000 are field-map candidates, not reviewed claims of importance.",
        "- Query APIs can return false positives, especially for robotics, wireless, traffic, and generic agent-based modeling papers; relevance/confidence scores are triage aids.",
        "- Citation counts come from OpenAlex when available and are intentionally not used as the sole ranking signal.",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=int, default=1000)
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--arxiv-results", type=int, default=80)
    parser.add_argument("--openalex-results", type=int, default=100)
    parser.add_argument("--arxiv-delay", type=float, default=3.0)
    parser.add_argument("--openalex-delay", type=float, default=0.15)
    args = parser.parse_args()

    entries: dict[str, dict[str, Any]] = {}
    for row in parse_curated_candidates():
        add_entry(entries, row)

    for row in parse_local_bib():
        row["relevance_score"] = relevance_score(row)
        if int(row["relevance_score"]) >= 28:
            add_entry(entries, row)

    for row in collect_external(args):
        row["relevance_score"] = relevance_score(row)
        if int(row["relevance_score"]) >= 22:
            row["role"] = classify_role(row)
            row["sub_area"] = classify_subarea(row)
            add_entry(entries, row)

    selected = select_entries(entries, args.target)
    if len(selected) < args.target:
        raise SystemExit(f"Only selected {len(selected)} entries; need {args.target}. Try increasing query limits.")

    write_csv(selected)
    write_yaml(selected, args)
    write_markdown(selected, args)
    print(f"Wrote {OUT_CSV.relative_to(ROOT)}")
    print(f"Wrote {OUT_YAML.relative_to(ROOT)}")
    print(f"Wrote {OUT_MD.relative_to(ROOT)}")
    print(json.dumps(stats(selected), indent=2))


if __name__ == "__main__":
    main()
