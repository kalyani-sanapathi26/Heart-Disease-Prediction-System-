import pandas as pd
from flask import Flask, render_template, request
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
data = pd.read_csv(r"C:\Users\Hemanth\Desktop\heartdiseaseproject\heart (1).csv")

# Features & target
X = data.drop("target", axis=1)
y = data["target"]

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

# Flask app
app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    values = [float(x) for x in request.form.values()]
    prediction = model.predict([values])

    if prediction[0] == 1:
        result = "High chance of Heart Disease"
    else:
        result = "Low chance of Heart Disease"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)