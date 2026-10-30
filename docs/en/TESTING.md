# Testing and quality gates

## Layered test plan
| Layer | Test | Evidence / status |
|---|---|---|
| Repository | links, file tree, path resolution, `.gitignore` | manual review required after docs merge |
| Backend contracts | `/health`, `/models`, invalid `kind`, non-CSV extension | four tests currently implemented; original overlay reported passing |
| Backend schema | wrong column count, omitted/extra features, nonfinite features, malformed CSV | code validates these; broader automated tests still recommended |
| Upload bounds | 10 MiB cap; 2,000-row cap | enforced; 2,205-cycle CSV blocked in local UI as expected |
| Model artifact | fixed-path champion models and matching feature schemas | local dashboard showed 7/7 paths; comprehensive load smoke tests pending |
| Hydraulic integration | 100 engineered rows / cooler | observed success, all predicted class 3; **one domain/model path only** |
| Multi-class evaluation | match `cycle_id` to `profile.txt`, stratify by conditions | pending for dashboard; Kaggle Experiment 02 scores saved separately |
| IMS integration | one real CSV for each `1st/2nd/3rd_test`, correct threshold/score | pending evidence for all three via UI |
| Frontend | `npm run build`, error/loading/empty states, navigation | local page launches; confirm production build separately |
| Security | untrusted joblib rejection, no secrets, malicious CSV, abuse limits | preliminary fixed-path rules; no public deployment approval |

## Manual smoke test
1. Start backend and check `GET /api/v1/health` and `GET /api/v1/models`. Confirm 7 local artifact files only; not an accuracy check.
2. Prepare a **100-row** CSV from `features/hydraulic_cycle_features.csv` (drop `cycle_id` for simplicity). Select Hydraulic → cooler and Run inference. Expect 100 results and a live class distribution, not placeholder chart.
3. Repeat on `valve`, `pump`, `accumulator`; record model name, row count, output and any errors.
4. Prepare ≤2,000-row subsets of `features/ims_1st_test_features.csv`, `ims_2nd_test_features.csv`, `ims_3rd_test_features.csv`, selecting matching IMS model each time. Confirm numeric score, threshold and bool `alarm`.
5. Upload invalid extension, extra column, missing feature, empty file and 2,205-row CSV. Confirm clear failures, not model corruption.
6. Check developer console, HTTP logs, UI responsiveness, keyboard operation, and no private CSV content in logs.

## Completion gates
**Research execution:** datasets accessible, split membership documented, metrics generated and artifact integrity checks pass. **Full-stack smoke:** at least 1 valid live API response for each of seven models, representative CSV subsets, schema rejection and repeatable build. **Production readiness:** NOT achieved; would require authentication, threat assessment, CI, reproducible deploy, source-data approvals and external-domain evaluation.

Avoid using passing smoke tests as evidence for all operating conditions or real industrial reliability.
