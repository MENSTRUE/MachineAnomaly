from __future__ import annotations
import math
import numpy as np
import pandas as pd
from fastapi import HTTPException
from app.inference.registry import candidate_path, ims_path, load_artifact, TARGETS, IMS_TESTS


def validated_frame(rows: list[dict], columns: list[str]) -> pd.DataFrame:
    if not columns or len(columns) != len(set(columns)):
        raise HTTPException(500, "Invalid model feature schema")
    if not rows:
        raise HTTPException(422, "No rows provided")
    required = set(columns)
    for idx, row in enumerate(rows):
        missing = required - set(row)
        extra = set(row) - required
        if missing or extra:
            raise HTTPException(422, {"row": idx, "missing": sorted(missing)[:15], "extra": sorted(extra)[:15], "required_count": len(columns)})
    try:
        frame = pd.DataFrame(rows)[columns].astype(float)
    except (ValueError, TypeError, KeyError) as exc:
        raise HTTPException(422, f"Non-numeric model features: {exc}") from exc
    if not np.isfinite(frame.to_numpy()).all():
        raise HTTPException(422, "Features must be finite numeric values")
    return frame


def hydraulic_batch(rows: list[dict], target: str) -> list[dict]:
    if target not in TARGETS:
        raise HTTPException(422, "Invalid Hydraulic target")
    artifact = load_artifact(str(candidate_path(target)))
    columns = list(artifact["feature_columns"])
    if len(columns) != 170:
        raise HTTPException(500, f"Expected 170 Hydraulic features, got {len(columns)}")
    frame = validated_frame(rows, columns)
    preds = artifact["pipeline"].predict(frame)
    probs = None
    if hasattr(artifact["pipeline"], "predict_proba"):
        probs = artifact["pipeline"].predict_proba(frame)
    results = []
    for i, pred in enumerate(preds):
        result = {"row_index": i, "target": target, "predicted_class": int(pred), "experiment": "02", "interpretation": "Hydraulic condition class; not a failure probability"}
        if probs is not None:
            result["confidence_proxy"] = float(max(probs[i]))
        results.append(result)
    return results


def ims_batch(rows: list[dict], test: str) -> list[dict]:
    if test not in IMS_TESTS:
        raise HTTPException(422, "Invalid IMS test")
    artifact = load_artifact(str(ims_path(test)))
    frame = validated_frame(rows, list(artifact["feature_columns"]))
    inp = artifact["scaler"].transform(artifact["imputer"].transform(frame))
    scores = -artifact["model"].score_samples(inp)
    threshold = float(artifact["threshold"])
    return [{"row_index": i, "test": test, "anomaly_score": float(s), "threshold": threshold, "alarm": bool(s > threshold), "interpretation": "Unsupervised deviation from early-life reference; NOT confirmed bearing failure"} for i, s in enumerate(scores)]
