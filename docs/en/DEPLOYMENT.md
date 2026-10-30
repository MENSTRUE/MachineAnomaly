# Deployment and operations runbook

## Current supported mode: local research development
**Not a validated production deployment.** Environment: Windows PowerShell, Python compatible with the exported sklearn/joblib serialization, Node/npm and trusted local models.

```powershell
# Terminal A
cd "D:\porto\100 day\day 25\MachineAnomaly\backend"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
python -m uvicorn app.main:app --reload --port 8000

# Terminal B
cd "D:\porto\100 day\day 25\MachineAnomaly\frontend"
npm install
npm run build
npm run dev
```

Check http://localhost:8000/docs, http://localhost:8000/api/v1/models and http://localhost:5173. Default model root is repository `models/`; optional `MACHINEANOMALY_MODEL_DIR` override. `CORS_ORIGINS` is comma-separated and should be restricted to actual frontend origins.

## Future preproduction checklist
- Pin Python + scikit-learn versions compatible with joblib artifacts; pin Node dependencies and maintain verified lockfiles.
- Publish only reviewed built frontend; configure reverse proxy `/api`, HTTPS/TLS, health/readiness probes and bounded server workers. Vite dev proxy is not production routing.
- Authenticate and authorize every dataset upload and model inference call; add throttling and maximum payload/row safeguards. Audit CORS and CSRF assumptions.
- Sign and hash allowlisted model artifacts; do not accept arbitrary model uploads or remote joblib paths. Treat model changes as versioned deployments.
- Monitor latency, error rate, input schema drift, class distribution, request sizes, timeouts and incident escalation, without raw sensitive data leakage.
- Validate deployment against actual target machine sensor regimes; establish rollback, backup, observability, data retention and license sign-off.
- Document a human-in-the-loop process: never automate plant safety actions from prototype scores.

## Acceptance
A working localhost demo is a valid portfolio milestone. It does not authorize claims of live production monitoring, safety certification, failure prediction or confirmed fault labels. See [security](SECURITY.md), [testing](TESTING.md), [research](RESEARCH.md).
