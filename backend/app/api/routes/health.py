from fastapi import APIRouter
from app.inference.registry import status
router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok", "service": "MachineAnomaly", "demo": False}

@router.get("/models")
def models():
    return status()
