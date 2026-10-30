# MachineAnomaly — Dokumentasi Bahasa Indonesia

**Day 25 / 100 Projects · Pemantauan Kondisi Hidrolik + Anomali Getaran Bearing · FastAPI + React.** Ini adalah proyek penelitian dan portofolio yang menjalankan model `.joblib` asli hasil Kaggle, **bukan** sistem diagnosis kerusakan industri tersertifikasi.

## Before — Now — Next
| Tahap | Keadaan | Bukti |
|---|---|---|
| Before | Dataset UCI Hydraulic 2.205 siklus, NASA/IMS 9.464 snapshot; eksperimen awal | Notebook bagian 00–13 |
| Now | Experiment 02 sudah dieksekusi, empat classifier kondisi + tiga model anomali IMS; frontend-backend berjalan | `reports/experiment_02_hydraulic/heldout_final_metrics.csv`; grafik `assets/plots/`; satu smoke test cooler 100 baris sukses |
| Next | Pengujian 7 model end-to-end, batching >2.000 baris, evaluasi domain baru, security dan deployment | [Roadmap](ROADMAP.md) |

## Hasil utama yang boleh diklaim
Experiment 02 memakai pembagian stratified **train 60%, validation 20%, test 20%** per target (1.323/441/441). Test macro-F1: **cooler 1,0000**, **valve 0,9884**, **pump 1,0000**, **accumulator 0,9841**. Hasil ini bukan bukti ketepatan mendeteksi *kerusakan fisik mesin nyata*. Experiment 01 memakai holdout kronologis dan jauh lebih lemah untuk accumulator (macro-F1 **0,1650**); jangan membandingkannya sebagai kenaikan langsung karena pembagian test berbeda.

IMS mengolah 2.156 + 984 + 6.324 snapshot. Model IsolationForest menghasilkan skor dan *alarm perubahan terhadap referensi awal*, **bukan label kerusakan yang tervalidasi**.

![Grafik anomali hidrolik Experiment 01](../../assets/plots/hydraulic_anomaly_timeline.png)
![Grafik IMS run pertama](../../assets/plots/ims_1st_test_anomaly_trend.png)

## Tautan dokumentasi lengkap
[Penelitian dan metrik](RESEARCH.md) · [Arsitektur](ARCHITECTURE.md) · [API](API.md) · [Reproduksibilitas](REPRODUCIBILITY.md) · [Testing](TESTING.md) · [Deployment](DEPLOYMENT.md) · [Security](SECURITY.md) · [Troubleshooting](TROUBLESHOOTING.md) · [FAQ](FAQ.md) · [Roadmap](ROADMAP.md). Detail repo dan seluruh tabel metrik juga tersedia pada [README utama](../../README.md).

## Jalankan lokal (Windows PowerShell)
```powershell
cd "D:\porto\100 day\day 25\MachineAnomaly\backend"
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8000
# terminal lain
cd "D:\porto\100 day\day 25\MachineAnomaly\frontend"
npm install
npm run dev
```
Buka http://localhost:5173 dan http://localhost:8000/docs. Upload **CSV fitur hasil Kaggle**, maksimal **2.000 baris dan 10 MiB**; jangan mengunggah data sensor mentah. Gunakan 100 baris dari `features/hydraulic_cycle_features.csv` untuk uji awal.

## Lisensi dan batas klaim
Lisensi kode merujuk file root `LICENSE` yang benar-benar ada dan telah ditinjau; UCI dan IMS punya ketentuan data terpisah. Jangan mempublikasikan data asli, secret, atau model joblib yang tidak tepercaya. Tidak ada bukti validasi real-time pabrik, safety interlock, RUL, akurasi kerusakan per snapshot IMS, atau probabilitas kerusakan terkalibrasi.
