# Delivery roadmap — truthful milestones

## Phase 0: Source and research baseline (complete)
- [x] Record UCI and IMS provenance; keep datasets separate.
- [x] Extract UCI 170 cycle-level statistical features and IMS short-window summary features.
- [x] Run original baseline Experiment 01 and retain chronological test limitations.
- [x] Evaluate IMS per-run early-reference, store unlabeled alarm trend and figures.

## Phase 1: Research refinement (complete in Kaggle)
- [x] Append Experiment 02 without changing original Experiment 01.
- [x] Train/validation/test target-specific 60/20/20; select RF/ExtraTrees by validation macro-F1.
- [x] Refit selected models and save final held-out metrics, splits, confusion matrices and models.
- [x] Verify export/reload, archive CRC and research QA gate.

## Phase 2: Full-stack prototype (partially verified)
- [x] FastAPI inference endpoint and fixed-path joblib registry.
- [x] React/Vite dashboard with real HTTP responses.
- [x] Local screenshot demonstrates Hydraulic cooler 100-row inference.
- [ ] End-to-end smoke tests for every Hydraulic target and all three IMS runs.
- [ ] Golden-fixture regression tests for model outputs and accurate class label mapping.
- [ ] Automatic multi-batch CSV upload with partial failure/retry handling.
- [ ] Sample-by-sample ground-truth matching and exportable analysis table.

## Phase 3: Research robustness (planned)
- [ ] Rigorous chronology/operating-regime grouped split, adequate class support and sensitivity analysis.
- [ ] Evaluate fully sampled IMS segments plus spectral features and reference contamination sensitivity.
- [ ] Independent target equipment dataset and actual fault labels, if authorized.
- [ ] Calibrated confidence, OOD rejection, model uncertainty and domain drift study.

## Phase 4: Production engineering (not started)
- [ ] Lock dependencies, CI/CD and runtime model reproducibility; publish evidence manifest.
- [ ] Authentication/RBAC, TLS, request limits, signed model artifacts and security review.
- [ ] MLOps monitoring, audit logging, drift detection, privacy/retention policy.
- [ ] Hardware integration with human approval and documented safety constraints.

**Definition of done:** Each checkbox needs evidence (commit, test report, run output or approved artifact); do not mark a research claim done just because a dashboard renders.
