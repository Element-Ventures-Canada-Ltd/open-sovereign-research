#!/usr/bin/env python3
# Handling: Unclassified — public
"""Validate Sovereign Seam reading files against seam/sovereign-seam.yaml.

Usage: python3 tools/validate_readings.py [reading.yaml ...]   (defaults to every file under seam/readings/)
Checks: known cell ids, posture and intensity vocabulary, evidence grade, at least one http(s) source,
non-empty rationale, one reading per cell per file, ISO date, and no monetary figures anywhere in a reading.
Exits non-zero on any error. Requires PyYAML.
"""
import datetime
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
URL = re.compile(r"^https?://\S+$")
MONEY = re.compile(r"(\$\s?\d|\b(CAD|USD|EUR|GBP|C\$|US\$)\s?\d|\d[\d,.]*\s?(CAD|USD|EUR|GBP|[MBK]\$|million|billion)\b)", re.I)


def main(argv):
    rubric = yaml.safe_load((ROOT / "seam" / "sovereign-seam.yaml").read_text(encoding="utf-8"))
    cells = {f"{l['id']}-{c['id']}" for l in rubric["layers"] for c in rubric["capabilities"]["items"]}
    postures = set(rubric["postures"])
    intensity = set(rubric["intensity"])
    grades = set(rubric["evidence_grades"])
    assert len(cells) == rubric["rubric"]["cells"], "rubric does not form the declared number of cells"

    targets = [Path(a) for a in argv[1:]] or sorted(
        p for p in (ROOT / "seam" / "readings").rglob("*.yaml") if p.name != "TEMPLATE.yaml")
    errors = []
    for t in targets:
        text = t.read_text(encoding="utf-8")
        for n, line in enumerate(text.splitlines(), 1):
            if not line.lstrip().startswith("#") and MONEY.search(line):
                errors.append(f"{t}:{n}: monetary figure — cells never carry dollar values")
        data = yaml.safe_load(text) or {}
        meta = data.get("reading_set") or {}
        for k in ("lens", "contributor", "as_of"):
            if not meta.get(k):
                errors.append(f"{t}: reading_set.{k} missing")
        if meta.get("as_of") and not isinstance(meta["as_of"], datetime.date):
            errors.append(f"{t}: reading_set.as_of must be YYYY-MM-DD")
        if not isinstance(meta.get("synthetic"), bool):
            errors.append(f"{t}: reading_set.synthetic must be true or false")
        seen = set()
        for i, r in enumerate(data.get("readings") or []):
            label = f"{t}: readings[{i}] {r.get('cell')}"
            if r.get("cell") not in cells:
                errors.append(f"{label}: unknown cell id")
            if r.get("cell") in seen:
                errors.append(f"{label}: cell read twice in one file")
            seen.add(r.get("cell"))
            if r.get("posture") not in postures:
                errors.append(f"{label}: posture must be one of {sorted(postures)}")
            if r.get("posture") != "UNREAD":
                if r.get("intensity") not in intensity:
                    errors.append(f"{label}: intensity must be one of {sorted(intensity)}")
                if not str(r.get("rationale") or "").strip():
                    errors.append(f"{label}: rationale missing")
                srcs = r.get("sources") or []
                if not srcs or not all(isinstance(s, str) and URL.match(s) for s in srcs):
                    errors.append(f"{label}: at least one http(s) source required")
            if r.get("evidence_grade") not in grades:
                errors.append(f"{label}: evidence_grade must be one of {sorted(grades)}")
        if not data.get("readings"):
            errors.append(f"{t}: no readings")
    for e in errors:
        print(f"ERROR {e}")
    print("OK" if not errors else "FAIL", f"({len(targets)} file(s), {len(cells)} cells)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
