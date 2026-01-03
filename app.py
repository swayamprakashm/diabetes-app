from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load trained model using absolute path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        glucose = float(request.form.get("glucose", 0))
        bmi = float(request.form.get("bmi", 0))
        age = float(request.form.get("age", 0))
    except ValueError:
        return render_template(
            "index.html",
            prediction=None,
            probability=None,
            risk_level=None
        )

    features = np.array([[glucose, bmi, age]])
    prob = model.predict_proba(features)[0][1]
    prediction = model.predict(features)[0]

    if prob >= 0.70:
        risk_level = "high"
    elif prob >= 0.40:
        risk_level = "moderate"
    else:
        risk_level = "normal"

    return render_template(
        "index.html",
        prediction=int(prediction),
        probability=f"{prob * 100:.2f}%",
        risk_level=risk_level
    )

