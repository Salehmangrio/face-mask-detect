# app/main.py
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse
import io
import cv2
from app.model import predict_mask

app = FastAPI(
    title="Face Mask Detection API",
    description="Detects mask usage using custom CNN model",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "message": "Face Mask Detection API is running",
        "endpoints": {
            "/predict": "Returns image with bounding box",
            "/predict/json": "Returns JSON response"
        }
    }

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    try:
        image_bytes = await file.read()
        result_img, label, confidence = predict_mask(image_bytes)
        
        # Convert to JPEG bytes
        _, buffer = cv2.imencode('.jpg', result_img, [cv2.IMWRITE_JPEG_QUALITY, 95])
        img_bytes = io.BytesIO(buffer.tobytes())
        
        return StreamingResponse(
            img_bytes, 
            media_type="image/jpeg",
            headers={
                "X-Prediction": label,
                "X-Confidence": f"{confidence:.2f}"
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")


@app.post("/predict/json")
async def predict_json(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    try:
        image_bytes = await file.read()
        _, label, confidence = predict_mask(image_bytes)
        
        return {
            "prediction": label,
            "confidence": round(confidence, 2),
            "success": True
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))