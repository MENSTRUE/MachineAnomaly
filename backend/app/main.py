from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import ALLOWED_ORIGINS
from app.api.routes import health, predictions

app = FastAPI(title="MachineAnomaly API", version="1.0.0", description="Real inference from trusted Day 25 Kaggle model artifacts; no simulated predictions.")
app.add_middleware(CORSMiddleware, allow_origins=ALLOWED_ORIGINS, allow_methods=["GET", "POST"], allow_headers=["*"])
app.include_router(health.router, prefix="/api/v1", tags=["System"])
app.include_router(predictions.router, prefix="/api/v1", tags=["Inference"])
