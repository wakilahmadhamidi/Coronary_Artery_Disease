from flask import Flask, request, render_template  
import joblib
import pandas as pd  
import numpy as np  
app = Flask(__name__)  
model = joblib.load('CAD Model.pkl')  
@app.route('/')  
def home():  
    return render_template("index.html")
@app.route("/predict", methods=["POST"])  
def predict(): 
    age = request.form["age"]  
    sex = request.form["sex"]  
    chest_pain_type = request.form["chest pain type"]  
    resting_bps = request.form["resting bp s"]
    cholesterol = request.form["cholesterol"]  
    fasting_blood_sugar = request.form["fasting blood sugar"]  
    resting_ecg = request.form["resting ecg"]  
    max_heart_rate = request.form["max heart rate"]  
    exercise_angina = request.form["exercise angina"]  
    oldpeak = request.form["oldpeak"]  
    ST_slope = request.form["ST slope"]   
    arr = np.array([[age, sex, chest_pain_type, resting_bps, cholesterol,
       fasting_blood_sugar, resting_ecg, max_heart_rate,
       exercise_angina, oldpeak, ST_slope]])  
    pred = model.predict(arr)  
    if pred == 0:  
        res_val = "No Coronary Artery Disease"  
    else:  
        res_val = "Coronary Artery Disease"  
    return render_template('index.html', prediction_text='The Patient Has {}'.format(res_val))  

if __name__ == "__main__":  
    app.run(debug=True) 