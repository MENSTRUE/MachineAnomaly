# Troubleshooting MachineAnomaly

## "Maximum 2000 rows per request" (413)
CSV Hydraulic berisi **2.205 baris**. Backend maksimal 2.000; ini bukan model error. Buat sampel CSV 100 baris melalui PowerShell:
```powershell
@'
import pandas as pd
from pathlib import Path
r = Path(r'D:\porto\100 day\day 25\MachineAnomaly')
f = pd.read_csv(r/'features'/'hydraulic_cycle_features.csv')
f = f.drop(columns=['cycle_id','Unnamed: 0'], errors='ignore')
assert f.shape[1] == 170
out = r/'assets'/'examples'/'hydraulic_test_100.csv'
out.parent.mkdir(parents=True,exist_ok=True)
f.head(100).to_csv(out,index=False)
print(out)
'@ | python -
```

## "422 Unprocessable Entity"
Kolom fitur tidak sesuai, ada ekstra/hilang, nilai bukan numerik, NaN/Inf, target tidak valid, atau file kosong. Gunakan CSV hasil Kaggle, bukan raw sensor. Hydraulic 170 fitur; IMS 10 fitur dan tiap test cocok dengan modelnya.

## "415 Unsupported Media Type"
Nama file harus `.csv`; jangan upload `.txt`, `.zip`, `.parquet`.

## API online, tetapi grafik masih kosong
Periksa request network browser, backend port 8000, server `uvicorn`, pemilihan target, file CSV dan error response. `/health` tidak menjalankan model.

## 7/7 model ada tetapi prediksi gagal
`/models` hanya mengecek file ada. Periksa direktori `models/experiment_02_hydraulic/` dan `models/ims_*_iforest.joblib`, versi scikit-learn, serta log error model. Jangan load file joblib dari pihak tidak tepercaya.

## Semua 100 cooler = class 3
Sampel awal dataset memang cooler class 3. Ini bukti jalur inferensi berfungsi, **bukan akurasi semua kelas**. Untuk evaluasi kelas 20/100 harus ambil siklus yang relevan dan label cocok.

## Error instalasi
Aktifkan venv di folder `backend/`, `python -m pip install -r requirements.txt`, `python -m uvicorn app.main:app --reload --port 8000`; untuk UI jalankan `npm install`, `npm run dev` dalam `frontend/`. Cek `npm run build` sebelum klaim build lulus.

## Plot hilang di README
Gambar Markdown merujuk `assets/plots/` hasil Kaggle asli. Kalau hilang, ekstrak lagi dari ZIP Kaggle; jangan membuat grafik palsu hanya untuk mengisi dokumentasi.
