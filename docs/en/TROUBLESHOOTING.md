# Troubleshooting — verified common problems

## 413: Maximum 2000 rows per request
`hydraulic_cycle_features.csv` has **2,205 rows**, exceeding `MAX_ROWS=2000`. Create an engineered 100-row sample instead of changing the model schema:
```powershell
@'
import pandas as pd
from pathlib import Path
root = Path(r'D:\porto\100 day\day 25\MachineAnomaly')
src = root/'features'/'hydraulic_cycle_features.csv'
dst = root/'assets'/'examples'/'hydraulic_test_100.csv'
df = pd.read_csv(src).drop(columns=['cycle_id','Unnamed: 0'], errors='ignore')
assert df.shape[1] == 170, f'Expected 170 features, got {df.shape[1]}'
dst.parent.mkdir(parents=True, exist_ok=True)
df.head(100).to_csv(dst,index=False)
print(dst)
'@ | python -
```
This is a connectivity test, not balanced statistical validation. For full-cycle inference split into batches and preserve original row IDs.

## 422: Unexpected / missing feature names
Use the Kaggle-exported engineered CSV matching the selected model. UCI: 170 numeric sensor statistics. IMS: 10 named statistical vibration features. `cycle_id` and known metadata fields are ignored by the CSV endpoint; unknown extra columns are rejected.

## 415: File extension not accepted
Use `.csv` (not `.txt`, `.parquet`, `.zip` or raw sensor samples). Verify the file actually contains comma-delimited numeric columns with the expected headers.

## 500 / model load exception
Check `models/experiment_02_hydraulic/hydraulic_<target>_champion.joblib` and `models/ims_<test>_iforest.joblib`. `GET /api/v1/models` checks file presence only. Review backend logs for incompatible scikit-learn/joblib versions; never "repair" errors by loading unknown binaries.

## API ONLINE but no predictions
A successful `/health` indicates server availability only. Confirm frontend uploaded a CSV, called `/api/v1/predict/csv`, backend returned 200 and result records were rendered. Inspect browser developer tools Network tab, backend terminal and `frontend/src/services/api.ts`.

## Entire 100-row cooler result is class 3
The **first 100 rows** of the original UCI profile belong to cooler condition class 3. This is compatible with a functioning inference path but does not demonstrate accuracy across cooler classes 20/100. For evaluation, compare predictions against exact cycle-ID labels on a class-diverse sample.

## Frontend build / backend startup
Run `npm install`, `npm run build` inside `frontend/`; if Python import `app` fails, run `python -m uvicorn app.main:app` from **backend** directory. For Vite proxy issues, inspect dev server configuration and backend at port 8000.

## Empty plots or documents missing
Plots must be real Kaggle-generated PNGs copied into `assets/plots/`; docs link to them. Markdown references alone do not generate images. Re-extract validated Kaggle artifacts if needed; don't invent screenshots.

## Git accidentally tracks ZIP/data/dependencies
Update `.gitignore`, review `git status`, then untrack specific files with `git rm --cached <path>`. Public Git history may retain already pushed secrets; rotate any compromised credentials and assess history cleanup separately.
