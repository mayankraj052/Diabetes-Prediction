# Diabetes Prediction Website

This web application is built using **Flask**, **HTML**, and a **Machine Learning Model** to predict whether a user is at risk of having diabetes. The user can input their health information, and the website will display a prediction based on a trained machine learning model.

## Features

- **Input Form**: Users can input their health-related details (e.g., age, BMI, glucose levels, etc.).
- **Prediction**: After submitting the form, the website uses a machine learning model to predict if the user has diabetes.
- **User-Friendly Interface**: Simple and responsive web design built with HTML and CSS.

## Technologies Used

- **Flask**: Python web framework to handle routes and backend logic.
- **HTML/CSS**: For the frontend UI.
- **Machine Learning**: A trained machine learning model to predict diabetes.
- **Virtual Environment**: To isolate project dependencies.

## Setup Instructions

Run the following commands step by step in one go to set up the project:

# 1. Clone the repository

git clone https://github.com/your-username/diabetes-prediction.git
cd diabetes-prediction

# 2. Create a virtual environment

python -m venv myenv

# 3. Activate the virtual environment

# For PowerShell

.\myenv\Scripts\Activate.ps1

# 4. Install dependencies

pip install flask numpy==1.26.4 pandas==2.2.2 joblib==1.4.2 scikit-learn==1.5.2 gunicorn

# 5. Run the Flask application

python app.py
**our website will be accessible at**: https://diabetes-prediction-college-project.onrender.com/
