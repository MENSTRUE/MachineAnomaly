# Backend AGENTS — service contracts

Read root `AGENTS.md` first. Maintain FastAPI endpoint compatibility under `/api/v1`; source-of-truth files: `app/main.py`, `api/routes/predictions.py`, `core/config.py`, `inference/registry.py`, `services/predict.py`.

- Preserve four target-specific Hydraulic models and three independent IMS session models. Do not switch to Experiment 01 models without an explicit versioned endpoint/model migration.
- Validate feature keys exactly against stored model schema. Require finite numeric inputs. Remove only explicitly permitted metadata fields; never silently drop arbitrary numeric columns.
- Keep `MAX_ROWS=2000`, `MAX_UPLOAD_BYTES=10*1024*1024` unless spec, docs and tests are updated together. Return appropriate 413, 415 or 422; never false HTTP 200 on malformed input.
- Maintain fixed artifact paths; no end-user-controlled joblib file path or deserialization of uploads. `lru_cache` must not hide model version replacement or deployment race (restart to reload).
- Hydraulic `confidence_proxy`: uncalibrated ensemble output, not verified probability of equipment failure. IMS `alarm`: change-from-reference, not failure event.
- Backend success requires `python -m pytest -q` and at least one actual prediction smoke test with trusted artifacts; if only contract tests ran, state that limitation.
- Add regression tests for malformed CSV, no rows, extra/missing columns, NaNs, large inputs, and correct model routing. Mock tests may validate routes but cannot substantiate ML metrics.
- Avoid logging uploaded industrial data, credentials, or full payloads. Add auth, rate limiting and audit controls before public deployment.
- No modifying root research metrics/notebook to make an API test pass. Document any new shape, contract or error in `docs/en/API.md` and `docs/id/API.md`.
