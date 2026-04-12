from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

from modules.predict import predict_crop
from modules.auto_test import generate_auto_test
from modules.pre_test import run_predefined_tests

app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Home
@app.route('/')
def home():
    return render_template('home.html')


# Predict
@app.route('/predict', methods=['POST'])
def predict():
    try:
        temp = float(request.form['Temperature'])
        rain = float(request.form['Rainfall'])
        hum = float(request.form['Humidity'])
        ph = float(request.form['Soil_pH'])
        user_crop = request.form['Crop'].lower()

        predicted = predict_crop(model, temp, rain, hum, ph)

        if user_crop == predicted.lower():
            result = "✔ Land is Suitable"
            suggestion = "Correct crop selected"
        else:
            result = "❌ Not Suitable"
            suggestion = f"Recommended Crop: {predicted}"

    except:
        result = "⚠️ Invalid Input!"
        suggestion = ""

    return render_template(
    'home.html',
    prediction_text=result,
    suggestion_text=suggestion,
    show_popup=True   # 👈 ADD THIS
)


# Auto Test
@app.route('/auto_test')
def auto_test():
    data = generate_auto_test(model)
    return jsonify(data)


# Predefined Test
@app.route('/pre_test')
def pre_test():
    data = run_predefined_tests(model)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)