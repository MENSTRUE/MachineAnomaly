# Research reports — empirical evidence index

These CSV/JSON outputs are **observed outputs of Kaggle code**, not narrative estimates. Change them only through a documented rerun/new experiment, with provenance.

| Evidence | What it proves | It does not prove |
|---|---|---|
| `dataset_provenance.csv` | dataset links / attribution recorded | unrestricted redistribution |
| `hydraulic_feature_schema.json` | engineered feature names/shapes | validity of industrial calibration |
| `hydraulic_split_support.json` | chronological class-support skew | fair balanced holdout |
| `hydraulic_iforest_metrics.json` | ROC-AUC 0.5784, AP 0.9875 under 431/441 positives | effective anomaly discrimination in deployment |
| `hydraulic_supervised_metrics.csv` | Experiment 01 component baselines | production generalization |
| `ims_run_summary.csv` | three unlabeled monitoring summaries | per-snapshot fault labels |
| `research_gate.json` | execution and data assumptions | certified predictive maintenance |
| `experiment_02_hydraulic/heldout_final_metrics.csv` | test metrics for stratified 60/20/20 experiment | a directly comparable improvement against chronological Experiment 01 |
| `experiment_02_hydraulic/validation_candidate_ledger.csv` | model-selection search by validation score | external validation |
| `experiment_02_hydraulic/revision_history.json` | experiment provenance and split caveats | causally proven improvements |

## KPI summary (do not alter without rerun)
Experiment 02 test macro-F1: cooler **1.0000**, valve **0.9884**, pump **1.0000**, accumulator **0.9841**. Experiment 01 cooler is one-class-only in the chronological test, while accumulator macro-F1 is **0.1650**. IMS test counts are 2,156, 984 and 6,324; alarms are unlabeled change indicators.

Use `assets/plots/` for corresponding *real* figures and `docs/en/RESEARCH.md` for interpretation. Keep feature CSV snapshots in the existing `features/` directory, rather than silently relocating them from the current repo.
