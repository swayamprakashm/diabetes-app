from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

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
        return render_template("index.html",
                               prediction=None,
                               probability=None,
                               risk_level=None)

    features = np.array([[glucose, bmi, age]])
    prob = model.predict_proba(features)[0][1]  # probability of diabetes
    prediction = model.predict(features)[0]

    # Classify by probability
    if prob >= 0.70:
        risk_level = "high"
    elif prob >= 0.40:
        risk_level = "moderate"
    else:
        risk_level = "normal"

    return render_template(
        "index.html",
        prediction=int(prediction),
        probability=f"{prob*100:.2f}%",  # formatted as percentage
        risk_level=risk_level
    )

if __name__ == "__main__":
    app.run(debug=True)
