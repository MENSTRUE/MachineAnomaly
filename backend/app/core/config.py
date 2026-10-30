from pathlib import Path
import os

# backend/app/core/config.py -> repository root
REPO_ROOT = Path(__file__).resolve().parents[3]
MODEL_ROOT = Path(os.getenv("MACHINEANOMALY_MODEL_DIR", str(REPO_ROOT / "models"))).resolve()
MAX_UPLOAD_BYTES = 10 * 1024 * 1024
MAX_ROWS = 2000
ALLOWED_ORIGINS = [x.strip() for x in os.getenv("CORS_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173").split(",") if x.strip()]
