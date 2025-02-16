# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import os
from autots import AutoTS

# For linear regression
from sklearn.linear_model import LinearRegression  # For linear regression
import numpy as np

# Streamlit app setup
st.title("Exchange Rate Forecast")

# Set the path to the finances.csv file
file_path = "euro.csv"

# Check if the file exists
if os.path.isfile(file_path):
    # Load the data
    data = pd.read_csv(file_path)
    st.write("Data Preview", data.head())
    st.write(f"Data Shape: {data.shape}")
else:
    # Upload data file if the automatic file loading fails
    uploaded_file = st.file_uploader("Upload a CSV file with your expense data", type="csv")
    if uploaded_file is not None:
        # Load the data
        data = pd.read_csv(uploaded_file)
        st.write("Data Preview", data.head())
        st.write(f"Data Shape: {data.shape}")
    else:
        st.info("Please upload a CSV file to begin training.")

if 'data' in locals():
    # Ensure US column is numeric
    data['US'] = pd.to_numeric(data['US'], errors='coerce')
    
    # Drop any rows with missing data in key columns
    data.dropna(subset=['Date', 'US'], inplace=True)
    
    # Sort data by Date to ensure chronological order
    data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
    data = data.sort_values(by='Date')
    
    # Display basic statistics
    st.write("Processed Data", data.head())
    st.write(data.describe())

    # Convert dates to ordinal for regression
    data['Date_ordinal'] = data['Date'].map(pd.Timestamp.toordinal)

    # Initialize and fit linear regression model
    X = data[['Date_ordinal']]
    y = data['US']
    linear_model = LinearRegression()
    linear_model.fit(X, y)
    
    # Generate linear regression line
    regression_line = linear_model.predict(X)
    
    # Plot historical data with linear regression line
    # Results in 1900x600 pixels
    plt.figure(figsize=(19, 6), dpi=100)  
    plt.plot(data['Date'], data['US'], label='Historical Exchange Rate', color='blue')
    plt.plot(data['Date'], regression_line, label='Linear Regression Line', color='red', linestyle='--')
    plt.xlabel("Date")
    plt.ylabel("US")
    plt.title("Exchange Rate with Linear Regression Line")
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
    
    # Input for forecast length
    forecast_length = st.slider("Select Forecast Length (in Months)", 
    min_value=6, max_value=24, value=12, step=1)

    # Initialize AutoTS model
    model = AutoTS(forecast_length=forecast_length, 
    frequency='M', 
    prediction_interval=0.9,
    transformer_list="fast",
    drop_most_recent=0,
    no_negatives=True ,
    constraint=2.0 , 
    max_generations=10,
    num_validations=0,
    model_list = ["ARIMA", "FBProphet", "ETS"],
    n_jobs=4,
    min_allowed_train_percent=0.9,
    validation_method='seasonal 168',    
    ensemble="all")
    
    # Fit the model
    model = model.fit(data, date_col='Date', value_col='US', id_col=None)
    
    # Generate prediction and retrieve forecast
    prediction = model.predict()
    forecast = prediction.forecast

    # Display forecast data
    st.write("Forecast Data Preview", forecast)

    # Generate future dates for forecast plotting
    last_date = data['Date'].max()
    
    # Start from the last existing date
    future_dates = pd.date_range(last_date, periods=forecast_length + 1, freq='M')[1:]
    
    
    # Adjust forecast to remove y-axis offset
    # Last value in the historical data
    last_historical_value = data['US'].iloc[-1]

    # Align first forecast point
    forecast['US'] = forecast['US'] + (last_historical_value - forecast['US'].iloc[0])
    forecast.index = future_dates

    # Plot forecast data on the same diagram
    plt.plot(forecast.index, forecast['US'], label='Forecast', color='green', linestyle='--')
    
    # Display final plot with forecast included
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
