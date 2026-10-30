# Frequently asked questions

**What is MachineAnomaly?** A reproducible, local research full-stack prototype for Hydraulic condition codes and IMS vibration anomaly indicators, not industrial-grade fault detection.

**Why two datasets?** UCI has supervised discrete condition labels; IMS has unlabeled time-series degradation records. Their training/evaluation methodologies cannot be merged or averaged.

**What is the source of truth?** The executed Kaggle notebook, `reports/` CSV/JSON evidence and current implementation (`backend/app`, `frontend/src`). README summarizes their contents.

**Why are Experiment 02 scores close to 100%?** Its within-dataset target-specific stratified split permits testing interpolation among sampled conditions. It does not certify temporal, new-machine or real-world generalization; chronological Experiment 01 is materially weaker for valve and accumulator.

**Can I say 99% fault detection accuracy?** No. The task is operating **condition-class classification**, not labeled industrial failure-event prediction.

**Does IMS identify a broken bearing?** Not with verified timestamp-level labels. It flags model-relative deviation from an early reference and visualizes changes across known run-to-failure recordings.

**Is the confidence proxy a failure probability?** No. It comes from a tree ensemble class output, not calibrated reliability analysis.

**Why 7/7 models?** Four Hydraulic champion model paths plus three IMS IsolationForest model paths are present. File existence is not comprehensive performance validation.

**What does the UI screenshot with 100 class-3 outputs demonstrate?** A valid frontend–FastAPI–model inference path for Hydraulic cooler. The early UCI sample is single-class, so it is not a balanced benchmark.

**Why reject 2,205 rows?** The API permits 2,000 rows and 10 MiB per request to bound resources. Use multiple slices; automatic batch ingestion is future work.

**Can the frontend read raw IMS or Hydraulic files?** No. Use the exact engineered feature CSV schema from Kaggle.

**Should trained joblib models be committed?** Only verified and permitted files, after checking size, license/provenance and security implications. Never load arbitrary joblib from users.

**Where should graphs go?** Actual saved plots in `assets/plots/` and actual screenshots in `assets/screenshots/`. Cite them in docs using relative Markdown links.

**Which license applies?** Consult repository root `LICENSE` for code. Upstream datasets have independent terms; do not assume code license covers them or derivatives.

**What makes this release final?** Final for the **Day 25 notebook + working local prototype milestone**; not final for production deployment, external validation or comprehensive model integration tests.
