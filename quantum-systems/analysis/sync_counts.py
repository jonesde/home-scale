#!/usr/bin/env python3
"""Rewrite the count lines quoted in the docs from qs-analysis.db.

Run after `python3 analysis/rebuild.py` when it prints count-drift warnings:

    python3 analysis/sync_counts.py

It touches only the count phrases the rebuild checks (catalog size, mapping
confidence split, sourced-effect count, the "Load" lines). INDEX.md rows are
not touched; fix those by hand or from frontmatter.
"""

from __future__ import annotations

import re
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    db = sqlite3.connect(ROOT / "qs-analysis.db")
    one = lambda sql: db.execute(sql).fetchone()[0]
    n_effect = one("SELECT COUNT(*) FROM effect")
    n_ec = one("SELECT COUNT(*) FROM effect_constraint")
    n_impl = one("SELECT COUNT(*) FROM implication")
    n_pred = one("SELECT COUNT(*) FROM implication WHERE origin = 'predicted'")
    n_ext = n_impl - n_pred
    n_src = one("SELECT COUNT(*) FROM source")
    n_sourced = one("SELECT COUNT(DISTINCT effect_slug) FROM source")
    n_isrc = one("SELECT COUNT(*) FROM implication_source")
    conf = dict(db.execute("SELECT confidence_mapping, COUNT(*) FROM effect GROUP BY 1"))
    high, medium, low = (conf.get(k, 0) for k in ("high", "medium", "low"))

    rules = {
        "library/INDEX.md": [
            (r"\*\*Sourcing:\*\* \d+ of \d+ files", f"**Sourcing:** {n_sourced} of {n_effect} files"),
            (r"\*\*Status:\*\* \d+ formal", f"**Status:** {n_effect} formal"),
            (r"Mapping: \d+ High · \d+ Medium · \d+ Low", f"Mapping: {high} High · {medium} Medium · {low} Low"),
        ],
        "README.md": [
            (r"Catalog: \d+ formal entries", f"Catalog: {n_effect} formal entries"),
            (r"\d+ High, \d+ Medium, \d+ Low", f"{high} High, {medium} Medium, {low} Low"),
        ],
        "Summary.md": [
            (r"\| Formal effects \| \d+ ", f"| Formal effects | {n_effect} "),
            (r"\d+ High · \d+ Medium · \d+ Low", f"{high} High · {medium} Medium · {low} Low"),
            (r"\| Sourced effects \| \d+ of \d+", f"| Sourced effects | {n_sourced} of {n_effect}"),
            (r"\| Extracted implications \| \d+ \|", f"| Extracted implications | {n_ext} |"),
        ],
    }
    load = [
        (r"\d+ `effect` · \d+ `effect_constraint` · \d+ `implication` \(\d+ extracted, \d+ predicted\)",
         f"{n_effect} `effect` · {n_ec} `effect_constraint` · {n_impl} `implication` ({n_ext} extracted, {n_pred} predicted)"),
        (r"\d+ `source` \(\d+ of \d+ effects sourced\) · \d+ `implication_source`",
         f"{n_src} `source` ({n_sourced} of {n_effect} effects sourced) · {n_isrc} `implication_source`"),
    ]
    rules["AGENTS.md"] = load
    rules["analysis/README.md"] = load
    for rel, pairs in rules.items():
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        for pattern, new in pairs:
            text, k = re.subn(pattern, new, text)
            if k == 0:
                print(f"sync_counts: {rel}: nothing matched {pattern!r}")
        path.write_text(text, encoding="utf-8")
    print(f"sync_counts: {n_effect} effects, {n_sourced} sourced, mapping {high}/{medium}/{low}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
