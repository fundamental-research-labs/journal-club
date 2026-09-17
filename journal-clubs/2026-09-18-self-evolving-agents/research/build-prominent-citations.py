#!/usr/bin/env python3
"""Render the reviewed citation map. Python 3 standard library only.

Run from any directory; --check verifies that the Markdown matches the JSON.
The input is coordinator-reviewed prominent-citations.json, not raw worker output.
This checks identities/counts, not the truth of citation contexts.
"""

import argparse
from collections import defaultdict
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent


def identity(url):
    match = re.search(r'arxiv\.org/(?:abs|html|pdf)/((?:\d{4}\.\d{4,5}|[a-z.-]+/\d{7}))(?:v\d+)?', url)
    if match:
        return 'arxiv:' + match.group(1)
    p = urlsplit(url)
    return p.netloc.lower() + p.path.rstrip('/') + ('?' + p.query if p.query else '')


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def render(data, records, thesis):
    register = {r['key']: r for r in records}
    seeds = data['seeds']
    keys = [s['source_key'] for s in seeds]
    if len(keys) != len(set(keys)):
        raise ValueError('Duplicate citing source keys')
    cited_urls = {identity(u) for u in re.findall(r'\]\((https?://[^)]+)\)', thesis)}
    cited_families = {r.get('family', r['key']) for r in records if identity(r['url']) in cited_urls}
    aggregate = defaultdict(dict)
    titles = {}
    edge_count = 0
    for seed in seeds:
        key = seed['source_key']
        if key not in register or not (ROOT / seed['note']).is_file():
            raise ValueError(f'Unknown seed or missing note: {key}')
        if not seed['inspection_source'] or not seed['sections_checked']:
            raise ValueError(f'Missing inspection provenance: {key}')
        seen = set()
        for edge in seed['edges']:
            target = identity(edge['url'])
            ck = edge.get('cited_key')
            if ck and ck not in register:
                raise ValueError(f'Unknown cited key: {ck}')
            family = register[ck].get('family', ck) if ck else target
            if family in seen:
                raise ValueError(f'Duplicate citation family in {key}: {family}')
            seen.add(family)
            if not edge['locator'] or not edge['context']:
                raise ValueError(f'Missing edge context: {key} -> {target}')
            seed_family = register[key].get('family', key)
            aggregate[family].setdefault(seed_family, []).append((seed, edge))
            titles.setdefault(family, edge)
            edge_count += 1
    lines = ['# Prominent citations', '',
             f"Reviewed {data['review_date']}; research cutoff {data['cutoff']}.", '',
             f"**{len(seeds)} citing papers; {edge_count} selected edges; {len(aggregate)} cited families.** "
             'These are selected, context-verified references, not complete bibliographies or a field-wide influence ranking.', '',
             'Each paper below has its own list. Counts deduplicate citing and cited evidence families; '
             'repeated mentions and versions do not add votes. Distinct papers are not necessarily independent research groups. '
             'Author/project independence has not been comprehensively classified. '
             'DGM and Hyperagents share a lineage; benchmark reuse and shared models also limit independence.', '',
             'The citation context is a paraphrase of the citing authors’ use. '
             'A verified edge does not verify the cited work’s findings. '
             '“Directly cited” below is a URL check; explanatory integration requires the '
             '[thesis coverage audit](thesis-coverage.md). Unregistered leads remain citation discoveries, not reviewed evidence.', '',
             'Edit [structured data](prominent-citations.json); rebuild with '
             '`python3 research/build-prominent-citations.py` from the session directory '
             '(standard library only). Add `--check` to detect stale output.', '',
             '## Recurring citations', '',
             '| Cited work | Citing families | Citing papers | Essay citation |',
             '| --- | ---: | --- | --- |']
    for family, incoming in sorted(aggregate.items(), key=lambda item: (-len(item[1]), titles[item[0]]['title'])):
        if len(incoming) < 2:
            continue
        e = titles[family]
        links = []
        for group in incoming.values():
            seed = group[0][0]
            links.append(f"[{seed['source_key']}](#{seed['source_key']})")
        used = 'Directly cited' if family in cited_families or identity(e['url']) in cited_urls else 'No direct citation; review disposition'
        lines.append(f"| [{cell(e['title'])}]({e['url']}) | {len(incoming)} | {', '.join(links)} | {used} |")
    lines += ['', 'Single-seed direct predecessors and decisive baselines still require review; recurrence is not an inclusion threshold.', '', '## Paper index', '']
    lines += [f"- [{s['title']}](#{s['source_key']})" for s in seeds]
    for seed in seeds:
        lines += ['', f'<a id="{seed["source_key"]}"></a>', '', f"## {seed['title']}", '',
                  f"[Inspected version]({seed['url']}) · [Reading note]({seed['note']})", '',
                  f"**Inspection:** {cell(seed['access'])} Sections: {cell('; '.join(seed['sections_checked']))}.", '',
                  f"**Scope:** {cell(seed['limitations'])}", '',
                  '| Prominent reference | Role in this paper | Locator and citation context | Cited-work reading status |',
                  '| --- | --- | --- | --- |']
        for e in seed['edges']:
            record = register.get(e.get('cited_key'), {})
            note = record.get('notes')
            status = f"[{cell(record.get('access_depth', 'See source record'))}]({note})" if note else cell(record.get('access_depth', 'Bibliographic identity/context only; no substantive review in this pass'))
            lines.append(f"| [{cell(e['title'])}]({e['url']}) | {cell(e['role'])} | {cell(e['locator'])}: {cell(e['context'])} | {status} |")
    lines += ['', '## Limits and exclusions', '']
    lines += ['- ' + item for item in data['limits']]
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    text = render(json.loads((ROOT / 'prominent-citations.json').read_text()),
                  json.loads((ROOT / 'sources.json').read_text()),
                  (ROOT.parent / 'analysis/thesis.md').read_text())
    output = ROOT / 'prominent-citations.md'
    if args.check:
        if not output.exists() or output.read_text() != text:
            raise SystemExit('prominent-citations.md is stale; rebuild it')
        print('Citation identities, provenance fields, counts, and rendered output checked.')
    else:
        output.write_text(text)
        print(output)


if __name__ == '__main__':
    main()
