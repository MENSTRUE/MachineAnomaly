# Strategi pengujian dan quality gate

| Lapisan | Pengujian | Status bukti |
|---|---|---|
| Kontrak API | `/health`, `/models`, invalid kind dan ekstensi salah | Empat pengujian backend pernah dilaporkan lulus |
| Smoke test UI | Hydraulic cooler + CSV 100 baris | Terlihat sukses di screenshot pengguna: 100 hasil kelas 3 |
| Ketujuh model | Empat Hydraulic + tiga IMS | **Belum** terverifikasi semuanya satu per satu melalui UI |
| Validasi data | Skema tepat, NaN/Inf ditolak, 10 MiB dan 2.000 baris | Sudah diimplementasi di backend; perlu tes otomatis menyeluruh |
| Frontend build | `npm run build` | Harus dicatat hasilnya setiap rilis |
| Kinerja ML | Metrik actual Experiment 01/02 dan IMS | Tersimpan di `reports/`; berbeda dari pengujian API |
| Security | Auth, rate limit, data governance | Belum siap untuk deployment publik |

## Langkah manual
1. Buka API docs dan `/api/v1/models`, pastikan model yang akan dipakai memang tersedia.
2. Buat CSV fitur 100 baris dari `features/hydraulic_cycle_features.csv`, upload Hydraulic cooler. Kemudian uji valve, pump, accumulator.
3. Untuk IMS, buat contoh CSV dari `features/ims_1st_test_features.csv`, `ims_2nd_test_features.csv`, `ims_3rd_test_features.csv`, selalu gunakan model run yang cocok.
4. Coba input invalid: 2.205 baris, `.txt`, kolom tak dikenali, fitur kurang, file kosong, NaN. Harus ditolak secara eksplisit.
5. Untuk menguji akurasi UI, cocokan `cycle_id` terhadap `profile.txt` dan gunakan kelas beragam, jangan hanya 100 baris awal (semuanya cooler class 3).
6. Cek performa dan aksesibilitas, serta pastikan UI bukan menampilkan data prediksi buatan.

**Lulus smoke test ≠ lulus penelitian generalisasi ≠ lulus security audit.** Definisi lebih lengkap pada [TESTING Inggris](../en/TESTING.md).
