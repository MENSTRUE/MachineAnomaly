# Roadmap dan kriteria penerimaan

## Tahap 0 — Data dan baseline
- [x] Dataset UCI dan IMS diinventarisasi; provenance ditulis.
- [x] Feature engineering: 170 fitur siklus UCI; 10 statistik IMS.
- [x] Experiment 01 kronologis dan monitoring anomali IMS dieksekusi.

## Tahap 1 — Revisi penelitian
- [x] Experiment 02 dibuat tanpa menghapus bagian 00–13.
- [x] Split stratified 60/20/20, tiga kandidat, pilihan berdasarkan macro-F1 validation.
- [x] Model, CSV hasil, confusion matrix, ZIP dan integrity gate diekspor.

## Tahap 2 — Aplikasi lokal
- [x] FastAPI memuat 4 champion Hydraulic + 3 IMS dari path tepercaya.
- [x] Frontend React/Vite membaca respons model asli.
- [x] Pengujian UI cooler 100 baris sukses.
- [ ] Uji end-to-end semua 7 model dan kelas Hydraulic beragam.
- [ ] CSV auto batch >2.000 baris, progress, partial-error dan ekspor hasil.
- [ ] Test model output regresi dan laporan prediksi vs label aktual.

## Tahap 3 — Validitas eksternal
- [ ] Split berdasarkan waktu/rezim, dataset mesin di luar UCI/IMS.
- [ ] Analisis IMS spektral/full snapshot, truth label dan threshold sensitivity.
- [ ] OOD detection, uncertainty, probability calibration.

## Tahap 4 — Produksi
- [ ] Version lock, CI, test dan manifest model signed.
- [ ] Auth, RBAC, TLS, rate limit, audit, privasi, logging tanpa bocor data.
- [ ] Validasi mesin nyata dan persetujuan manusia sebelum keputusan safety.

**Aturan:** checkbox hanya boleh ditandai selesai jika sudah ada bukti nyata berupa file, kode, log atau uji; tidak cukup sekadar tampilan dashboard.
