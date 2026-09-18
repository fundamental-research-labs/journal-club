#!/usr/bin/env python3
"""Regenerate source excerpts: uv run --with pymupdf python slides/figures/extract.py.

Run from any directory. Retained PDFs are read unchanged. Missing sources are
downloaded only into a temporary directory; attributed excerpts are retained.
Crop rectangles use PDF points from the top-left; page numbers are one-based.
"""
import hashlib
import argparse
import json
from pathlib import Path
import tempfile
import urllib.request
import pymupdf

ROOT = Path(__file__).resolve().parent
ORIGINALS = ROOT.parents[1] / 'research' / 'originals'
SPECS = [
    ('finevo-figure-1a', '2026-finevo-bench', 'v1', '2608.06144v1', 3, [54, 53, 317, 227], 'Figure 1(a): complete landscape panel; task-workspace panel and caption omitted'),
    ('hyperagents-figure-1-loops', '2026-hyperagents', 'v1', '2603.19461v1', 4, [70, 175, 332, 387], 'Figure 1: left agent/archive and central loops for both methods; right implementation traces and caption omitted'),
    ('agentstream-table-5', '2026-agentstream', 'v1', '2608.00155v1', 11, [89, 108, 505, 187], 'Table 5: complete table, all methods and columns; caption omitted'),
    ('seal-figure-6', '2025-self-adapting-language-models', 'v2', '2506.10943v2', 8, [344, 497, 507, 661], 'Figure 6: complete retention heatmap, axes and color scale; caption omitted'),
    ('wikiskill-figure-2', '2026-wikiskill', 'v1', '2608.27454v1', 4, [61, 82, 535, 306], 'Figure 2: complete conceptual framework; caption omitted'),
    ('finevo-figure-1', '2026-finevo-bench', 'v1', '2608.06144v1', 3, [54, 53, 558, 227], 'Figure 1: both panels, benchmark landscape and example task workspace; caption omitted'),
    ('harness-figure-2', '2026-harness-evolution-evaluation', 'v2', '2607.12227v2', 3, [108, 70, 504, 229], 'Figure 2: all four method panels and legend; caption omitted'),
    ('hyperagents-figure-1', '2026-hyperagents', 'v1', '2603.19461v1', 4, [70, 175, 542, 387], 'Figure 1: both conceptual panels; caption omitted'),
    ('seal-figure-1', '2025-self-adapting-language-models', 'v2', '2506.10943v2', 2, [106, 70, 505, 174], 'Figure 1: complete conceptual diagram; caption omitted'),
    ('hyperagents-figure-3', '2026-hyperagents', 'v1', '2603.19461v1', 10, [226, 65, 544, 169], 'Figure 3: middle and right held-out panels with comparators, axes and uncertainty; left training panel and caption omitted'),
    ('wikiskill-table-1', '2026-wikiskill', 'v1', '2608.27454v1', 8, [74, 83, 522, 235], 'Table 1: headers and complete Qwen-3.5-4B / 9B blocks; other model blocks and caption omitted'),
    ('seal-table-2', '2025-self-adapting-language-models', 'v2', '2506.10943v2', 8, [106, 70, 524, 156], 'Table 2: complete table; caption omitted'),
    ('finevo-table-5', '2026-finevo-bench', 'v1', '2608.06144v1', 6, [60, 278, 288, 368], 'Table 5: complete table; caption omitted'),
    ('harness-table-1', '2026-harness-evolution-evaluation', 'v2', '2607.12227v2', 6, [118, 70, 494, 173], 'Table 1: complete table; caption omitted'),
    ('hyperagents-figure-4', '2026-hyperagents', 'v1', '2603.19461v1', 13, [94, 64, 518, 202], 'Figure 4: both panels, legends, axes and error bars; caption omitted'),
]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--only', nargs='+', help='Regenerate named assets without .png; preserve other manifest entries.')
    args = parser.parse_args()
    selected = set(args.only or [])
    known = {s[0] for s in SPECS} | {'agentstream-figure-1b'}
    if selected - known:
        parser.error('Unknown assets: ' + ', '.join(sorted(selected - known)))
    manifest_path = ROOT / 'extraction.json'
    manifest = json.loads(manifest_path.read_text()) if selected and manifest_path.exists() else []
    manifest = [m for m in manifest if Path(m['asset']).stem not in selected]
    with tempfile.TemporaryDirectory() as temp:
        # The source HTML provides this original artwork directly. Crop only
        # panel (a); retain all of panel (b), its labels and state-update loop.
        url = 'https://arxiv.org/html/2608.00155v1/evaluation_compare.png'
        source = Path(temp) / 'agentstream-figure-1.png'
        if not selected or 'agentstream-figure-1b' in selected:
            urllib.request.urlretrieve(url, source)
            image_doc = pymupdf.open(source)
            with pymupdf.open('pdf', image_doc.convert_to_pdf()) as doc:
                page = doc[0]
                # Image DPI metadata determines the converted page size.
                sx, sy = page.rect.width / 1600, page.rect.height / 900
                page.get_pixmap(matrix=pymupdf.Matrix(1/sx, 1/sy),
                                clip=pymupdf.Rect(0, 290*sy, 1600*sx, 900*sy), alpha=False).save(ROOT / 'agentstream-figure-1b.png')
            manifest.append(dict(asset='agentstream-figure-1b.png', url=url, version='v1',
                             figure='1(b)', crop_pixels=[0, 290, 1600, 900],
                             scope='Panel (b) complete; independent-evaluation panel (a) omitted',
                             source_sha256=hashlib.sha256(source.read_bytes()).hexdigest()))
        for name, key, version, arxiv, page, rect, scope in SPECS:
            if selected and name not in selected:
                continue
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
