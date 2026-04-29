# app/utils.py
import cv2
import numpy as np

def preprocess_image_for_model(image_bytes: bytes, img_size: int = 128):
    """Preprocess image for model prediction"""
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if img is None:
        raise ValueError("Could not decode image")
    
    # Convert to RGB and resize
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    resized = cv2.resize(rgb_img, (img_size, img_size))
    
    # Normalize (same as training)
    normalized = resized.astype(np.float32) / 255.0
    input_tensor = np.expand_dims(normalized, axis=0)
    
    return img, input_tensor  # Return original for drawing + processed tensor


def draw_prediction_on_image(image, label: str, confidence: float):
    """Draw bounding box and label on image"""
    color = (0, 255, 0) if "With Mask" in label else (0, 0, 255)
    
    # Face detection using Haar Cascade
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 3)
        text = f"{label} ({confidence:.1f}%)"
        cv2.putText(image, text, (x, y - 10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    
    # If no face detected, put text at top
    if len(faces) == 0:
        text = f"{label} ({confidence:.1f}%)"
        cv2.putText(image, text, (30, 50), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)
    
    return image