# Trusted exported model artifacts

This folder contains **serialized Python/joblib models** produced by the author's Kaggle run, not human-readable model source code. Only load trusted exports: joblib/pickle deserialization can execute arbitrary code.

Expected inference paths:
```text
models/
├── experiment_02_hydraulic/
│   ├── hydraulic_cooler_champion.joblib
│   ├── hydraulic_valve_champion.joblib
│   ├── hydraulic_pump_champion.joblib
│   └── hydraulic_accumulator_champion.joblib
├── ims_1st_test_iforest.joblib
├── ims_2nd_test_iforest.joblib
└── ims_3rd_test_iforest.joblib
```

Other Experiment 01 `hydraulic_*_rf.joblib` and `hydraulic_anomaly_iforest.joblib` files are experimental evidence and **not the active champion routes**. Artifact presence is not a comprehensive inference or statistical validation. The HTTP model registry reports path existence.

Hydraulic artifacts require **170 ordered cycle features** (exact names in artifact `feature_columns`). IMS artifacts require the exact stored 10-feature schema and test-specific preprocessing/threshold. Do not feed raw vibration streams directly.

Model training dependencies and feature computation should match the Kaggle notebook. Verify artifact hash/manifests, loading in the intended environment, and inference round-trip; do not unpickle anything from unknown uploads or PRs. Never claim models provide proven RUL, machine failure events or calibrated risk.
