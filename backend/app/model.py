# app/model.py
import tensorflow as tf
from pathlib import Path
from app.utils import preprocess_image_for_model, draw_prediction_on_image

MODEL_PATH = Path("models/face_mask_detect.keras")
IMG_SIZE = 128

# Load model at startup
print("Loading model...")
model = tf.keras.models.load_model(MODEL_PATH)
print("Model loaded successfully!")

def predict_mask(image_bytes: bytes):
    """Main prediction function"""
    # Preprocess
    original_img, input_tensor = preprocess_image_for_model(image_bytes, IMG_SIZE)
    
    # Predict
    pred = model.predict(input_tensor, verbose=0)[0][0]
    
    if pred < 0.5:
        label = "With Mask"
        confidence = (1 - pred) * 100
    else:
        label = "Without Mask"
        confidence = pred * 100
    
    # Draw on image
    result_img = draw_prediction_on_image(original_img, label, confidence)
    
    return result_img, label, float(confidence)