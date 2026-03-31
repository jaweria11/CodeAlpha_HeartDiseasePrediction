#  Heart Disease Prediction System

A Machine Learning + Django-based web application that predicts the likelihood of heart disease based on user input parameters.



##  Project Overview

This project uses a trained **Machine Learning model (XGBoost)** to predict whether a person has a risk of heart disease or not. The model is integrated into a **Django web application**, where users can input medical data and get instant predictions.



##  Features

*  Predict heart disease (Yes / No)
*  Uses trained ML model (XGBoost)
*  Fast real-time prediction
* Interactive and modern UI
*  CSRF protection (Django security)
*  Scaler + Model integration

---

##  Machine Learning Details

* Algorithm: **XGBoost Classifier**
* Dataset: Heart Disease UCI Dataset
* Preprocessing:

  * Train/Test Split
  * Feature Scaling (StandardScaler)
* Output:

  * `0` → No Heart Disease
  * `1` → Heart Disease

---


##  Requirements

Make sure you have the following installed:

* Python (>= 3.8)
* Django
* NumPy
* Scikit-learn
* XGBoost
* Pandas

---

##  Installation

### 1 Clone the repository

```bash
git clone https://github.com/jaweria11/CodeAlpha_HeartDiseasePrediction
cd heart-disease-prediction
```

---

### 2 Create virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

---

### 3 Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Run the Project

```bash
python manage.py runserver
```

Open in browser:



---

##  Input Parameters

| Feature  | Description               |
| -------- | ------------------------- |
| Age      | Age of patient            |
| Sex      | 0 = Female, 1 = Male      |
| CP       | Chest Pain Type (0–3)     |
| Trestbps | Resting Blood Pressure    |
| Chol     | Cholesterol Level         |
| FBS      | Fasting Blood Sugar (0/1) |
| RestECG  | ECG Result (0–2)          |
| Thalach  | Max Heart Rate            |
| Exang    | Exercise Induced Angina   |
| Oldpeak  | ST Depression             |
| Slope    | Slope of Peak Exercise    |
| CA       | Number of Major Vessels   |
| Thal     | Thalassemia (1–3)         |

---

##  Model Files

* `heart_model.pkl` → Trained ML model
* `scaler.pkl` → StandardScaler used during training

 Both must be present in the project directory for predictions to work.

---

##  Example Output

*  No Heart Disease
*  Heart Disease Detected

---

##  UI Preview

Modern glass-style UI with animations and responsive layout.

---

##  Future Improvements

*  Show prediction probability (% risk)
*  Mobile responsive design
*  Graph visualization
*  Improve model accuracy


---

##  Author

Developed by **[Jaweria]**

---

##  Support

If you like this project:

*  Star the repo
*  Fork it
*  Share it

---

##  License

This project is for educational purposes.
