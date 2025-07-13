from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)
model = load_model("cats_vs_dogs_model.keras")

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No image uploaded'})

    file = request.files['file']
    img = image.load_img(file, target_size=(160, 160))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    pred = model.predict(img_array)[0][0]
    label = 'Dog' if pred > 0.5 else 'Cat'
    return jsonify({'prediction': label, 'confidence': float(pred)})

# ❌ No app.run(...) here
