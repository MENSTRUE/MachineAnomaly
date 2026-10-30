# API reference — actual FastAPI routes

Base URL local: `http://localhost:8000/api/v1` (Swagger `http://localhost:8000/docs`). For frontend development, Vite forwards relative `/api` requests to local backend.

## Endpoints
| Method | Path | Request | Response |
|---|---|---|---|
| GET | `/health` | none | `{"status":"ok","service":"MachineAnomaly","demo":false}` |
| GET | `/models` | none | keys `hydraulic`, `ims`, `model_directory`; boolean path existence by target |
| POST | `/predict/csv?kind=hydraulic&target=cooler` | multipart file field `file`, `.csv` 170 feature columns + allowed metadata | `{kind,target,total,results:[...]}` |
| POST | `/predict/csv?kind=ims&target=1st_test` | multipart CSV exact 10 named model features + allowed metadata | `{kind,target,total,results:[...]}` |
| POST | `/predict/hydraulic/{target}` | JSON `features` object | `{results:[{row_index,target,predicted_class,experiment,interpretation,confidence_proxy?}]}` |
| POST | `/predict/ims` | JSON `test` and `features` object | `{results:[{row_index,test,anomaly_score,threshold,alarm,interpretation}]}` |

**Valid hydraulic targets:** `cooler`, `valve`, `pump`, `accumulator`. **Valid IMS tests:** `1st_test`, `2nd_test`, `3rd_test`.

## Input constraints
- CSV max **10 MiB** (`MAX_UPLOAD_BYTES=10*1024*1024`); max **2,000 rows**. The source UCI file has 2,205 rows, so use a sliced test file or multiple requests.
- Metadata allowlist ignored by CSV upload: `cycle_id`, `Unnamed: 0`, `test`, `sequence_index`, `snapshot`, `n_channels`, `anomaly_score`, `reference_threshold`, `alarm`, `reference_period`, `smoothed_score`. Unknown columns rejected instead of silently removed.
- Numeric, finite feature values only; exact names and target-specific ordering derived from artifact `feature_columns`. Training artifact schema is authoritative; do not invent aliases or reorder columns manually.
- The backend infers from exported **engineered** features, not UCI PS/FS raw matrices or IMS timestamp vibration files.

## Example request (PowerShell)
```powershell
# Existing 100-row engineered example, created from local feature export
curl.exe -X POST "http://localhost:8000/api/v1/predict/csv?kind=hydraulic&target=cooler" `
    -F "file=@assets/examples/hydraulic_test_100.csv"

curl.exe http://localhost:8000/api/v1/models
```

## Representative response shapes (schema illustrations, NOT observed inference values)
```json
{"kind":"hydraulic","target":"cooler","total":1,"results":[{"row_index":0,"target":"cooler","predicted_class":3,"experiment":"02","interpretation":"Hydraulic condition class; not a failure probability","confidence_proxy":0.83}]}
```
The example JSON above is **syntactic illustration**; `confidence_proxy=0.83` is NOT a measured model result. For IMS, the `results` items contain `anomaly_score`, `threshold`, `alarm`, and cautionary interpretation. No failure events are promised.

## Errors and security
- `413`: uploaded bytes >10 MiB or >2,000 data rows.
- `415`: filename not `.csv`.
- `422`: invalid `kind`/`target`, empty/invalid CSV, missing/extra columns, nonnumeric/nonfinite inputs.
- `500` / other server failures: model missing/incompatible, schema or internal errors. Do not treat as passing inference.
- Model registry file presence does not invoke `joblib.load`; only trusted Kaggle artifacts should be stored in the model directory.

For production add authentication, rate limiting, audit controls, upload hardening, secure TLS ingress, and model provenance. See [SECURITY.md](SECURITY.md).
