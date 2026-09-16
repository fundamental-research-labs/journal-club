"""Recalculate AgentStream Table 2 from version-1 Tables 11–13.

Run: python3 research/check-agentstream-aggregates.py
Requires Python 3 standard library and network access. Reads the canonical HTML
without retaining a manuscript copy. This checks published rounded table cells;
it does not reproduce experiments or recover unrounded results.
"""

import json
import statistics
import urllib.request
from html.parser import HTMLParser

URL = "https://arxiv.org/html/2608.00155v1"


class Tables(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tables = []
        self.table = self.row = self.cell = None
        self.depth = self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self.depth += 1
            if self.depth == 1:
                self.table = []
        if self.depth == 1 and tag == "tr":
            self.row = []
        if self.depth == 1 and tag in ("td", "th"):
            self.cell = []
        if tag == "annotation":
            self.skip += 1

    def handle_endtag(self, tag):
        if tag == "annotation":
            self.skip -= 1
        if tag in ("td", "th") and self.depth == 1 and self.cell is not None:
            self.row.append(" ".join("".join(self.cell).split()))
            self.cell = None
        if tag == "tr" and self.depth == 1 and self.row is not None:
            self.table.append(self.row)
            self.row = None
        if tag == "table":
            if self.depth == 1:
                self.tables.append(self.table)
            self.depth -= 1

    def handle_data(self, data):
        if self.cell is not None and not self.skip:
            self.cell.append(data)


def main():
    parser = Tables()
    with urllib.request.urlopen(URL, timeout=60) as response:
        parser.feed(response.read().decode())
    candidates = [table for table in parser.tables
                  if table and table[0][:2] == ["Methods", "Mode"]]
    assert len(candidates) == 4, "Expected main table and three per-seed tables"
    modes = ("Isolated", "Sequential", "Interleaved")
    pooled = {mode: [] for mode in modes}
    seed_means = {mode: [] for mode in modes}
    for table in candidates[1:]:
        per_seed = {mode: [] for mode in modes}
        baseline = None
        for row in table[1:]:
            if "Vanilla" in row:
                baseline = float(row[-1])
                continue
            assert baseline is not None
            mode = row[1] if len(row) == 9 else row[0]
            per_seed[mode].append(float(row[-1]) - baseline)
        for mode in modes:
            assert len(per_seed[mode]) == 15
            pooled[mode].extend(per_seed[mode])
            seed_means[mode].append(statistics.mean(per_seed[mode]))
    result = {}
    for mode, values in pooled.items():
        result[mode] = {
            "model_method_seed_cells": len(values),
            "positive": sum(value > 1e-6 for value in values),
            "negative": sum(value < -1e-6 for value in values),
            "ties": sum(abs(value) < 1e-6 for value in values),
            "mean_gain_percentage_points": statistics.mean(values),
            "three_seed_means": seed_means[mode],
            "sample_sd_of_seed_means": statistics.stdev(seed_means[mode]),
        }
    print(json.dumps({"source": URL, "results": result}, indent=2))


if __name__ == "__main__":
    main()
