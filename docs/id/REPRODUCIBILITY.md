# Reproduksibilitas eksperimen dan audit artefak

1. Ambil data asli dari [UCI](https://archive.ics.uci.edu/dataset/447/condition+monitoring+of+hydraulic+systems) dan [NASA IMS](https://data.nasa.gov/dataset/ims-bearings), jangan unggah ulang data mentah tanpa izin. Mount Kaggle: `/kaggle/input/datasets/wafabila/machineanomaly-dataset`.
2. Jalankan seluruh notebook `notebooks/` secara berurutan: bagian **00–13 Experiment 01** dan **14–19 Experiment 02 + final QA**. Seed **42**, catat versi package.
3. Audit profil 2.205 siklus/17 sumber sensor/170 fitur; IMS 2.156, 984, 6.324 snapshot; cek tidak ada duplikasi indeks split per model.
4. Experiment 01 tetap disimpan, Experiment 02 memilih model **hanya lewat validation macro-F1**, refit train+validation, lalu test sekali.
5. Audit hasil JSON/CSV, gambar, confusion matrix, manifest SHA-256, validasi reload joblib dan CRC ZIP Kaggle. `PASS_REPRODUCIBILITY` bukan sertifikasi industrial.
6. Taruh model di `models/`, laporan di `reports/`, hasil fitur engineering di folder `features/` existing, plot asli di `assets/plots/`. Jangan copy dataset mentah ke GitHub.
7. Jalankan `cd backend; python -m pytest -q`, `cd frontend; npm run build`, serta uji sample 100 baris. Bedakan log pelaksanaan nyata dari metrik yang diklaim.

Batas klaim, ancaman validitas, serta angka hasil dibahas di [RESEARCH.md](RESEARCH.md).
