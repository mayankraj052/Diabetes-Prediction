from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from joblib import load

app = Flask(__name__)

# Load the trained model
model = load('model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the form
        data = request.form

        # Create a DataFrame from the form input
        input_data = pd.DataFrame({
            'Age': [data['age']],
            'Gender': [data['gender']],
            'Polyuria': [data['polyuria']],
            'Polydipsia': [data['polydipsia']],
            'sudden weight loss': [data['sudden_weight_loss']],
            'weakness': [data['weakness']],
            'Polyphagia': [data['polyphagia']],
            'Genital thrush': [data['genital_thrush']],
            'visual blurring': [data['visual_blurring']],
            'Itching': [data['itching']],
            'Irritability': [data['irritability']],
            'delayed healing': [data['delayed_healing']],
            'partial paresis': [data['partial_paresis']],
            'muscle stiffness': [data['muscle_stiffness']],
            'Alopecia': [data['alopecia']],
            'Obesity': [data['obesity']]
        })

        # Make prediction
        prediction = model.predict(input_data)

        # Redirect to the result page with prediction
        return render_template('result.html', prediction=prediction[0])
    
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
