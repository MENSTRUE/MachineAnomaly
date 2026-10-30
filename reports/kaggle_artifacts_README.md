# MachineAnomaly Day 25 — evidence package

Input Kaggle dataset: /kaggle/input/datasets/wafabila/machineanomaly-dataset

Original sources:
- Hydraulic https://archive.ics.uci.edu/dataset/447/condition+monitoring+of+hydraulic+systems | DOI 10.24432/C5CW21 | CC BY 4.0
- IMS https://data.nasa.gov/dataset/ims-bearings | Original IMS / University of Cincinnati; NASA distributor

Contracts:
- Hydraulic: condition diagnosis and anomaly scoring from cycle sensors; chronological holdout and baseline models.
- IMS: 3 independent vibration streams, early-reference anomaly timeline; NO per-file failure ground truth.
- NO direct model fusion or cross-dataset leaderboard.
- No production fault warranty / no calibrated lead-time claim.

Artifacts: reports/, plots/, features/, models/. The Kaggle inputs are not republished here.

Configuration: {
  "run_hydraulic": true,
  "run_ims": true,
  "hydraulic_test_fraction": 0.2,
  "hydraulic_reference_train_fraction": 0.6,
  "iforest_estimators": 240,
  "ims_read_rows_per_snapshot": 4096,
  "ims_max_files_per_test": null,
  "ims_early_reference_fraction": 0.25,
  "ims_contamination": 0.03,
  "zip_include_features": true
}
