from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
import numpy as np
from PIL import Image
from io import BytesIO

app = FastAPI()

model = tf.keras.models.load_model("best_model.h5")

def preprocess_image(image):
    image = image.resize((32, 32), Image.ANTIALIAS)
    image = np.array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image

class_names = [
    "airplane", "automobile", "bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck"
]

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(BytesIO(await file.read()))
    preprocessed_image = preprocess_image(image)
    prediction = model.predict(preprocessed_image)
    predicted_index = np.argmax(prediction)
    predicted_class_name = class_names[predicted_index]  # Get the class name using the predicted index
    return {"predicted_class": predicted_class_name}



