# Frontend AGENTS — dashboard rules

Read root `AGENTS.md` before changing UI. Maintain React + Vite + TypeScript conventions. API client: `src/services/api.ts`; backend contract: `docs/en/API.md`.

- Never render invented scores, fabricated maintenance alerts or hardcoded model predictions as real output. Empty/loading/error states must be distinguishable.
- Display Hydraulic condition values as integer *condition classes*, not percent health/failure. Do not label `confidence_proxy` a reliable failure probability.
- Display IMS alarm score, threshold and anomaly trend as **unlabeled deviation from early-life reference**, not diagnosis or RUL.
- Preserve exact `kind`, `target`, FormData `file` and `/api/v1/predict/csv` request shape. Handle server 413 (size/row cap), 415 (file type), 422 (schema), 500 (artifact/load) clearly.
- Current frontend/API processes one request of ≤2,000 rows and ≤10 MiB; user-facing auto batching is future work. Do not claim unlimited CSV support.
- Keep keyboard-accessible controls, readable contrast, proper labels, useful loading and error messages, responsive tables and chart alternatives. Charts must use actual response data only.
- Run `npm run build`, then smoke test Hydraulic/IMS when trusted model artifacts and example files are available. If not run, say so explicitly.
- Do not add third-party libraries or reorganize `src/` without reason. Update both locale documents and tests with behavioral changes.
- Avoid shipping API keys and uploading users' CSVs to any destination other than the configured backend. No analytics collecting raw sensor payloads.
