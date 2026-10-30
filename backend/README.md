# MachineAnomaly Backend

FastAPI inference service for **real** exported Kaggle models. Predictions are never synthetic. Missing model artifacts cause an explicit error.

## Quick start (PowerShell)

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Open http://localhost:8000/docs. Put trusted Kaggle model outputs in repo `models/` according to the existing structure. The API uses `MACHINEANOMALY_MODEL_DIR` if set.

Hydraulic `/api/v1/predict/csv?kind=hydraulic&target=cooler` expects the exported `hydraulic_cycle_features.csv` (170 columns + optional `cycle_id`). IMS `/api/v1/predict/csv?kind=ims&target=1st_test` expects `ims_1st_test_features.csv` (10 features plus metadata). Each model accepts only its own feature schema. The confidence proxy is the tree ensemble vote/probability, not a calibrated real-world reliability estimate.

Run `pytest -q` in `backend/`. Model existence is visible at `/api/v1/models`.

**Security:** `joblib.load` deserializes pickle and can execute untrusted code. Load only models produced by your own Kaggle notebook. CSV uploads are capped at 10 MB and 2,000 rows. This is a local research prototype; add authentication, rate limits and hosting controls before public deployment.
