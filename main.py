from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
from skimage import io, transform, exposure
import numpy as np
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# 💡 CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # veya sadece frontend portun: ["http://localhost:5174"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model ve etiketleri yükle
model = load_model("model/model.keras")

with open("signnames.csv", "r") as f:
    labelNames = [line.strip().split(",")[1] for line in f.readlines()[1:]]

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()

    # Görseli oku ve yeniden boyutlandır
    image = io.imread(contents, plugin='imageio')
    image = transform.resize(image, (32, 32))
    image = exposure.equalize_adapthist(image, clip_limit=0.1)
    image = image.astype("float32") / 255.0
    image = np.expand_dims(image, axis=0)

    # Tahmin yap
    preds = model.predict(image)
    class_index = int(np.argmax(preds))
    confidence = float(preds[0][class_index]) * 100
    label = labelNames[class_index]

    return {
        "label": label,
        "confidence": f"{confidence:.2f}"
    }
