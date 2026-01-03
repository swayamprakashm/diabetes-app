import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression

url = "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv"
df = pd.read_csv(url)

X = df[["Glucose", "BMI", "Age"]]
y = df["Outcome"]

model = LogisticRegression()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved as model.pkl")
