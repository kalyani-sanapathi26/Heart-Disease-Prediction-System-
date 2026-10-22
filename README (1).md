# Heart Disease Prediction System

A web application built with **Python, Flask, and Machine Learning** to estimate whether the supplied patient measurements indicate a higher or lower chance of heart disease. The app accepts inputs through an HTML form and displays a prediction.

> **Medical disclaimer:** This project is for educational and demonstration purposes only. It is not a medical device and must not be used to diagnose, treat, or rule out heart disease. Consult a qualified healthcare professional for medical advice.

## Features

- Web interface built with HTML and CSS.
- Flask backend with a `/predict` route.
- Logistic Regression classification model from scikit-learn.
- Reads a heart-disease CSV dataset and trains the model.
- Displays one of two messages: `High chance of Heart Disease` or `Low chance of Heart Disease`.

## Technologies Used

- Python
- Flask
- pandas
- scikit-learn
- HTML
- CSS
- Pickle (to save the trained model)

## Project Structure

```text
heartdiseaseproject/
├── app.py
├── heart (1).csv
├── model.pkl
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── heartdiseaseproject.code-workspace
└── README.md
```

## Dataset

The included CSV file has **1,025 rows and 14 columns**. It contains 13 input features and a `target` column used as the classification label.

The feature columns are:

`age`, `sex`, `cp`, `trestbps`, `chol`, `fbs`, `restecg`, `thalach`, `exang`, `oldpeak`, `slope`, `ca`, and `thal`.

The `target` column is the value the model learns to predict. Check the dataset's original source and license before redistributing it.

## Setup and Run

### 1. Install Python

Install a supported Python 3 version if it is not already installed.

### 2. Clone the repository

```bash
git clone https://github.com/kalyani-sanapathi26/Heart-Disease-Prediction-System-.git
cd Heart-Disease-Prediction-System-
```

### 3. Create and activate a virtual environment (recommended)

On Windows (Git Bash):

```bash
python -m venv .venv
source .venv/Scripts/activate
```

On Windows (Command Prompt):

```bat
python -m venv .venv
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install flask pandas scikit-learn
```

### 5. Check the dataset path in `app.py`

The current code uses a Windows-specific absolute path to the CSV file. To make it work after cloning the repository, change:

```python
data = pd.read_csv(r"C:\Users\Hemanth\Desktop\heartdiseaseproject\heart (1).csv")
```

to this project-relative path:

```python
data = pd.read_csv("heart (1).csv")
```

Run the app from the project root directory so the CSV file can be found.

### 6. Start the application

```bash
python app.py
```

Open the local URL printed by Flask in your terminal (typically `http://127.0.0.1:5000/`).

The application trains a Logistic Regression model when `app.py` runs, saves it as `model.pkl`, and then uses the model for predictions.

## How It Works

1. The application reads the CSV dataset with pandas.
2. The `target` column is separated from the input features.
3. A Logistic Regression model is trained with scikit-learn.
4. The trained model is saved to `model.pkl`.
5. Flask serves the home page and receives submitted form values at `/predict`.
6. The model predicts a class and the page displays the result.

## Future Improvements

- Use a reproducible train/test split and report appropriate evaluation metrics.
- Validate form inputs and handle missing or invalid values.
- Add a clear explanation of the prediction's limitations.
- Use a configurable, project-relative dataset path.
- Avoid enabling Flask debug mode in a production deployment.
- Add automated tests and a dependency file such as `requirements.txt`.

## Author

**Kalyani Sanapathi**

---

If you use or adapt this project, review the dataset's source and licensing terms and do not present model predictions as a medical diagnosis.
