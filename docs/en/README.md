# MachineAnomaly — technical overview (English)

MachineAnomaly is a local research prototype joining two *separate* experimental datasets: UCI Hydraulic supervised **condition classification** (four targets) and NASA/IMS unlabeled bearing vibration **change detection** (three test-specific Isolation Forest models). It serves real Kaggle-exported joblib artifacts through FastAPI to a React dashboard. It is not a safety-certified machine-failure predictor.

## Before / Now / Next
**Before:** Hydraulic cycle-level sensor matrices and condition labels, IMS timestamp snapshots, Kaggle baseline with chronological holdout. **Now:** preserved baseline plus Experiment 02 target-specific stratified model-selection study; 7 model artifact paths; local dashboard; one successful 100-row Hydraulic cooler UI inference. **Next:** class-diverse and all-model end-to-end tests, batching, outside-regime evaluation, model calibration, and production security review.

**Research evidence:** [RESEARCH.md](RESEARCH.md) and `../../reports/`. **Runtime:** [ARCHITECTURE.md](ARCHITECTURE.md), [API.md](API.md), [DEPLOYMENT.md](DEPLOYMENT.md). **Research limitations:** no fault-event truth for IMS, no RUL, no raw sensor stream pipeline, no claim that stratified results are equivalent to chronological results. Refer to the [root README](../../README.md) for the full metrics table, source URLs, genuine plots and repository layout.
