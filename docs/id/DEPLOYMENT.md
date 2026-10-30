# Deployment dan operasional

## Mode yang sudah dibuktikan: lokal
```powershell
# Terminal 1
cd "D:\porto\100 day\day 25\MachineAnomaly\backend"
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8000
# Terminal 2
cd "D:\porto\100 day\day 25\MachineAnomaly\frontend"
npm install
npm run build
npm run dev
```
Buka `http://localhost:5173`, `http://localhost:8000/docs`. Simpan model joblib tepercaya pada `models/`; override via `MACHINEANOMALY_MODEL_DIR` bila diperlukan. `CORS_ORIGINS` mengatur origin frontend yang diizinkan.

## Sebelum produksi harus tersedia
Dependency lockfile serta versi sklearn kompatibel, model hash/signature, autentikasi dan otorisasi, TLS, rate limiting, pengamanan upload CSV, reverse proxy `/api`, observability, audit log, kebijakan privasi/retensi, backup/rollback, pemeriksaan izin dataset, evaluasi hardware nyata, dan persetujuan manusia sebelum tindakan pemeliharaan/safety.

**Belum ada bukti deployment produksi.** Vite development proxy hanya berlaku saat development. Dashboard localhost sudah merupakan milestone portofolio yang nyata, tetapi jangan ditulis sebagai live monitoring pabrik. [Security](SECURITY.md) · [Roadmap](ROADMAP.md).
