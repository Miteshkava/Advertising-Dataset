pip install Flask
from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

app = Flask(__name__)

# Load model
model = pickle.load(open('advertisement_regression_model.pkl', 'rb'))

with open('advertisement_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        TV = float(request.form['TV'])
        Radio = float(request.form['Radio'])
        Newspaper = float(request.form['Newspaper'])
        
        prediction = model.predict([[TV, Radio, Newspaper]])
        output = round(prediction[0], 2)
        
        pred = f"Predicted Sales: {output}"
        return render_template('index.html', pred=pred)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

