from __future__ import annotations
from io import BytesIO
import pandas as pd
from fastapi import APIRouter, HTTPException, UploadFile, File, Query
from app.core.config import MAX_ROWS, MAX_UPLOAD_BYTES
from app.inference.registry import TARGETS, IMS_TESTS
from app.schemas.predictions import HydraulicRequest, IMSRequest
from app.services.predict import hydraulic_batch, ims_batch
router = APIRouter()

@router.post("/predict/hydraulic/{target}")
def hydraulic(target: str, request: HydraulicRequest):
    return {"results": hydraulic_batch([request.features], target)}

@router.post("/predict/ims")
def ims(request: IMSRequest):
    return {"results": ims_batch([request.features], request.test)}

@router.post("/predict/csv")
async def csv_predict(file: UploadFile = File(...), kind: str = Query(..., pattern="^(hydraulic|ims)$"), target: str = Query(...)):
    if kind == "hydraulic" and target not in TARGETS:
        raise HTTPException(422, f"target must be one of {TARGETS}")
    if kind == "ims" and target not in IMS_TESTS:
        raise HTTPException(422, f"target must be one of {IMS_TESTS}")
    if not (file.filename or "").lower().endswith(".csv"):
        raise HTTPException(415, "Upload a .csv file")
    raw = await file.read(MAX_UPLOAD_BYTES + 1)
    if len(raw) > MAX_UPLOAD_BYTES:
        raise HTTPException(413, "CSV exceeds 10 MB limit")
    try:
        df = pd.read_csv(BytesIO(raw), nrows=MAX_ROWS + 1)
    except Exception as exc:
        raise HTTPException(422, f"Invalid CSV: {exc}") from exc
    if df.empty:
        raise HTTPException(422, "CSV is empty")
    if len(df) > MAX_ROWS:
        raise HTTPException(413, f"Maximum {MAX_ROWS} rows per request")
    # Notebook exports include cycle_id, test, sequence_index etc. Ignore explicitly known metadata ONLY.
    metadata = {"cycle_id", "Unnamed: 0", "test", "sequence_index", "snapshot", "n_channels", "anomaly_score", "reference_threshold", "alarm", "reference_period", "smoothed_score"}
    feature_rows = df.drop(columns=[c for c in df.columns if c in metadata]).to_dict(orient="records")
    results = hydraulic_batch(feature_rows, target) if kind == "hydraulic" else ims_batch(feature_rows, target)
    return {"kind": kind, "target": target, "total": len(results), "results": results}
