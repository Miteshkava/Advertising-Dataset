from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model safely
with open('advertisement_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            TV = float(request.form['TV'])
            Radio = float(request.form['Radio'])
            Newspaper = float(request.form['Newspaper'])
            
            # Ensure model input is a 2D array
            features = np.array([[TV, Radio, Newspaper]])
            prediction = model.predict(features)
            output = round(prediction[0], 2)
            
            return render_template('index.html', pred=f"Predicted Sales: {output}")
        except Exception as e:
            return render_template('index.html', pred=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
