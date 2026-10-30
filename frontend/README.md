# MachineAnomaly Frontend

React + Vite + TypeScript dashboard. The interface calls FastAPI and displays only real model responses, never hardcoded predictions.

```powershell
cd frontend
npm install
npm run dev
```

Visit http://localhost:5173. Start backend on port 8000 first. Upload `features/hydraulic_cycle_features.csv` for Hydraulic or `features/ims_1st_test_features.csv` for IMS; choose matching domain and model. Upload maximum 2,000 rows and 10 MB per request. Do not upload raw vibration timestamp text or raw Hydraulic sensor matrices; the exported models require engineered features.

Build: `npm run build`. Vite proxies `/api` to localhost:8000 in development. Configure allowed CORS origins on the backend for non-local deployments.
