#!/usr/bin/env python3
"""Recolor domain icons from the base white SVGs using category colors.

Reads white-stroked SVGs from ../domain_icons/, replaces stroke/fill="white"
with the category icon color, and writes to this directory.

Usage:
    python process_icons.py          # recolor all icons
    python process_icons.py dns      # recolor a single icon

To change colors: edit CATEGORY_COLORS below, then re-run.
"""

import re
import sys
from pathlib import Path

SRC_DIR = Path(__file__).parent.parent / "domain_icons"
OUT_DIR = Path(__file__).parent

# ── Category → domain mapping ───────────────────────────────────────
# Must match DOMAIN_CATEGORIES in analysis/tables.py

CATEGORY_DOMAINS = {
    "code": [
        "dbschema", "dns", "docker", "filesystem", "graphviz",
        "infra", "json", "makefile", "malware", "python", "translation",
    ],
    "science": [
        "aviation", "circuit", "crystal", "mathlean", "molecule",
        "protein", "quantum", "robotics", "satellite", "starcatalog", "weather",
    ],
    "creative": [
        "audiosyn", "fiction", "fonteng", "latex", "musicsheet",
        "obj3d", "screenplay", "slides", "subtitles", "vector", "weaving",
    ],
    "records": [
        "accounting", "calendar", "edifact", "emails", "genealogy",
        "geodata", "geotrack", "hamradio", "libcatalog", "spreadsheet", "treebank",
    ],
    "everyday": [
        "chess", "earncall", "foodmenu", "jobboard", "landmarks",
        "playlist", "recipe", "transit",
    ],
}

# ── Category colors (HSV-based warm spread: rose → coral → orange → gold → yellow)
# bg: base color (pre-fade), border: darkened border/text
# icon: derived from bg (darkened 20%, saturated 60%) — vivid on pastel tiles

CATEGORY_COLORS = {
    "code":     {"bg": "#F7A8A8", "border": "#885C5C", "icon": "#C66060"},
    "science":  {"bg": "#F7B8A8", "border": "#88655C", "icon": "#C67560"},
    "creative": {"bg": "#F7C9A8", "border": "#886F5C", "icon": "#C68B60"},
    "records":  {"bg": "#F7D6A8", "border": "#88765C", "icon": "#C69B60"},
    "everyday": {"bg": "#F7E8A8", "border": "#88805C", "icon": "#C6B260"},
}

# Reverse lookup: domain → category
_DOMAIN_TO_CAT = {}
for cat, domains in CATEGORY_DOMAINS.items():
    for d in domains:
        _DOMAIN_TO_CAT[d] = cat


def colorize(svg_text: str, color: str, bg: str) -> str:
    """Replace white stroke/fill values with the given hex color.

    Also handles icons with ribbon banners:
      - fill="#F5F5F5" (light grey bg) → category bg color
      - fill="black" (text on ribbon)  → icon stroke color
    """
    result = re.sub(r'stroke="white"', f'stroke="{color}"', svg_text, flags=re.IGNORECASE)
    result = re.sub(r'fill="white"', f'fill="{color}"', result, flags=re.IGNORECASE)
    # Ribbon background → category tile bg
    result = re.sub(r'fill="#[Ff]5[Ff]5[Ff]5"', f'fill="{bg}"', result)
    # Ribbon text → icon stroke color
    result = re.sub(r'fill="black"', f'fill="{color}"', result, flags=re.IGNORECASE)
    # Black strokes inside ribbon lettering
    result = re.sub(r'stroke="black"', f'stroke="{color}"', result, flags=re.IGNORECASE)
    return result


def process(domain: str) -> None:
    """Colorize a single domain icon."""
    src = SRC_DIR / f"{domain}.svg"
    if not src.exists():
        print(f"  SKIP {domain}: {src} not found")
        return

    cat = _DOMAIN_TO_CAT.get(domain)
    if not cat:
        print(f"  SKIP {domain}: not in any category")
        return

    color = CATEGORY_COLORS[cat]["icon"]
    bg = CATEGORY_COLORS[cat]["bg"]
    svg_text = src.read_text()
    colored = colorize(svg_text, color, bg)

    out = OUT_DIR / f"{domain}.svg"
    out.write_text(colored)
    print(f"  {domain:15s} → {color} ({cat})")


def main():
    targets = sys.argv[1:] if len(sys.argv) > 1 else sorted(_DOMAIN_TO_CAT.keys())
    print(f"Recoloring {len(targets)} icons...")
    for domain in targets:
        process(domain)
    print("Done.")


if __name__ == "__main__":
    main()
