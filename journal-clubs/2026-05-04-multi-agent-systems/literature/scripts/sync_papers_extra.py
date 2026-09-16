#!/usr/bin/env python3
"""Populate papers_extra/ for field-map triage without reviewed paper folders.

This script is intentionally separate from scripts/add_arxiv_paper.sh. The
`papers/` tree is the curated reviewed corpus; `papers_extra/` is a broad local
paper-artifact corpus for agent triage over `docs/field-map-1000.csv`.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import re
import shutil
import tarfile
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "docs" / "field-map-1000.csv"
DEFAULT_OUT = ROOT / "papers_extra" / "multi-agent-triaged"
USER_AGENT = "LiteraturePapersExtra/1.0 (multi-agent literature triage)"

ARXIV_RE = re.compile(
    r"(?:arxiv[.:/ ]+)?\b([0-9]{2}(?:0[1-9]|1[0-2])\.[0-9]{4,5})(?:v[0-9]+)?\b",
    flags=re.I,
)
OPENREVIEW_RE = re.compile(r"openreview:([A-Za-z0-9_-]+)", flags=re.I)

MANIFEST_FIELDS = [
    "rank",
    "title",
    "authors",
    "year",
    "id",
    "status",
    "role",
    "sub_area",
    "source",
    "citation_count",
    "confidence",
    "url",
    "arxiv_id",
    "artifact_path",
    "pdf_url",
    "pdf_path",
    "pdf_status",
    "pdf_bytes",
    "pdf_error",
    "source_url",
    "source_path",
    "source_status",
    "source_error",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download PDFs and arXiv source into papers_extra/ for triage."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--execute", action="store_true", help="Download missing artifacts.")
    parser.add_argument("--force", action="store_true", help="Redownload present artifacts.")
    parser.add_argument("--pdf", dest="fetch_pdf", action="store_true", help="Download PDFs.")
    parser.add_argument("--no-pdf", dest="fetch_pdf", action="store_false", help="Skip PDFs.")
    parser.add_argument(
        "--source",
        dest="fetch_source",
        action="store_true",
        help="Download arXiv source when an arXiv ID is available.",
    )
    parser.add_argument(
        "--no-source",
        dest="fetch_source",
        action="store_false",
        help="Skip arXiv source downloads.",
    )
    parser.set_defaults(fetch_pdf=True, fetch_source=True)
    parser.add_argument("--limit", type=int, default=0, help="Process at most N eligible rows.")
    parser.add_argument("--rank-min", type=int, default=0)
    parser.add_argument("--rank-max", type=int, default=0)
    parser.add_argument(
        "--status",
        action="append",
        default=[],
        help="Only include this status. May be repeated.",
    )
    parser.add_argument(
        "--role",
        action="append",
        default=[],
        help="Only include this role. May be repeated.",
    )
    parser.add_argument(
        "--sub-area",
        action="append",
        default=[],
        help="Only include this sub-area. May be repeated.",
    )
    parser.add_argument(
        "--source-contains",
        action="append",
        default=[],
        help="Only include rows whose source field contains this string.",
    )
    parser.add_argument("--sleep", type=float, default=1.0, help="Seconds between downloads.")
    parser.add_argument("--timeout", type=float, default=60.0, help="Download timeout seconds.")
    parser.add_argument(
        "--no-existing",
        action="store_true",
        help="Do not point manifest rows at existing papers/* artifacts.",
    )
    return parser.parse_args()


def clean(value: Any) -> str:
    return str(value or "").strip()


def row_rank(row: dict[str, str]) -> int:
    try:
        return int(clean(row.get("rank")))
    except ValueError:
        return 0


def matches_filters(row: dict[str, str], args: argparse.Namespace) -> bool:
    rank = row_rank(row)
    if args.rank_min and rank < args.rank_min:
        return False
    if args.rank_max and rank > args.rank_max:
        return False
    if args.status and clean(row.get("status")) not in args.status:
        return False
    if args.role and clean(row.get("role")) not in args.role:
        return False
    if args.sub_area and clean(row.get("sub_area")) not in args.sub_area:
        return False
    source = clean(row.get("source")).lower()
    for needle in args.source_contains:
        if needle.lower() not in source:
            return False
    return True


def arxiv_id_from_text(text: str) -> str:
    match = ARXIV_RE.search(text or "")
    return match.group(1) if match else ""


def infer_arxiv_id(row: dict[str, str]) -> str:
    for field in ("id", "url"):
        arxiv_id = arxiv_id_from_text(clean(row.get(field)))
        if arxiv_id:
            return arxiv_id
    return ""


def infer_pdf_url(row: dict[str, str], arxiv_id: str) -> str:
    if arxiv_id:
        return f"https://arxiv.org/pdf/{arxiv_id}.pdf"

    identifier = clean(row.get("id"))
    openreview_match = OPENREVIEW_RE.fullmatch(identifier)
    if openreview_match:
        return f"https://openreview.net/pdf?id={openreview_match.group(1)}"

    url = clean(row.get("url"))
    if not url:
        return ""

    url_arxiv_id = arxiv_id_from_text(url)
    if url_arxiv_id:
        return f"https://arxiv.org/pdf/{url_arxiv_id}.pdf"

    parsed = urllib.parse.urlparse(url)
    lower_url = url.lower()
    lower_path = parsed.path.lower()
    if lower_path.endswith(".pdf"):
        return url
    if "openreview.net/pdf" in lower_url:
        return url
    if "papers.nips.cc" in lower_url and lower_path.endswith(".pdf"):
        return url

    return ""


def safe_stem(row: dict[str, str], arxiv_id: str) -> str:
    rank = row_rank(row)
    identifier = arxiv_id or clean(row.get("id")) or clean(row.get("url"))
    if not identifier:
        digest = hashlib.sha1(clean(row.get("title")).encode("utf-8")).hexdigest()[:10]
        identifier = "title-" + digest
    identifier = identifier.replace("https://", "").replace("http://", "")
    identifier = re.sub(r"[^A-Za-z0-9._-]+", "_", identifier).strip("_")
    identifier = identifier[:80] or "paper"
    return f"{rank:04d}_{identifier}"


def find_existing_pdf(arxiv_id: str) -> Path | None:
    if not arxiv_id:
        return None
    for path in sorted((ROOT / "papers").glob(f"*_{arxiv_id}/paper.pdf")):
        if path.is_file():
            return path
    return None


def source_has_files(path: Path) -> bool:
    if not path.is_dir():
        return False
    return any(path.iterdir())


def find_existing_source(arxiv_id: str) -> Path | None:
    if not arxiv_id:
        return None
    for path in sorted((ROOT / "papers").glob(f"*_{arxiv_id}/source")):
        if source_has_files(path):
            return path
    return None


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def is_pdf(path: Path) -> bool:
    try:
        with path.open("rb") as handle:
            head = handle.read(1024)
    except OSError:
        return False
    return b"%PDF" in head


def download_pdf(url: str, destination: Path, timeout: float) -> tuple[str, int, str]:
    destination.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = destination.with_suffix(destination.suffix + ".tmp")
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = response.read()
    except urllib.error.HTTPError as exc:
        return "failed", 0, f"HTTP {exc.code}"
    except urllib.error.URLError as exc:
        return "failed", 0, str(exc.reason)
    except TimeoutError:
        return "failed", 0, "timeout"

    tmp_path.write_bytes(payload)
    if not is_pdf(tmp_path):
        tmp_path.unlink(missing_ok=True)
        return "failed", 0, "response was not a PDF"

    tmp_path.replace(destination)
    return "downloaded", destination.stat().st_size, ""


def source_url(arxiv_id: str) -> str:
    return f"https://arxiv.org/e-print/{arxiv_id}" if arxiv_id else ""


def mostly_text(data: bytes) -> bool:
    if not data:
        return False
    sample = data[:8192]
    if b"\x00" in sample:
        return False
    printable = sum(1 for byte in sample if byte in b"\n\r\t" or 32 <= byte <= 126)
    return printable / len(sample) > 0.85


def looks_like_tex(data: bytes) -> bool:
    sample = data[:8192].lower()
    return (
        b"\\documentclass" in sample
        or b"\\begin{" in sample
        or b"\\section" in sample
        or b"\\title{" in sample
    )


def safe_tar_members(archive: tarfile.TarFile, destination: Path) -> list[tarfile.TarInfo]:
    destination_root = destination.resolve()
    members = []
    for member in archive.getmembers():
        if member.issym() or member.islnk():
            continue
        target = (destination / member.name).resolve()
        if target == destination_root or destination_root in target.parents:
            members.append(member)
    return members


def unpack_source_archive(archive_path: Path, destination: Path) -> tuple[str, str]:
    try:
        with tarfile.open(archive_path, "r:*") as archive:
            archive.extractall(destination, members=safe_tar_members(archive, destination))
        archive_path.unlink(missing_ok=True)
        return "downloaded", ""
    except tarfile.TarError:
        pass

    raw = archive_path.read_bytes()
    if raw.startswith(b"\x1f\x8b"):
        try:
            raw = gzip.decompress(raw)
        except OSError as exc:
            return "failed", f"could not unpack gzip source: {exc}"

    if looks_like_tex(raw) or mostly_text(raw):
        (destination / "main.tex").write_bytes(raw)
        archive_path.unlink(missing_ok=True)
        return "downloaded", ""

    shutil.move(str(archive_path), destination / "source.raw")
    return "downloaded-raw", "source format was not tar/gzip/TeX"


def download_arxiv_source(
    arxiv_id: str,
    destination: Path,
    timeout: float,
    force: bool,
) -> tuple[str, str]:
    if source_has_files(destination) and not force:
        return "present", ""

    if destination.exists() and force:
        shutil.rmtree(destination)

    destination.mkdir(parents=True, exist_ok=True)
    archive_path = destination / "source.download"
    request = urllib.request.Request(source_url(arxiv_id), headers={"User-Agent": USER_AGENT})

    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            archive_path.write_bytes(response.read())
    except urllib.error.HTTPError as exc:
        archive_path.unlink(missing_ok=True)
        return "failed", f"HTTP {exc.code}"
    except urllib.error.URLError as exc:
        archive_path.unlink(missing_ok=True)
        return "failed", str(exc.reason)
    except TimeoutError:
        archive_path.unlink(missing_ok=True)
        return "failed", "timeout"

    return unpack_source_archive(archive_path, destination)


def manifest_row(
    row: dict[str, str],
    arxiv_id: str,
    artifact_path: str,
    pdf_url: str,
    pdf_path: str,
    pdf_status: str,
    pdf_bytes: int,
    pdf_error: str,
    source_url_value: str,
    source_path: str,
    source_status: str,
    source_error: str,
) -> dict[str, Any]:
    return {
        "rank": clean(row.get("rank")),
        "title": clean(row.get("title")),
        "authors": clean(row.get("authors")),
        "year": clean(row.get("year")),
        "id": clean(row.get("id")),
        "status": clean(row.get("status")),
        "role": clean(row.get("role")),
        "sub_area": clean(row.get("sub_area")),
        "source": clean(row.get("source")),
        "citation_count": clean(row.get("citation_count")),
        "confidence": clean(row.get("confidence")),
        "url": clean(row.get("url")),
        "arxiv_id": arxiv_id,
        "artifact_path": artifact_path,
        "pdf_url": pdf_url,
        "pdf_path": pdf_path,
        "pdf_status": pdf_status,
        "pdf_bytes": pdf_bytes or "",
        "pdf_error": pdf_error,
        "source_url": source_url_value,
        "source_path": source_path,
        "source_status": source_status,
        "source_error": source_error,
    }


def write_manifest(out_dir: Path, rows: list[dict[str, Any]]) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "manifest.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=MANIFEST_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def print_summary(rows: list[dict[str, Any]], out_dir: Path, executed: bool) -> None:
    pdf_counts: dict[str, int] = {}
    source_counts: dict[str, int] = {}
    for row in rows:
        pdf_status = clean(row.get("pdf_status"))
        source_status = clean(row.get("source_status"))
        pdf_counts[pdf_status] = pdf_counts.get(pdf_status, 0) + 1
        source_counts[source_status] = source_counts.get(source_status, 0) + 1

    print(f"Rows in manifest: {len(rows)}")
    print("PDF statuses:")
    for key in sorted(pdf_counts):
        print(f"  {key}: {pdf_counts[key]}")
    print("Source statuses:")
    for key in sorted(source_counts):
        print(f"  {key}: {source_counts[key]}")
    if executed:
        print(f"Manifest: {rel(out_dir / 'manifest.csv')}")
        print(f"Extra papers directory: {rel(out_dir)}")
    else:
        print("Dry run only. Re-run with --execute to download into papers_extra/.")


def main() -> int:
    args = parse_args()
    if not args.input.is_file():
        raise SystemExit(f"Missing input CSV: {args.input}")
    if args.limit < 0:
        raise SystemExit("--limit must be non-negative")

    rows: list[dict[str, Any]] = []
    processed = 0

    with args.input.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if not matches_filters(row, args):
                continue

            arxiv_id = infer_arxiv_id(row)
            stem = safe_stem(row, arxiv_id)
            extra_artifact_dir = args.out / stem
            artifact_path = ""

            pdf_url_value = infer_pdf_url(row, arxiv_id) if args.fetch_pdf else ""
            pdf_path = ""
            pdf_status = "disabled"
            pdf_bytes = 0
            pdf_error = ""
            pdf_destination = extra_artifact_dir / "paper.pdf"

            if args.fetch_pdf:
                existing_pdf = None if args.no_existing else find_existing_pdf(arxiv_id)
                if existing_pdf is not None:
                    artifact_path = rel(existing_pdf.parent)
                    pdf_path = rel(existing_pdf)
                    pdf_status = "existing"
                    pdf_bytes = existing_pdf.stat().st_size
                elif not pdf_url_value:
                    pdf_status = "unresolved"
                elif pdf_destination.is_file() and not args.force:
                    pdf_path = rel(pdf_destination)
                    pdf_status = "present"
                    pdf_bytes = pdf_destination.stat().st_size
                else:
                    pdf_path = rel(pdf_destination)
                    pdf_status = "pending"

            source_url_value = source_url(arxiv_id) if args.fetch_source and arxiv_id else ""
            source_path = ""
            source_status = "disabled"
            source_error = ""
            source_destination = extra_artifact_dir / "source"

            if args.fetch_source:
                existing_source = None if args.no_existing else find_existing_source(arxiv_id)
                if existing_source is not None:
                    artifact_path = rel(existing_source.parent)
                    source_path = rel(existing_source)
                    source_status = "existing"
                elif not arxiv_id:
                    source_status = "unavailable"
                elif source_has_files(source_destination) and not args.force:
                    source_path = rel(source_destination)
                    source_status = "present"
                else:
                    source_path = rel(source_destination)
                    source_status = "pending"

            has_pending = pdf_status == "pending" or source_status == "pending"
            if has_pending and args.limit and processed >= args.limit:
                if pdf_status == "pending":
                    pdf_status = "skipped-limit"
                    pdf_path = ""
                if source_status == "pending":
                    source_status = "skipped-limit"
                    source_path = ""
                has_pending = False

            if has_pending:
                processed += 1
                if args.execute:
                    if pdf_status == "pending":
                        pdf_status, pdf_bytes, pdf_error = download_pdf(
                            pdf_url_value,
                            pdf_destination,
                            args.timeout,
                        )
                        pdf_path = rel(pdf_destination) if pdf_status == "downloaded" else ""

                    if source_status == "pending":
                        source_status, source_error = download_arxiv_source(
                            arxiv_id,
                            source_destination,
                            args.timeout,
                            args.force,
                        )
                        source_path = (
                            rel(source_destination)
                            if source_status in {"downloaded", "downloaded-raw", "present"}
                            else ""
                        )

                    if args.sleep > 0:
                        time.sleep(args.sleep)
                else:
                    if pdf_status == "pending":
                        pdf_status = "planned"
                    if source_status == "pending":
                        source_status = "planned"

            rows.append(
                manifest_row(
                    row,
                    arxiv_id,
                    artifact_path
                    or (
                        rel(extra_artifact_dir)
                        if pdf_path or source_path or pdf_status == "planned" or source_status == "planned"
                        else ""
                    ),
                    pdf_url_value,
                    pdf_path,
                    pdf_status,
                    pdf_bytes,
                    pdf_error,
                    source_url_value,
                    source_path,
                    source_status,
                    source_error,
                )
            )

    if args.execute:
        write_manifest(args.out, rows)
    print_summary(rows, args.out, args.execute)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
