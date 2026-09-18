#!/usr/bin/env python3
"""Regenerate source excerpts: uv run --with pymupdf python slides/figures/extract.py.

Run from any directory. Retained PDFs are read unchanged. FinEvo is downloaded
only into a temporary directory; only its attributed Table 5 excerpt is retained.
Crop rectangles use PDF points from the top-left; page numbers are one-based.
"""
import hashlib
import json
from pathlib import Path
import tempfile
import urllib.request
import pymupdf

ROOT = Path(__file__).resolve().parent
ORIGINALS = ROOT.parents[1] / 'research' / 'originals'
SPECS = [
    ('hyperagents-figure-3', '2026-hyperagents', 'v1', '2603.19461v1', 10, [226, 65, 544, 169], 'Figure 3: middle and right held-out panels with comparators, axes and uncertainty; left training panel and caption omitted'),
    ('wikiskill-table-1', '2026-wikiskill', 'v1', '2608.27454v1', 8, [74, 83, 522, 235], 'Table 1: headers and complete Qwen-3.5-4B / 9B blocks; other model blocks and caption omitted'),
    ('seal-table-2', '2025-self-adapting-language-models', 'v2', '2506.10943v2', 8, [106, 70, 524, 156], 'Table 2: complete table; caption omitted'),
    ('finevo-table-5', '2026-finevo-bench', 'v1', '2608.06144v1', 6, [60, 278, 288, 368], 'Table 5: complete table; caption omitted'),
    ('harness-table-1', '2026-harness-evolution-evaluation', 'v2', '2607.12227v2', 6, [118, 70, 494, 173], 'Table 1: complete table; caption omitted'),
    ('hyperagents-figure-4', '2026-hyperagents', 'v1', '2603.19461v1', 13, [94, 64, 518, 202], 'Figure 4: both panels, legends, axes and error bars; caption omitted'),
]

def main():
    manifest = []
    with tempfile.TemporaryDirectory() as temp:
        for name, key, version, arxiv, page, rect, scope in SPECS:
            source = ORIGINALS / key / f'{key}-paper-{version}.pdf'
            url = f'https://arxiv.org/pdf/{arxiv}'
            if not source.exists():
                source = Path(temp) / f'{key}.pdf'
                urllib.request.urlretrieve(url, source)
            with pymupdf.open(source) as doc:
                doc[page - 1].get_pixmap(matrix=pymupdf.Matrix(3, 3), clip=pymupdf.Rect(rect), alpha=False).save(ROOT / f'{name}.png')
            manifest.append(dict(asset=f'{name}.png', url=url, version=version, pdf_page=page,
                                 crop_points=rect, scale=3, scope=scope,
                                 source_sha256=hashlib.sha256(source.read_bytes()).hexdigest()))
    (ROOT / 'extraction.json').write_text(json.dumps(manifest, indent=2) + '\n')
    print(f'Extracted {len(manifest)} source visuals without redrawing.')

if __name__ == '__main__':
    main()
