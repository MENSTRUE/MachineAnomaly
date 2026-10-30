# Reproducibility and evidence audit

## Inputs
1. Original UCI Hydraulic source (2,205 profile rows and sensor files), cited in `reports/dataset_provenance.csv`.
2. NASA/IMS original snapshot files, three independent `1st_test`, `2nd_test`, `3rd_test` directories.
3. Kaggle input mount `/kaggle/input/datasets/wafabila/machineanomaly-dataset`. If Kaggle changes it, adjust **only notebook `INPUT_ROOT`** rather than broad path rewrites.
4. Notebook from `notebooks/` and project dependency versions; experiment seed **42**. Record runtime Python, scikit-learn and other package versions in saved execution logs.

## Execution procedure
- Inspect extracted dataset roots, profiles and channel counts. Validate UCI has 2,205 cycles, 17 sensor sources and 170 finite engineered features; IMS contains 2,156/984/6,324 usable timestamps.
- Execute Experiment 01 sections **00–13** in order. Preserve original chronological split, reference proxy policy, charts, raw observed scores and ZIP.
- Execute appended Experiment 02 sections **14–19** and QA. Keep per-target 60/20/20 partitions, save split class support, candidate ledger, selected champion and 441 held-out predictions, per-class reports and model export/reload check.
- Inspect quality gate and **revised artifact ZIP**; verify ZIP CRC, file inventory and SHA-256 manifest. A `PASS_REPRODUCIBILITY` flag is a technical gate, not a research impact or production certification.
- Extract outputs into `models/`, `reports/`, `assets/plots/` and existing `features/`; do not upload raw dataset or entire Kaggle input to GitHub.

## Audit commands
```powershell
# From repo root
python -m pytest -q backend/tests  # run from backend/ instead if imports need local cwd
cd backend; python -m pytest -q; cd ..
cd frontend; npm run build; cd ..
git status
Get-ChildItem models -Recurse -Filter *.joblib | Select-Object FullName,Length
```

## Recorded checkpoints
- Experiment 02 stored CSV macro-F1: cooler 1.0, valve 0.9884477735, pump 1.0, accumulator 0.9841300400.
- Experiment 01 anomalous binary ROC-AUC 0.578422 on skewed chronological test; report limitations, not solely average precision.
- IMS metrics measure per-test alarm frequency without per-snapshot fault labels.
- Screenshot-based local UI smoke test: 100 Hydraulic cooler rows processed successfully; all class 3 from early dataset portion, not representative per-class evaluation.

## What counts as evidence
Actual run logs + machine-readable metrics + feature schemas + split membership IDs + model export/reload + genuine generated plots. Do not backfill graphs or test outcomes with synthetic data. If a named artifact is missing, describe it as missing and reproduce from the Kaggle export.
