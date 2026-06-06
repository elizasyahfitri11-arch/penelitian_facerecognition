# 🎯 Face Detection Attendance System dengan YOLOv8

Sistem deteksi wajah untuk presensi pengunjung perpustakaan menggunakan YOLOv8 dengan target akurasi 99%.

## 📋 Project Overview

**Objective:**
- Membuat aplikasi web untuk deteksi wajah dan presensi otomatis
- Training model YOLOv8 dengan custom dataset
- Evaluasi model dengan hyperparameter tuning
- Target akurasi: 99%

**Tech Stack:**
- **Backend:** Python, Flask
- **ML Model:** YOLOv8 (Ultralytics)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Deployment:** Google Colab (Training), Web Server

## 📁 Project Structure

```
penelitian_facerecognition/
├── data/
│   ├── raw/                      # Raw data dari capture wajah
│   ├── processed/                # Data yang sudah pre-processed
│   └── dataset_info.csv          # Info: nama, jenis_kelamin, npm, program_studi
├── models/
│   ├── yolov8_models/            # Pre-trained YOLOv8 models
│   └── trained_models/           # Custom trained models
├── training/
│   ├── train.py                  # Script training
│   ├── evaluate.py               # Script evaluasi
│   └── compare_algorithms.py     # Perbandingan algoritma
├── notebooks/
│   ├── 01_data_collection.ipynb  # Jupyter notebook data collection
│   ├── 02_training.ipynb         # Jupyter notebook training
│   └── 03_evaluation.ipynb       # Jupyter notebook evaluasi
├── web_app/
│   ├── app.py                    # Flask main app
│   ├── templates/
│   ├── static/
│   └── utils/
├── requirements.txt
├── config.py
└── .gitignore
```

## 🚀 Quick Start

### 1. Setup Environment
```bash
git clone https://github.com/elizasyahfitri11-arch/penelitian_facerecognition.git
cd penelitian_facerecognition
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Data Collection (Google Colab)
- Gunakan notebook: `notebooks/01_data_collection.ipynb`
- Target: 50-100 foto per person

### 3. Training Model (Google Colab)
- Gunakan notebook: `notebooks/02_training.ipynb`

### 4. Evaluasi & Comparison
- Gunakan notebook: `notebooks/03_evaluation.ipynb`

## 📊 Target Metrics
- Precision: ≥ 95%
- Recall: ≥ 95%
- Accuracy: ≥ 99%
- F1-Score: ≥ 97%

## 🔧 Algoritma Perbandingan
1. YOLOv8
2. MTCNN
3. RetinaFace
