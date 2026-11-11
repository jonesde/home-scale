#!/usr/bin/env python3
"""Edit extracted-implication rows in analysis/fragments/*.jsonl in place.

Only the rows that are changed are re-serialised. Every other line of the
fragment files stays byte-identical, so a diff shows exactly what was edited.

Use from a short script, run from anywhere:

    import sys; sys.path.insert(0, "analysis")
    import fragtools as ft
    ft.apply({
        "skin-effect:failure_mode:thick-conductor": {
            "observed_text": "...",          # restate the sourced §4.3 fact
            "basis": "measured",             # measured | model | convention | computed
            "form": "crossover",             # failure rows only: threshold | crossover
            "sources": ["S1", "S4"],         # keys from the effect file's Sources table
        },
    }, "2026-11-12")

`apply` sets `updated` on every row it touches and fails if a key is not found.
Do not add or delete rows with it; append a new JSON line by hand for a new row.
Then run `python3 analysis/rebuild.py`.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

FRAGMENTS = Path(__file__).resolve().parent / "fragments"

# Field order used in the fragment files; unknown fields are written last.
ORDER = [
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
    "basis",
    "form",
    "sources",
]


def fmt_num(x) -> str:
    """Write value_si the way the existing rows do (4.5e6, 1.0e-11, 0.0, 9.3)."""
    if x is None:
        return "null"
    x = float(x)
    if x == 0:
        return "0.0"
    if 1e-3 <= abs(x) < 1e4:
        return repr(x)
    exponent = math.floor(math.log10(abs(x)))
    mantissa = f"{x / 10**exponent:.6g}"
    if "." not in mantissa:
        mantissa += ".0"
    return f"{mantissa}e{exponent}"


def dump_row(row: dict) -> str:
    parts = []
    for key in ORDER + [k for k in row if k not in ORDER]:
        if key not in row:
            continue
        if key == "value_si":
            parts.append(f'"{key}": {fmt_num(row[key])}')
        else:
            parts.append(f'"{key}": {json.dumps(row[key], ensure_ascii=False)}')
    return "{" + ", ".join(parts) + "}"


def apply(updates: dict[str, dict], today: str) -> int:
    """Merge `updates[impl_key]` into each matching row. Returns the number of rows changed."""
    seen: set[str] = set()
    for path in sorted(FRAGMENTS.glob("*.jsonl")):
        lines = path.read_text(encoding="utf-8").split("\n")
        changed = False
        for i, line in enumerate(lines):
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            row = json.loads(line)
            key = row["impl_key"]
            if key in updates:
                row.update(updates[key])
                row["updated"] = today
                lines[i] = dump_row(row)
                changed = True
                seen.add(key)
        if changed:
            path.write_text("\n".join(lines), encoding="utf-8")
    missing = sorted(set(updates) - seen)
    if missing:
        raise SystemExit("fragtools: keys not found: " + ", ".join(missing))
    print(f"fragtools: updated {len(seen)} rows")
    return len(seen)


def rows_for(slug: str) -> list[dict]:
    """Return the current rows of one effect, for inspection before editing."""
    out = []
    for path in sorted(FRAGMENTS.glob("*.jsonl")):
        for line in path.read_text(encoding="utf-8").split("\n"):
            if line.strip() and not line.lstrip().startswith("#"):
                row = json.loads(line)
                if row["effect_slug"] == slug:
                    out.append(row)
    return out


def set_csv_row(path, key: str, updates: dict | None = None, append_notes: str | None = None) -> None:
    """Change one row of a hand-kept CSV (first column is the key) and leave every other line as it is.

    `updates` maps column name to new value; `append_notes` is added to the notes cell.
    Only the target line is re-serialised, so the hand quoting of other rows survives.
    """
    import csv
    import io

    path = Path(path)
    lines = path.read_text(encoding="utf-8").split("\n")
    header = next(csv.reader([lines[0]]))
    for i, line in enumerate(lines[1:], start=1):
        if line.startswith(key + ","):
            row = next(csv.reader([line]))
            if len(row) != len(header):
                raise SystemExit(f"{path.name}: row {key} has {len(row)} cells, header has {len(header)}")
            for column, value in (updates or {}).items():
                row[header.index(column)] = value
            if append_notes:
                j = header.index("notes")
                row[j] = (row[j] + " " + append_notes).strip()
            buf = io.StringIO()
            csv.writer(buf, lineterminator="").writerow(row)
            lines[i] = buf.getvalue()
            path.write_text("\n".join(lines), encoding="utf-8")
            return
    raise SystemExit(f"{path.name}: no row with key {key}")
