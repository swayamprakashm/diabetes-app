---

# 🩺 Diabetes Prediction Web App

A simple web application that predicts whether a person has diabetes or not based on user-provided health parameters using a trained machine learning model.

This app uses a Python backend (e.g., Flask) to serve an interface where users can enter health data and receive predictions in real time.

---

## 🚀 Features

✔ Predicts diabetes using a trained machine learning model  
✔ User-friendly web interface  
✔ Easy to run locally  
✔ Trained model stored separately (`model.pkl`)

---
## 🎥 Demo Video


https://github.com/user-attachments/assets/e0ebbf25-b36d-48f9-9c7d-f1dc4d5ab6ea

[Video File](assets/diabetes-app-vid.mp4)


---
## 📁 Project Structure

```

📦 diabetes-app
┣ 📂 static/
┣  ┣ styles.css
┣ 📂 templates/
┣  ┣ index.html
┣ 📂 assets/
┣  ┣ diabetes-app-vid.mp4
┣ 
┣ 📄 app.py
┣ 📄 train_model.py
┣ 📄 model.pkl
┣ 📄 requirements.txt
┣ 📄 README.md
```
---

## 🧠 How It Works

1. The user enters health details (e.g., glucose level, BMI, age) via the web interface.  
2. The backend loads the saved machine learning model (`model.pkl`).  
3. It predicts whether a person has diabetes (Yes/No).  
4. The result is shown on the result page.

*(This is a common setup for diabetes prediction projects using ML models — see similar examples on GitHub.)* :contentReference[oaicite:0]{index=0}

---

## 🛠️ Technologies Used

| Component | Technology |
|-----------|------------|
| Backend   | Python (Flask) |
| Model     | Machine Learning (Scikit-learn / Pickle) |
| Frontend  | HTML / CSS |
| Dependencies | Listed in `requirements.txt` |

---

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/swayamprakashm/diabetes-app.git
   cd diabetes-app
   ```

2. **Create and activate a Python virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the web app**

   ```bash
   python app.py
   ```

5. Open your browser and go to:

   ```
   http://127.0.0.1:5000/
   ```

---

## 🧪 Training Your Own Model

If you want to retrain the model:

```bash
python train_model.py
```

This script should take your dataset, preprocess it, train a model, and save it as `model.pkl`.

*(Make sure your dataset contains health metrics like glucose, BMI, age, etc.)* ([GitHub][1])

---

## 📈 Usage

After starting the app in your browser:

1. Fill in all required health parameters.
2. Click the **Predict** button.
3. View the prediction result on the output page.

---

## 📌 Contributing

Contributions are welcome!
To contribute:

1. Fork this repository.
2. Create your feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to your branch (`git push origin feature-name`).
5. Create a Pull Request.

---

## 📜 License

Add your license here (e.g., MIT License).

---

## 💬 Contact

Created by **Swayam Prakash** — feel free to reach out for questions or collaboration!

---

⭐ *Don’t forget to star this repository if you find it helpful!*

---
