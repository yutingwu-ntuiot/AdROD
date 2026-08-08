#!/usr/bin/env python3
"""Verify the scope and required metadata of the public AdROD companion."""

from __future__ import annotations

import csv
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    "NOTICE",
    "LICENSE",
    "configs/paper_hyperparameters.yaml",
    "configs/evaluation_protocols.yaml",
    "results/reported_results.csv",
    "patches/Person/Hip/patch.png",
    "patches/Person/Hip/cfg.json",
    "evaluation_data/consecutive_data/road_noisy/0001.jpg",
    "evaluation_data/nonconsecutive_data/coco_person",
    "DATASET_LICENSES.md",
    "demo/images/stopsign_yolo.png",
    "demo/images/stopsign_adrod.png",
)
FORBIDDEN_SUFFIXES = {".pt", ".pth", ".onnx", ".engine"}
FORBIDDEN_FILENAMES = {
    "AdROD.py",
    "eval_AdROD_YOLO.py",
    "eval_NOHIDE_FRCNN.py",
    "train_hypernet_yolov5s.py",
    "val_hypernet.py",
    "val_mAP.py",
}


def fail(message: str) -> None:
    print(f"Release check failed: {message}", file=sys.stderr)
    raise SystemExit(1)


for relative_path in REQUIRED:
    if not (ROOT / relative_path).exists():
        fail(f"missing required file: {relative_path}")

for path in ROOT.rglob("*"):
    if not path.is_file():
        continue
    if path.suffix.lower() in FORBIDDEN_SUFFIXES:
        fail(f"model artifact must not be public: {path.relative_to(ROOT)}")
    if path.name in FORBIDDEN_FILENAMES:
        fail(f"executable implementation must not be public: {path.relative_to(ROOT)}")

with (ROOT / "results/reported_results.csv").open(newline="", encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))

if len(rows) != 4 or any(not row.get("value") for row in rows):
    fail("reported_results.csv must contain four complete result rows")

evaluation_files = sum(1 for path in (ROOT / "evaluation_data").rglob("*") if path.is_file())
if evaluation_files != 1400:
    fail(f"expected 1400 released evaluation files, found {evaluation_files}")

print("Public AdROD companion release check passed.")
