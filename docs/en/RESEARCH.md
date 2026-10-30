# Research methodology, audit and claim boundaries

## Research questions
**RQ1 — Hydraulic:** Can features engineered from the UCI condition-monitoring cycles discriminate four discrete component **condition states** under explicitly stated evaluation splits? **RQ2 — IMS:** Can unsupervised vibration indicators, calibrated against an early segment of each test's own history, visualize atypical signal changes over run-to-failure recordings? The answers are **not interchangeable**.

## Data audit and provenance
- UCI: 2,205 cycles, original `profile.txt` columns = cooler (`3,20,100`), valve (`73,80,90,100`), pump (`0,1,2`), accumulator (`90,100,115,130`), stable flag (`0,1`). Source: https://archive.ics.uci.edu/dataset/447/condition+monitoring+of+hydraulic+systems ; DOI 10.24432/C5CW21 ; attribution CC BY 4.0.
- UCI features: **17** original sensor matrices (PS1–6, EPS1, FS1–2, TS1–4, VS1, CE, CP, SE). **10** statistics each = **170 cycle-level features**: mean, std, min, max, q25, median, q75, RMS, mean absolute change, std change. Every sensor matrix is aligned by cycle; individual cycle retained as atomic sample.
- NASA IMS: `1st_test` 2,156 timestamps/8 channels, `2nd_test` 984/4, `3rd_test` 6,324/4; original source https://data.nasa.gov/dataset/ims-bearings . The experiments refer to run-to-failure sessions but **do not supply trustworthy per-timestamp failure labels**. Source terms must be reviewed before redistribution.
- Snapshot processing reads **first 4,096 signal rows** per timestamp; features aggregate RMS, std, peaks, crest factors, kurtosis across available channels (10 features). Not a full-window FFT or diagnostic fault-frequency calculation.
- Data not merged across rigs. Split and provenance files under `reports/` record actual execution.

## Experiment 01 — chronological baseline and stress test
UCI ordered 1,764 train / 441 test. Stable jointly healthy training reference contains **only 11 cycles**, so the IF baseline deliberately falls back to **least-degraded stable training-only proxy** (never call these indisputably healthy). Binary target `any_component_degraded` is 431 positive / 10 negative in the chronological test (97.7% prevalence).

| Experiment 01 target | Accuracy | Macro-F1 | Caveat |
|---|---:|---:|---|
| Cooler | 1.0000 | 1.0000 | Test contains only class **100** |
| Valve | 0.7143 | 0.6932 | Changes in condition distribution/sequence |
| Pump | 1.0000 | 1.0000 | Check external validity |
| Accumulator | 0.1905 | 0.1650 | Poor under chronological holdout |

Anomaly IF on UCI: ROC-AUC **0.578422**, average precision **0.987459**, threshold **0.575790** (95th percentile of training proxy score), flagged positives **213**. AP must be interpreted against extremely high positive prevalence, not promoted as a strong anomaly result. See `reports/hydraulic_iforest_metrics.json` and `reports/hydraulic_split_support.json`.

## Experiment 02 — complementary within-dataset diagnostic protocol
For **each target independently**, stratified random training **1,323**, validation **441**, test **441**. Test rows are untouched until after model selection. Candidate set was predeclared: balanced RF with 240 estimators, regularized balanced RF with 400 estimators, and balanced ExtraTrees with 300 estimators. Choose by validation **macro-F1**, deterministic candidate-order tiebreak; retrain selected configuration on train + validation, then evaluate test once. Fit model-specific imputer only on corresponding training partitions.

| Target | Validation macro-F1 | Test accuracy | Test macro-F1 | Champion |
|---|---:|---:|---:|---|
| Cooler | 1.000000 | 1.000000 | 1.000000 | rf_balanced_240 |
| Valve | 0.979118 | 0.990930 | 0.988448 | rf_balanced_240 |
| Pump | 0.996616 | 1.000000 | 1.000000 | extratrees_balanced_300 |
| Accumulator | 0.990622 | 0.986395 | 0.984130 | rf_balanced_240 |

Actual authoritative CSV: `reports/experiment_02_hydraulic/heldout_final_metrics.csv`; validation ledger: `validation_candidate_ledger.csv`; per-class reports and confusion matrices are saved under the Experiment 02 folders. Random partitioning may preserve temporal and operating-regime correlation; these are **within-dataset interpolation** scores, **not an independent industrial machine test**. One target's test rows differ from another's and from Experiment 01's test rows.

## IMS experiment — unlabeled model-relative anomaly monitoring
Separate fit and threshold for each test, using its earliest **25%** of snapshots as reference (539/246/1,581). IsolationForest with `contamination=.03` and **training-only** cutoff at 97th percentile. Saved later alarm fractions: **0.381571**, **0.363144**, **0.049968**; last-10% fractions: **0.981395**, **1.0**, **0.337025** for tests 1–3. See `reports/ims_run_summary.csv` and saved timeline plots. Alarm fraction is **not sensitivity, specificity, F1, accuracy, validated onset time or failure prevalence**.

## Threats to validity
1. Experiment 02 class stratification does not rule out sample similarity from adjacent cycles/regimes or data-collection order.
2. Experiment 01 chronological test under-represents cooler classes and heavily imbalances binary degraded labels.
3. No external machine, manufacturing site or changed hardware-domain validation.
4. Raw sensor engineering/calibration uncertainties not covered by model CV or application tests.
5. Per-test IMS reference may contain changing conditions; no certified normal-fault segmentation or timestamp-level truth.
6. IMS reads only first 4,096 rows per snapshot; some failure signatures might occur elsewhere in the signal or its spectrum.
7. Model serialization/version compatibility, calibration and measurement-unit consistency require deployment-level audits.
8. Selected target models use different stratified cycle partitions; no common multi-target experiment is established.

## Claim boundaries
**Allowed:** "UCI Hydraulic Experiment 02 achieved held-out macro-F1 [exact values] using target-specific stratified random splits"; "IMS displayed test-specific unsupervised anomaly alarms"; "one local cooler CSV UI smoke test processed 100 rows". **Not allowed:** "98–100% failure detection in production"; "IMS predicts remaining useful life"; "Experiment 02 improved chronological performance by X%"; "7/7 loaded proves all seven models are accurate"; "anomaly score is probability of breakdown". Pass reproducibility gates validate artifacts and test separation, not operational quality.

## Future experiments
Group/temporal split by operating regimes, cross-rig evaluation, accurate fault ground truth, probabilistic calibration, full-signal RMS/FFT sensitivity study, error analysis, comprehensive all-model smoke tests and uncertainty/OOD policy. Preserve original outputs and use Experiment 03+ naming rather than rewriting results.
