from fastapi import FastAPI,File
from fastapi.datastructures import UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
from tensorflow.keras.models import load_model
from fastapi.middleware.cors import CORSMiddleware
MODEL =load_model('models/potatoModel/potatoModel.h5')
class_names=['Early_Blight' , 'Late_Blight' , 'Healthy']
app= FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

def read_file_as_image(data) -> np.ndarray:
    image=np.array(Image.open(BytesIO(data)))
    return image

@app.post("/predictions/") 
async def predict(file: UploadFile = File(...)):
    
    return {"filename": file.filename}

@app.post("/apk")
async def g(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    image_batch=np.expand_dims(image,0)
    # print(image)
    predictions=MODEL.predict(image_batch)
    final_prediction=class_names[np.argmax(predictions[0])]
    print(final_prediction)
    return {"prediction":final_prediction}