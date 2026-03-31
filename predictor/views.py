from django.shortcuts import render
import pickle
import numpy as np

# ✅ Load model
with open('predictor/heart_model.pkl', 'rb') as f:
    model = pickle.load(f)

# ✅ Load scaler
with open('predictor/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)


def home(request):
    prediction = None

    if request.method == "POST":
        try:
            age = float(request.POST['age'])
            sex = float(request.POST['sex'])
            cp = float(request.POST['cp'])
            trestbps = float(request.POST['trestbps'])
            chol = float(request.POST['chol'])
            fbs = float(request.POST['fbs'])
            restecg = float(request.POST['restecg'])
            thalach = float(request.POST['thalach'])
            exang = float(request.POST['exang'])
            oldpeak = float(request.POST['oldpeak'])
            slope = float(request.POST['slope'])
            ca = float(request.POST['ca'])
            thal = float(request.POST['thal'])

            features = [[
                age, sex, cp, trestbps, chol,
                fbs, restecg, thalach, exang,
                oldpeak, slope, ca, thal
            ]]

            # ✅ Apply scaling
            features = scaler.transform(features)

            result = model.predict(features)[0]

            # ✅ User-friendly output
            if result == 1:
                prediction = "⚠️ Heart Disease Detected"
            else:
                prediction = "✅ No Heart Disease"

        except:
            prediction = "❌ Invalid Input! Please enter all values correctly."

    return render(request, 'predictor/home.html', {'prediction': prediction})