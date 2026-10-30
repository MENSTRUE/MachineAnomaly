# MachineAnomaly documentation hub

Documentation is maintained in **Bahasa Indonesia** and **English**. Technical and scientific claims must remain aligned between translations and the actual notebook/CSV/JSON evidence.

| Topic | Bahasa Indonesia | English |
|---|---|---|
| Getting started / project status | [id/README.md](id/README.md) | [en/README.md](en/README.md) |
| Research, datasets, methods, metrics, limitations | [id/RESEARCH.md](id/RESEARCH.md) | [en/RESEARCH.md](en/RESEARCH.md) |
| System architecture, model/data flows | [id/ARCHITECTURE.md](id/ARCHITECTURE.md) | [en/ARCHITECTURE.md](en/ARCHITECTURE.md) |
| Endpoint contract, CSV schemas | [id/API.md](id/API.md) | [en/API.md](en/API.md) |
| Reproducibility & artifact audit | [id/REPRODUCIBILITY.md](id/REPRODUCIBILITY.md) | [en/REPRODUCIBILITY.md](en/REPRODUCIBILITY.md) |
| Tests and quality gates | [id/TESTING.md](id/TESTING.md) | [en/TESTING.md](en/TESTING.md) |
| Local deployment & security | [id/DEPLOYMENT.md](id/DEPLOYMENT.md), [id/SECURITY.md](id/SECURITY.md) | [en/DEPLOYMENT.md](en/DEPLOYMENT.md), [en/SECURITY.md](en/SECURITY.md) |
| Troubleshooting and FAQ | [id/TROUBLESHOOTING.md](id/TROUBLESHOOTING.md), [id/FAQ.md](id/FAQ.md) | [en/TROUBLESHOOTING.md](en/TROUBLESHOOTING.md), [en/FAQ.md](en/FAQ.md) |
| Roadmap, acceptance criteria | [id/ROADMAP.md](id/ROADMAP.md) | [en/ROADMAP.md](en/ROADMAP.md) |

## Source-of-truth hierarchy
1. Runtime implementation in `backend/app`, `frontend/src`.
2. Executed notebook and original experiment source (`notebooks/`).
3. Reproducible metrics, input schema and split ledger (`reports/`, `features/`).
4. Genuine Kaggle plots (`assets/plots/`) and original UI screenshots (`assets/screenshots/`).
5. This documentation, which describes but **never overrides** code or measured research outputs.

If output files are missing from a clone, consult the notebook/Kaggle artifact export; do not invent them or copy source dataset files to GitHub.
