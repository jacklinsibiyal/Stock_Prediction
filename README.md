# Stock Price Prediction App

## Overview

This project is a **stock price prediction web application** that uses historical stock data to predict future stock prices. It allows users to input a date, fetches the **Open**, **High**, and **Low** prices for that day using the `yfinance` API, and then uses a machine learning model to predict the stock's **Adjusted Close** price.

The model is trained using Google's stock data (`GOOGL`) from 2004-08-19 to the present day and uses **Linear Regression** for predictions based on the **Open**, **High**, and **Low** prices of the day.

## Features

- **Date-Based Input**: Users can select a date, and the app fetches the stock prices for that specific day.
- **Prediction**: Predicts the stock's adjusted closing price using the provided stock data.
- **Automated Data Fetching**: Automatically fetches stock prices from Yahoo Finance based on the date entered by the user.
- **Pre-Trained Model**: No need to retrain the model; it predicts based on the input provided.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Machine Learning**: Linear Regression (with `sklearn`)
- **Data Source**: `yfinance` for fetching real-time and historical stock data.
- **Model Storage**: `joblib` for loading the model.

## How It Works

1. The user enters a date on the web page.
2. The backend fetches the stock's **Open**, **High**, and **Low** prices for that specific date using `yfinance`.
3. The **Linear Regression** model predicts the **Adjusted Close** price based on the fetched data.
4. The predicted stock price is displayed to the user.

## Installation

### Prerequisites

- Python 3.x
- Flask
- `yfinance` library
- `scikit-learn`
- `joblib`

### Step-by-Step Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository/stock-price-prediction-app.git
   cd stock-price-prediction-app
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the Model**: Use the `stock_prediction.ipynb` notebook to train the model:
   - Open the notebook and run all cells to train the model.
   - The trained model will be saved as `google_stock_prediction_model.pkl`.

5. **Run the App**:
   ```bash
   python app.py
   ```

6. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure

```
├── app.py                        
├── stock_prediction.ipynb         
├── google_stock_prediction_model.pkl 
├── google_stock_data.csv           
├── templates
│   └── index.html                
├── static
│   ├── style.css                   
│   └── script.js                   
└── README.md                   
```

## Usage

- Input a **date** in the **YYYY-MM-DD** format.
- The application will fetch the stock's **Open**, **High**, and **Low** prices for that date.
- The app will then predict the stock's **Adjusted Close** price based on the provided information.

## License

This project is licensed under the MIT License. Feel free to modify and distribute.
