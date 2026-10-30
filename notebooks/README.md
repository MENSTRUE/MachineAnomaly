# Notebooks — research execution record

The Kaggle notebook (currently in this repository as `machineanomaly.ipynb` in the observed working tree) is the **executable research source of truth**. Do not rename the file speculatively or overwrite it with template content. The intended final notebook keeps sections **00–13 Experiment 01**, then **14–19 Experiment 02 plus QA**.

**Datasets:** Kaggle mount `/kaggle/input/datasets/wafabila/machineanomaly-dataset`; UCI Hydraulic (2,205 cycles); IMS (9,464 timestamp snapshots in three tests). Change `INPUT_ROOT` only if Kaggle mounting differs.

**Experiment 01:** 17 UCI sensors → 170 features, chronological holdout, baseline tree classification and IsolationForest; IMS early-reference per test using initial 4,096 rows/snapshot. **Experiment 02:** independent target-specific stratified train 60%, validation 20%, test 20%; 3 ensemble candidates, select by validation macro-F1; refit train+validation then one test. Original and revised splits are **not equivalent**.

### Reproduce
1. Attach the original data through Kaggle; inspect mount layout, avoid committing raw data.
2. `Run All`; inspect errors and actual metrics, rather than replaying saved screenshots.
3. Save Kaggle version and extract ZIP artifacts. Verify CRC and feature/model manifest.
4. Map outputs back to approved folders: `models/`, `reports/`, `assets/plots/`, and existing `features/`.
5. Record package versions, random seed and dataset provenance. Do not claim model quality solely from `PASS_REPRODUCIBILITY`.

More details: [English protocol](../docs/en/RESEARCH.md), [reproduction](../docs/en/REPRODUCIBILITY.md), [Indonesian notes](../docs/id/REPRODUCIBILITY.md).
