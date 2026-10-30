# Backend — FastAPI model inference

**Source:** `app/main.py`, `app/api/routes/`, `app/services/predict.py`, `app/inference/registry.py`, `app/core/config.py`. Supports exported, trusted Kaggle model artifacts only. No generated or synthetic inference.

## Quick start (PowerShell)
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
python -m uvicorn app.main:app --reload --port 8000
```

Swagger at http://localhost:8000/docs. Health `/api/v1/health`; model path registry `/api/v1/models`.

## Routes
| Method | Path | Contract |
|---|---|---|
| GET | `/api/v1/health` | status `ok` (does not execute a model) |
| GET | `/api/v1/models` | available artifact paths for four Hydraulic and three IMS models |
| POST | `/api/v1/predict/csv?kind=hydraulic&target=cooler` | CSV upload, Hydraulic 170 numeric engineered features |
| POST | `/api/v1/predict/csv?kind=ims&target=1st_test` | CSV upload, 10 IMS features matching per-test model |
| POST | `/api/v1/predict/hydraulic/{target}` | JSON features object for one row |
| POST | `/api/v1/predict/ims` | JSON features and `test` for one IMS row |

Targets: Hydraulic `cooler`, `valve`, `pump`, `accumulator`; IMS `1st_test`, `2nd_test`, `3rd_test`. CSV: at most 10 MiB / 2,000 rows; metadata columns are removed by explicit allowlist only, schema is matched against stored `feature_columns` in each `.joblib`. A file with 2,205 cycles is not accepted in one request; split batches.

## Inference paths
- Hydraulic: `../models/experiment_02_hydraulic/hydraulic_<target>_champion.joblib` → preprocessing pipeline → class integer and optional `confidence_proxy` (uncalibrated).
- IMS: `../models/ims_<test>_iforest.joblib` → imputer + scaler + IsolationForest → score and per-test alarm threshold. Does **not** establish failure truth.

Configure `MACHINEANOMALY_MODEL_DIR` to change the model root. Configure `CORS_ORIGINS` as comma-separated allowed origins; default local `http://localhost:5173,http://127.0.0.1:5173`. Reload backend on configuration changes. Model registry's file existence is not equivalent to prediction readiness.

## Validation and negative cases
- `pytest -q` checks health/registry and rejection of invalid `kind`, unsupported extension. **These are limited contract tests**, not a full ML regression suite.
- Add tests for exact columns, missing features, nonfinite values, upload limits, rejected unauthorized artifact paths and representative prediction fixtures.
- Verify correct sample feature CSV (`features/hydraulic_cycle_features.csv` subset 100 rows); original file has 2,205 rows.

## Deployment / security boundaries
Only load self-generated **trusted** joblib files; pickle deserialization is unsafe for untrusted artifacts. Do not publish this development API without authentication, reverse proxy and upload scanning limits, rate limiting, TLS, observability, deployment CORS policy and tested environment compatibility. Package `scikit-learn` version must remain compatible with serialized models. See [API docs](../docs/en/API.md), [testing](../docs/en/TESTING.md), [security](../docs/en/SECURITY.md).
