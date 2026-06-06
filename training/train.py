"""
Training script untuk YOLOv8 Face Detection
"""

import os
import sys
from pathlib import Path
import yaml
import torch
from ultralytics import YOLO
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import config
sys.path.insert(0, str(Path(__file__).parent.parent))
from config import TRAINING_CONFIG, RAW_DATA_DIR, TRAINED_MODELS_DIR

class YOLOv8TrainerFaceDetection:
    def __init__(self, model_variant='nano'):
        """
        Initialize YOLOv8 trainer
        
        Args:
            model_variant: Model size (nano, small, medium, large, xlarge)
        """
        self.model_variant = model_variant
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = None
        
        logger.info(f"Using device: {self.device}")
        
    def load_model(self):
        """Load YOLOv8 model"""
        try:
            model_name = f"yolov8{self.model_variant[0]}.pt"
            self.model = YOLO(model_name)
            logger.info(f"Model {model_name} loaded successfully")
        except Exception as e:
            logger.error(f"Error loading model: {e}")
            raise
    
    def prepare_dataset_yaml(self, dataset_path):
        """
        Prepare dataset.yaml for YOLOv8 training
        
        Args:
            dataset_path: Path to dataset directory
        """
        dataset_config = {
            'path': str(dataset_path),
            'train': 'images/train',
            'val': 'images/val',
            'test': 'images/test',
            'nc': 1,  # Number of classes (face)
            'names': ['face']
        }
        
        yaml_path = dataset_path / 'data.yaml'
        with open(yaml_path, 'w') as f:
            yaml.dump(dataset_config, f)
        
        logger.info(f"Dataset YAML created at {yaml_path}")
        return yaml_path
    
    def train(self, dataset_path, epochs=100, batch_size=16, imgsz=416):
        """
        Train YOLOv8 model
        
        Args:
            dataset_path: Path to dataset
            epochs: Number of training epochs
            batch_size: Batch size
            imgsz: Image size
        """
        if self.model is None:
            self.load_model()
        
        # Prepare dataset
        data_yaml = self.prepare_dataset_yaml(Path(dataset_path))
        
        try:
            # Train model
            results = self.model.train(
                data=str(data_yaml),
                epochs=epochs,
                imgsz=imgsz,
                batch=batch_size,
                device=self.device,
                patience=20,
                save=True,
                project=str(TRAINED_MODELS_DIR),
                name=f'yolov8{self.model_variant[0]}_face',
                exist_ok=True,
            )
            
            logger.info(f"Training completed successfully")
            return results
            
        except Exception as e:
            logger.error(f"Training error: {e}")
            raise
    
    def validate(self):
        """Validate trained model"""
        if self.model is None:
            raise ValueError("Model not loaded")
        
        try:
            metrics = self.model.val()
            logger.info(f"Validation metrics: {metrics}")
            return metrics
        except Exception as e:
            logger.error(f"Validation error: {e}")
            raise
    
    def predict(self, image_path, confidence=0.5):
        """
        Make prediction on image
        
        Args:
            image_path: Path to image
            confidence: Confidence threshold
        """
        if self.model is None:
            raise ValueError("Model not loaded")
        
        try:
            results = self.model.predict(
                source=image_path,
                conf=confidence,
                device=self.device
            )
            return results
        except Exception as e:
            logger.error(f"Prediction error: {e}")
            raise
    
    def export_model(self, export_format='onnx'):
        """
        Export model to different formats
        
        Args:
            export_format: Export format (onnx, torchscript, etc)
        """
        if self.model is None:
            raise ValueError("Model not loaded")
        
        try:
            exported_path = self.model.export(format=export_format)
            logger.info(f"Model exported to {exported_path}")
            return exported_path
        except Exception as e:
            logger.error(f"Export error: {e}")
            raise


def main():
    """Main training function"""
    
    # Initialize trainer
    trainer = YOLOv8TrainerFaceDetection(model_variant='nano')
    
    # Load model
    trainer.load_model()
    
    # Train model
    print("Starting training...")
    results = trainer.train(
        dataset_path=RAW_DATA_DIR.parent / 'dataset',
        epochs=TRAINING_CONFIG['epochs'],
        batch_size=TRAINING_CONFIG['batch_size'],
        imgsz=416
    )
    
    # Validate
    print("Validating model...")
    metrics = trainer.validate()
    
    # Export
    print("Exporting model...")
    trainer.export_model('onnx')
    
    logger.info("Training pipeline completed!")


if __name__ == "__main__":
    main()
