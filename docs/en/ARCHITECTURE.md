# Architecture and data flow

## Components
```text
Original UCI / IMS distributions
       |
       v
Kaggle notebook (separate experiment pipelines)
  UCI matrices -> 170 statistical features -> validation-selected champions
  IMS timestamps -> 10 vibration features -> per-test early-life IF
       |               |
       v               v
 exported CSVs     trusted joblib models
       |               |
       |         repository models/
       v               v
React/Vite dashboard ----> FastAPI /api/v1/predict/csv
                             |
                  exact feature schema validation
                             |
                  fixed-path model load & inference
                             |
                     JSON predictions/scores
                             |
               UI timeline, class distribution, result rows
```

**Data path:** `frontend/src/services/api.ts` sends `multipart/form-data` with `file` and URL `kind`/`target`. `backend/app/api/routes/predictions.py` enforces `.csv` extension, 10 MiB cap, 2,000-row cap, drops only permitted metadata columns. `app/services/predict.py` requires exactly the stored feature keys and finite numeric values. `app/inference/registry.py` loads only configured artifact paths. Hydraulic uses exported pipeline `.predict` and optional `.predict_proba`; IMS uses stored imputer/scaler, negative IsolationForest score and a test-specific threshold.

## Boundaries
- Browser is a client, not an ML training service. Predictions are synchronous and batch-sized.
- Hydraulic model is **not** raw-sensor to diagnosis end to end; Kaggle feature engineering is an explicit upstream dependency.
- IMS early-life reference model can be compared within its own run; scales and thresholds differ across sessions.
- `GET /api/v1/models` checks `Path.is_file()`, not successful `joblib.load` or ML validation.
- No API authentication, model version signing or production event storage currently verified.

## Failure and integrity concerns
Reject wrong CSV columns/units, NaN/Inf, malformed file or unsupported target. Treat `.joblib` as potentially executable pickle. Preserve cycle ID/order on client batching and align ground-truth label comparisons by ID, not display index alone. Do not reproduce charts from invented values: connect visuals to saved reports or live API outputs only.

See [API](API.md), [security](SECURITY.md), and [reproducibility](REPRODUCIBILITY.md).
