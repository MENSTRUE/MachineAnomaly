# Kontrak API FastAPI

Base URL: `http://localhost:8000/api/v1`, Swagger `http://localhost:8000/docs`.

| Metode | Endpoint | Fungsi |
|---|---|---|
| GET | `/health` | Menampilkan status server; bukan pengujian model lengkap |
| GET | `/models` | Keberadaan empat model Hydraulic dan tiga IMS |
| POST | `/predict/csv?kind=hydraulic&target=cooler` | Upload file CSV 170 fitur numerik untuk kondisi cooler |
| POST | `/predict/csv?kind=ims&target=1st_test` | Upload CSV 10 fitur untuk indikator anomali sesi pertama |
| POST | `/predict/hydraulic/{target}` | Prediksi satu baris dalam JSON `features` |
| POST | `/predict/ims` | Prediksi satu baris JSON dengan `test` dan `features` |

Pilihan Hydraulic: `cooler`, `valve`, `pump`, `accumulator`. IMS: `1st_test`, `2nd_test`, `3rd_test`. File maksimal **10 MiB** dan **2.000 baris per request**. File UCI 2.205 baris harus dibagi; fitur harus sesuai nama dan urutan model hasil Kaggle. Kolom metadata yang dikenal seperti `cycle_id`, `test`, `snapshot` dapat diabaikan; kolom fitur tidak dikenal atau hilang ditolak.

```powershell
curl.exe -X POST "http://localhost:8000/api/v1/predict/csv?kind=hydraulic&target=cooler" `
    -F "file=@assets/examples/hydraulic_test_100.csv"
```

Kode error: **413** terlalu besar/banyak baris; **415** bukan `.csv`; **422** schema/target/nilai tidak valid. Hydraulic mengeluarkan `predicted_class`, `confidence_proxy` (jika tersedia, **bukan** probabilitas gagal terkalibrasi); IMS mengeluarkan `anomaly_score`, `threshold`, `alarm` (bukan konfirmasi bearing rusak). Keterangan lengkap [API Inggris](../en/API.md).
