from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib
import yfinance as yf
from datetime import datetime, timedelta

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('google_stock_prediction_model.pkl')

# Function to fetch stock data from yfinance
def get_stock_data(date):
    # Add one day to the 'end' date because yf.download excludes the 'end' date
    end_date = (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
    
    # Fetch the stock data for the given date using yfinance
    stock_data = yf.download('GOOGL', start=date, end=end_date)
    
    if stock_data.empty:
        return None  # If no data is found for that date, return None
    
    open_price = stock_data['Open'][0]
    high_price = stock_data['High'][0]
    low_price = stock_data['Low'][0]
    return open_price, high_price, low_price

# Route to serve the home page
@app.route('/')
def home():
    return render_template('index.html')

# API to predict stock prices based on the date
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    date = data['Date']  # Get the date input from the user

    # Fetch the stock data for the provided date
    stock_data = get_stock_data(date)
    if stock_data is None:
        return jsonify({'error': 'No data available for the given date'}), 404

    open_price, high_price, low_price = stock_data

    # Prepare the data in the right format for prediction
    input_data = np.array([[open_price, high_price, low_price]])
    
    # Make the prediction
    prediction = model.predict(input_data)

    # Return the prediction result
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)