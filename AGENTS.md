# AGENTS.md — MachineAnomaly repository instructions

## Purpose and operating contract
This file governs human contributors and coding agents operating on the repository. Read **README.md**, **docs/en/RESEARCH.md**, **docs/en/ARCHITECTURE.md**, and the nested `backend/AGENTS.md` / `frontend/AGENTS.md` before code changes. Project goal: an evidence-based research dashboard for UCI Hydraulic **condition diagnosis** and NASA/IMS **unlabeled anomaly indication**, not production fault prediction.

### Non-negotiable source of truth
1. **Code** determines implemented behavior (`backend/app`, `frontend/src`). **Notebook and saved CSV/JSON metrics** determine research findings (`notebooks/`, `reports/`). Do not substitute screenshots, README claims, or hand-written numbers for actual outputs.
2. Preserve all original notebook sections **00–13**, their cell ordering and measured outputs. Any revised experiment must be **appended** with sequential experiment number, explicit motivation, split specification, rationale, result artifacts, and caveats. Do not silently modify Experiment 01.
3. Distinguish **Experiment 01** chronological holdout and **Experiment 02** stratified validation selection. No direct uplift calculation as though identical tests. Different test partitions preclude like-for-like comparison.
4. IMS sessions have **no per-snapshot fault ground truth**. No fabricated anomaly accuracy, RUL, fault timestamps, lead time, cost savings, or plant safety claim.
5. Use original source provenance; no unauthorized raw dataset redistribution. Never conflate UCI Hydraulic and IMS into one training table or common scoring benchmark.
6. Keep **current repository structure** (including existing `features/`); do not add arbitrary root directories, new `datasets/`, renamed folders, or replace users' existing files without inspecting diffs.
7. Never produce fake model outputs, fabricated plots, success screenshots, forged test logs, invented downloaded data, or placeholder records presented as empirical evidence.

## Repository map
- `notebooks/`: Kaggle final `.ipynb`, experiment methodology and actual notebook outputs.
- `features/`: existing exported **engineered** input CSVs. Do not confuse with `dataset/` raw inputs.
- `models/`: trusted `.joblib`, champion subfolder `experiment_02_hydraulic/`. Treat binaries as untrusted unless provenance verified.
- `reports/`: split audits, holdout metrics, predictions, provenance, model-selection ledger, and IMS trend summaries.
- `assets/plots/`: real generated research charts; `assets/screenshots/`: user-tested UI captures; `assets/diagrams/`: architectural diagrams only if actually created.
- `backend/app`: API, model registry and prediction schema; `backend/tests`: behavior and failure tests.
- `frontend/src`: dashboard and request client; `docs/id`, `docs/en`: maintained bilingual technical documentation.

## Change workflow / review gate
1. Establish target problem, read affected source files and check working tree (`git status`). Do not clobber existing user work.
2. Define expectations in concrete terms: input contracts, response shape, failure modes, metrics and tests.
3. Implement small cohesive diffs, use named helper functions, validate schema and numerical input, avoid unsafe deserialization paths.
4. For backend run `python -m pytest -q`; for frontend run `npm run build`. Test CSV 413/415/422 scenarios and all model routes when trusted local model artifacts exist. If unable to run, clearly mark *not run* and why.
5. Confirm changes do not leak credentials, raw datasets, private files or massive ZIPs; audit `git diff --stat`, `git status`, `.gitignore` and potentially oversize assets.
6. If research protocol changes, add a new experiment rather than overwriting prior outputs; record data splits, seeds, feature schema, train/validation/test provenance, model selection method and exact artifact names.
7. Update **both** Indonesian and English docs for interface changes; preserve link targets, markdown tables and alt text; verify referenced plot files exist before claiming screenshots are present.
8. Use precise conventional commits such as `feat(api): support bounded CSV batching`, `test(api): cover malformed schemas`, `docs: document condition-code semantics`.

## Model and claim boundaries
- UCI: 2,205 cycles; engineered 170 numeric features per cycle; four independent condition targets `cooler`, `valve`, `pump`, `accumulator`.
- Experiment 02 champions chosen by validation macro-F1; target-specific stratified 60/20/20. Report exactly stored test scores; don't infer out-of-distribution performance.
- Experiment 01: chronological 80/20; cooler test only class 100; binary degradation holdout 431/441 positive; IF ROC-AUC 0.5784; severe limitations.
- IMS: 2,156 + 984 + 6,324 snapshots; per-test reference; first 4,096 rows; test-specific threshold and alarm, not failure diagnosis.
- `confidence_proxy` is tree class confidence surrogate; no calibration claim. IMS `anomaly_score` is model-derived, thresholded deviation, not probability of damage.
- `GET /api/v1/models` checks local artifact paths; **not** a passing end-to-end health certification.

## Data and security policy
- Preserve exact engineered feature names/ordering. Backend must reject missing/extra, nonnumeric or nonfinite values. Never silently impute arbitrary columns at request boundary.
- CSV endpoint: <=10 MiB, <=2,000 rows, `.csv` extension; honor 413/415/422, no auto-unbounded ingestion. User-facing batch extension must maintain original order and errors.
- `joblib.load` executes Python pickle payloads: only load verified, trusted exports. Never allow arbitrary uploaded joblib or attacker-selected model path.
- Maintain least-privilege CORS, secret-free git tree, and no credentials in frontend builds. No production exposure without auth, abuse limits, audit log and threat model.
- Model files, source data, and experimental results are governed by separate license/provenance rules; don't relabel them as automatically permitted under repository code license.

## Definition of done
A task is complete only if matching source code exists, tests/build pass or limitations are reported, docs and evidence align, no unsupported scientific claims are introduced, outputs are located in approved folders, and the update can be reproduced by another contributor.

## Do not
- Rewrite notebook baseline or alter stored metrics for aesthetics.
- Add synthetic industrial signals and call them real observations.
- Describe IMS thresholds as validated equipment-failure events.
- Claim accuracy from a same-class 100-row UI test.
- Unconditionally run expensive/download-all jobs, or push raw research datasets.
- Modify unrelated project folders, credentials, user-origin files, or git history without permission.
