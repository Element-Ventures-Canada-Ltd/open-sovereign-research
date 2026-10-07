#!/usr/bin/env python3
# Handling: Unclassified — public
"""Validate eval-task files. Usage: python3 tools/validate_evals.py [task.yaml ...] (defaults to evals/**).
Checks required fields, track vocabulary, Seam cell ids, http(s) context, 3–10 criteria with unique ids,
criterion type and weight, and no monetary figures. Exits non-zero on any error. Requires PyYAML."""
import datetime
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TRACKS = {"seam", "chokepoint", "launch", "space-economy", "workforce"}
TYPES = {"must", "should", "must_not"}
URL = re.compile(r"^https?://\S+$")
ID = re.compile(r"^[a-z-]+-\d{3}$")
MONEY = re.compile(r"(\$\s?\d|\b(CAD|USD|EUR|GBP|C\$|US\$)\s?\d|\d[\d,.]*\s?(CAD|USD|EUR|GBP|million|billion)\b)", re.I)


def main(argv):
    rubric = yaml.safe_load((ROOT / "seam" / "sovereign-seam.yaml").read_text(encoding="utf-8"))
    cells = {f"{l['id']}-{c['id']}" for l in rubric["layers"] for c in rubric["capabilities"]["items"]}
    targets = [Path(a) for a in argv[1:]] or sorted(
        p for p in (ROOT / "evals").rglob("*.yaml") if p.name != "TASK_TEMPLATE.yaml")
    errors, ids = [], {}
    for t in targets:
        text = t.read_text(encoding="utf-8")
        for n, line in enumerate(text.splitlines(), 1):
            if not line.lstrip().startswith("#") and MONEY.search(line):
                errors.append(f"{t}:{n}: monetary figure")
        d = yaml.safe_load(text) or {}
        task, crit = d.get("task") or {}, d.get("criteria") or []
        if not ID.match(str(task.get("id", ""))):
            errors.append(f"{t}: task.id must look like <track>-<nnn>")
        elif task["id"] in ids:
            errors.append(f"{t}: duplicate task id (also in {ids[task['id']]})")
        ids[task.get("id")] = t
        if task.get("track") not in TRACKS:
            errors.append(f"{t}: track must be one of {sorted(TRACKS)}")
        for c in task.get("cells") or []:
            if c not in cells:
                errors.append(f"{t}: unknown cell {c}")
        for k in ("prompt", "contributor"):
            if not str(task.get(k) or "").strip():
                errors.append(f"{t}: task.{k} missing")
        if not task.get("context") or not all(isinstance(u, str) and URL.match(u) for u in task["context"]):
            errors.append(f"{t}: task.context needs at least one http(s) source")
        if not isinstance(task.get("as_of"), datetime.date):
            errors.append(f"{t}: task.as_of must be YYYY-MM-DD")
        if not isinstance(task.get("synthetic"), bool):
            errors.append(f"{t}: task.synthetic must be true or false")
        if not 3 <= len(crit) <= 10:
            errors.append(f"{t}: 3–10 criteria required")
        cids = [c.get("id") for c in crit]
        if len(set(cids)) != len(cids):
            errors.append(f"{t}: criterion ids must be unique")
        for c in crit:
            if c.get("type") not in TYPES:
                errors.append(f"{t}: criterion {c.get('id')} type must be one of {sorted(TYPES)}")
            if c.get("weight") not in (1, 2, 3):
                errors.append(f"{t}: criterion {c.get('id')} weight must be 1, 2 or 3")
            if not str(c.get("text") or "").strip():
                errors.append(f"{t}: criterion {c.get('id')} text missing")
    for e in errors:
        print(f"ERROR {e}")
    print("OK" if not errors else "FAIL", f"({len(targets)} task file(s))")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
