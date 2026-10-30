# Frontend — Industrial Condition Intelligence

React 18 + Vite 6 + TypeScript dashboard backed by FastAPI. Source of truth for UI behavior is `src/`; no hardcoded prediction list or synthetic metric histories should be passed off as model results.

## Develop
```powershell
cd frontend
npm install
npm run dev
# independent terminal: start backend on :8000
npm run build
npm run preview
```

Visit http://localhost:5173. The Vite development proxy serves `/api/v1` against local backend port 8000. For production, configure a reverse proxy or API deployment explicitly; the Vite dev proxy does not ship automatically.

## Existing user flow
1. Overview shows backend status and model artifact availability; **7/7** means files exist, not 7 models statistically validated in the app.
2. Select `Hydraulic` and one of `cooler/valve/pump/accumulator`, or `IMS Bearings` and one of `1st_test/2nd_test/3rd_test`.
3. Upload feature CSV exported from the notebook. No raw sensor matrices or raw IMS timestamp files.
4. Upload must contain **≤2,000 rows** and **≤10 MiB**. Use a 100-row subset for smoke tests; the 2,205-row Hydraulic feature file is rejected as a single request.
5. View actual backend predictions, class distribution, anomaly timeline and the first 100 result rows. Treat class labels as **condition codes**; tree confidence as a proxy only; IMS alarms as unlabeled change indications.

## Tested and untested
A local screenshot demonstrates a successful **100-row Hydraulic cooler inference** with all class-3 predictions. This establishes one integration path; it does **not** prove accuracy, calibrated confidence or all-target support. Additional tests are required for balanced class sampling and all IMS model choices.

## UX, privacy, security
Avoid persisting uploaded sensor data to browser storage, logging full rows or placing secrets in Vite `VITE_` variables. Surface clear 413/415/422 errors; do not trim CSV without consent. If introducing automatic batching, preserve row ordering, provide per-chunk status and partial-failure handling, and document maximum run size.

See [API](../docs/en/API.md), [architecture](../docs/en/ARCHITECTURE.md), [testing](../docs/en/TESTING.md) and [troubleshooting](../docs/en/TROUBLESHOOTING.md).
