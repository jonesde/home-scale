#!/usr/bin/env python3
"""Merge analysis/fragments/*.jsonl into analysis/implication.csv."""

from __future__ import annotations

import csv
import json
from pathlib import Path

ANALYSIS = Path(__file__).resolve().parent
FRAGMENTS = ANALYSIS / "fragments"
OUT = ANALYSIS / "implication.csv"

FIELDS = [
    "impl_key",
    "effect_slug",
    "source_path",
    "clause",
    "role",
    "aspect",
    "resource",
    "observed_text",
    "implied_text",
    "inference_kind",
    "description",
    "operator",
    "value_si",
    "si_unit",
    "value_text",
    "confidence",
    "notes",
    "updated",
]


def load_rows() -> list[dict]:
    rows = []
    for path in sorted(FRAGMENTS.glob("*.jsonl")):
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"{path.name}:{lineno}: {exc}") from exc
            row = {}
            for key in FIELDS:
                val = obj.get(key)
                if val is None:
                    row[key] = ""
                else:
                    row[key] = val
            rows.append(row)
    rows.sort(key=lambda r: r["impl_key"])
    keys = [r["impl_key"] for r in rows]
    dupes = sorted({k for k in keys if keys.count(k) > 1})
    if dupes:
        raise SystemExit("duplicate impl_key: " + ", ".join(dupes))
    return rows


def main() -> int:
    rows = load_rows()
    with OUT.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    slugs = {}
    for row in rows:
        slugs[row["effect_slug"]] = slugs.get(row["effect_slug"], 0) + 1
    print(f"wrote {OUT} ({len(rows)} rows, {len(slugs)} effects)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
