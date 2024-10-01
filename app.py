from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('google_stock_prediction_model.pkl')

# Route to serve the home page
@app.route('/')
def home():
    return render_template('index.html')

# API to predict stock prices based on the Open price
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    open_price = data['Open']  # Get the Open price input from the user

    # Prepare the data in the right format for prediction
    input_data = np.array([[open_price]])

    # Make the prediction
    prediction = model.predict(input_data)

    # Return the prediction result
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True, port=5002)