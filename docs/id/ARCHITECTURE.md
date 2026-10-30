# Arsitektur dan aliran data

```text
Dataset asli UCI / IMS (terpisah)
  -> Notebook Kaggle: audit, preprocessing, training, evaluasi
     -> UCI: 170 fitur siklus -> 4 champion classifier
     -> IMS: 10 fitur snapshot -> 3 IsolationForest per test
  -> CSV fitur dan model joblib tepercaya
  -> Upload CSV melalui React/Vite
  -> FastAPI /api/v1/predict/csv
  -> Validasi tipe, ukuran, baris, nama kolom dan nilai numerik
  -> Load model sesuai target, prediksi, JSON
  -> Grafik, distribusi dan audit trail dashboard
```

**Frontend**: `frontend/src/services/api.ts`; **backend**: `backend/app/api/routes/predictions.py`, `backend/app/services/predict.py`; **registry**: `backend/app/inference/registry.py`; **config**: `backend/app/core/config.py`. Upload hanya CSV hasil feature engineering, bukan raw sensor. API tidak menyimpan stream mesin nyata dan belum melakukan inferensi streaming real-time.

Endpoint `/models` memeriksa keberadaan file path, bukan kinerja model. Skema Hydraulic harus 170 fitur dan IMS harus sesuai 10 fitur di artefak. IMS threshold spesifik per test dan tidak bisa digabung lintas run. Lihat [API](API.md), [security](SECURITY.md), [Testing](TESTING.md).
