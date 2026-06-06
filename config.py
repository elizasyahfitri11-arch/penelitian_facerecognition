import os
from pathlib import Path

# Project Root Directory
PROJECT_ROOT = Path(__file__).resolve().parent

# Data Directories
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

# Models Directories
MODELS_DIR = PROJECT_ROOT / "models"
TRAINED_MODELS_DIR = MODELS_DIR / "trained_models"
TRAINED_MODELS_DIR.mkdir(parents=True, exist_ok=True)

# Training Configuration
TRAINING_CONFIG = {
    "model_name": "yolov8n",
    "epochs": 100,
    "batch_size": 16,
    "learning_rate": 0.001,
    "device": "cuda",
}

# Face Detection Algorithms
ALGORITHMS = {
    "yolov8": {"name": "YOLOv8", "confidence_threshold": 0.5},
    "mtcnn": {"name": "MTCNN", "min_face_size": 20},
    "retinaface": {"name": "RetinaFace", "confidence_threshold": 0.8},
}

# Evaluation Metrics
EVALUATION_METRICS = {
    "precision": {"target": 0.95},
    "recall": {"target": 0.95},
    "accuracy": {"target": 0.99},
    "f1_score": {"target": 0.97},
}