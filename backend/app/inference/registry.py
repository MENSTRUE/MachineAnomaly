from __future__ import annotations
from functools import lru_cache
from pathlib import Path
import joblib
from app.core.config import MODEL_ROOT

TARGETS = ("cooler", "valve", "pump", "accumulator")
IMS_TESTS = ("1st_test", "2nd_test", "3rd_test")

def candidate_path(target: str) -> Path:
    return MODEL_ROOT / "experiment_02_hydraulic" / f"hydraulic_{target}_champion.joblib"

def ims_path(test: str) -> Path:
    return MODEL_ROOT / f"ims_{test}_iforest.joblib"

@lru_cache(maxsize=12)
def load_artifact(path_string: str):
    path = Path(path_string)
    if not path.is_file():
        raise FileNotFoundError(f"Model not found: {path}")
    # joblib uses pickle: only load YOUR trusted Kaggle-generated artifacts.
    return joblib.load(path)

def status() -> dict:
    return {
        "hydraulic": {target: candidate_path(target).is_file() for target in TARGETS},
        "ims": {test: ims_path(test).is_file() for test in IMS_TESTS},
        "model_directory": str(MODEL_ROOT),
    }
