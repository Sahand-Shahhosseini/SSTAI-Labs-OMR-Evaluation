#!/usr/bin/env python3
import json,pathlib
R=pathlib.Path(__file__).resolve().parent;M=json.loads((R/"FOLDER_DESCRIPTIONS.json").read_text());B={x["path"]:x for x in M["directories"]}
def e(s):
 a=s.lower().split("/");z=s.lower();return any(x in {"__pycache__","node_modules",".venv","venv","site-packages","dist","build","obj","bin",".cache",".pytest_cache",".mypy_cache",".tox","htmlcov"} for x in a) or z.startswith("vendor/") or "/vendor/" in z or z.endswith(".egg-info")
D=[p.relative_to(R).as_posix() for p in R.rglob("*") if p.is_dir() and p.relative_to(R).as_posix()!=".git" and not p.relative_to(R).as_posix().startswith(".git/")];F=[d for d in D if d not in B or not str(B[d].get("description","")).strip() or (e(d) and B[d].get("description_mode")!="MANIFEST_EXEMPT") or (not e(d) and not (R/d/"README.md").exists())];print("PASS_BOUNDED" if not F else "FAIL_FOLDER_DESCRIPTIONS",len(D),F);raise SystemExit(1 if F else 0)
