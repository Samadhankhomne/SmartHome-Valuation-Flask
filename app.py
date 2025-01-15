import numpy as np
import pickle
from flask import Flask, request, render_template

# Load the trained model
with open('House_price.pkl', 'rb') as file:
    model = pickle.load(file)

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input from the form
    try:
        sqft = float(request.form['sqft'])
        prediction = model.predict([[sqft]])
        price = f"Predicted House Price: ${prediction[0]:,.2f}"
    except ValueError:
        price = "Invalid input. Please enter a valid number."
    return render_template('index.html', prediction=price)

if __name__ == '__main__':
    app.run(debug=True)
