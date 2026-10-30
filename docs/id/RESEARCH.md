# Metodologi penelitian, audit, metrik, dan batas klaim

## Dataset dan label
**UCI Hydraulic** ([sumber UCI](https://archive.ics.uci.edu/dataset/447/condition+monitoring+of+hydraulic+systems), DOI 10.24432/C5CW21, lisensi sumber CC BY 4.0): **2.205 siklus**; 17 sumber sensor (`PS1–PS6`, `EPS1`, `FS1–FS2`, `TS1–TS4`, `VS1`, `CE`, `CP`, `SE`); masing-masing menghasilkan 10 statistik sehingga 170 fitur/siklus. Label `profile.txt`: cooler {3,20,100}, valve {73,80,90,100}, pump {0,1,2}, accumulator {90,100,115,130}, stable_flag {0,1}. Label ini adalah *kondisi komponen*, bukan waktu terjadinya kerusakan mesin.

**NASA IMS Bearings** ([sumber NASA](https://data.nasa.gov/dataset/ims-bearings)): **9.464 snapshot**: test pertama 2.156 (8 kanal), kedua 984 (4 kanal), ketiga 6.324 (4 kanal). Ringkasan statistik dibuat dari **4.096 baris awal per snapshot**, bukan keseluruhan sinyal atau FFT. Meskipun data terdiri dari sesi run-to-failure, **tidak tersedia ground truth per-snapshot yang sah** untuk klaim akurasi deteksi kerusakan.

## Experiment 01 — Baseline kronologis
Train 1.764 / test 441. Hanya **11 siklus** training yang sehat+stabil sekaligus; model anomali memakai **proxy least-degraded stable** dari training. Test untuk target binary degraded berisi **431 positif dan 10 negatif**. IsolationForest ROC-AUC **0,578422**, average precision **0,987459**; AP tidak boleh dipakai sendirian karena prevalensi positif 97,7%.

| Target | Accuracy | Macro-F1 | Catatan penting |
|---|---:|---:|---|
| Cooler | 1,0000 | 1,0000 | Test hanya mengandung kelas 100 |
| Valve | 0,7143 | 0,6932 | Shift kondisi masih signifikan |
| Pump | 1,0000 | 1,0000 | Bukan uji perangkat di luar dataset |
| Accumulator | 0,1905 | 0,1650 | Performa kronologis rendah |

## Experiment 02 — Refinement diagnostik
Per target dibuat split stratified acak **1.323 train, 441 validation, 441 test**. Ada tiga kandidat: RF balanced 240, RF regularized 400, dan ExtraTrees balanced 300. Pilihan menggunakan **validation macro-F1**, lalu refit train+validation dan satu kali evaluasi test. Semua catatan split dan hasil dapat dilihat di `../../reports/experiment_02_hydraulic/`.

| Target | Model terpilih | Accuracy test | Macro-F1 test |
|---|---|---:|---:|
| Cooler | RF balanced 240 | 1,000000 | **1,000000** |
| Valve | RF balanced 240 | 0,990930 | **0,988448** |
| Pump | ExtraTrees balanced 300 | 1,000000 | **1,000000** |
| Accumulator | RF balanced 240 | 0,986395 | **0,984130** |

**Batas validitas:** Experiment 01 dan 02 mempunyai partisi berbeda sehingga tidak boleh diklaim peningkatan langsung. Sampling acak masih dapat membawa korelasi siklus/rezim pengoperasian ke test. Tidak ada bukti generalisasi mesin baru.

## Model IMS — Monitoring anomali tanpa label
Referensi 25% awal per test (539 / 246 / 1.581 snapshot), IsolationForest dengan threshold dari skor referensi training. Later alarm fraction berturut-turut **0,3816; 0,3631; 0,0500**. Alarm 10% akhir **0,9814; 1,0000; 0,3370**. Ini *frekuensi indikator perubahan*, **bukan F1, sensitivitas, akurasi, tanggal kegagalan, atau RUL**.

## Audit dan pelaporan
Bukti: `reports/dataset_provenance.csv`, `hydraulic_split_support.json`, `hydraulic_iforest_metrics.json`, `hydraulic_supervised_metrics.csv`, `ims_run_summary.csv`, `research_gate.json`, `experiment_02_hydraulic/heldout_final_metrics.csv` dan `revision_history.json`. Grafik nyata terdapat di `assets/plots/`. Jangan mengubah metrik agar terlihat tinggi.

## Claim boundaries
**Boleh:** "Model klasifikasi kondisi Hydraulic memiliki macro-F1 0,9884 pada split stratified internal untuk valve"; "IMS menunjukkan perubahan sinyal relatif referensi awal"; "uji UI cooler 100 baris berhasil". **Tidak boleh:** "Akurasi deteksi kerusakan pabrik 99%", "model memprediksi kapan bearing rusak", "confidence merupakan probabilitas gagal", "Experiment 02 pasti meningkat dibanding Experiment 01", "7/7 file berarti seluruh model sudah lulus tes real-world".

## Penelitian lanjutan
Grouped split per rezim, external machine evaluation, kalibrasi, fitur spektral penuh, kebenaran label fault dan kebijakan *out-of-distribution*. Seluruh pengujian tambahan harus dibuat sebagai eksperimen baru, bukan menimpa baseline.
