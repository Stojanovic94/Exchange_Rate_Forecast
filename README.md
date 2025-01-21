# Exchange Rate Forecast
Exchange Rate Forecast using forecasting models such as ARIMA, ETS, and FBProphet.

---
## Overview
This project aims to analyze and predict the exchange rate between the Euro (EUR) and the US Dollar (USD) using historical exchange rate data.

---
## Dataset
This project utilizes the **Euro Exchange Daily Rates** dataset, which contains daily exchange rates between the Euro and various currencies from 04 Jan 1999 - 27 Sept 2024. The dataset is sourced from Kaggle and can be accessed at the following link: [Euro Exchange Daily Rates (1999-2020)](https://www.kaggle.com/datasets/lsind18/euro-exchange-daily-rates-19992020).

---
### Dataset Overview
- **Date Range**: The dataset includes daily exchange rates from 04 Jan 1999 - 27 Sept 2024.
- **Columns**:
  - **Date**: The date of the exchange rate.
  - **Currency**: The currency against which the Euro exchange rate is provided.
  - **Exchange Rate**: The value of one Euro in the corresponding currency.

---
### How to Use
To use this dataset in your project, ensure that the data file is in CSV format and located in the appropriate directory. 
```bash
pip install -r requirements.txt
```
```bash
streamlit run exchange_rate_forecast.py
```
Once the application is running, it will automatically open in your web browser at  ```http://localhost:8501```.


![Prediction shown for 1 year](images/image.png) -OLD-
The model forecasts exchange rate for a period of one year, providing insights into expected financial trends.



## Recommended Dataset Size
![Prediction shown for 1 year](images/image1.png)
For the most accurate and reliable predictions, it is recommended to use datasets that are **no longer than 5 years**. Longer datasets may introduce outdated patterns that could reduce the forecasting accuracy, especially when the data trends and seasonality patterns have changed. Using a dataset with recent data (less than 5 years) ensures that the model is focused on current trends, leading to better predictions for short to medium-term forecasting.

---

## Limitations for Cryptocurrency Forecasting

While AutoTS is a powerful tool for general time series forecasting, it may not be the best choice for **cryptocurrency forecasting** due to the following reasons:

1. **High Volatility**:  
   Cryptocurrencies experience significant volatility with frequent and unpredictable price swings. The chaotic nature of crypto markets makes it harder for models like ARIMA, ETS, and even machine learning methods to effectively capture trends and make accurate forecasts over time.

2. **Market Shocks and Sudden Movements**:  
   Cryptocurrencies can experience sudden price jumps or drops due to news, government regulations, or investor sentiment. These events introduce noise that traditional models often fail to account for, making forecasting difficult.

3. **Short-Term Unpredictability**:  
   Crypto markets can change drastically in a very short period of time, and past data may not always be relevant. A model trained on historical data may not be able to predict sudden changes or new trends that emerge in the market.

4. **Outlier Data Points**:  
   In cryptocurrency datasets, you may encounter extreme outliers—such as large price fluctuations due to pump-and-dump schemes—that can skew the predictions and lead to less reliable results.


---

## Using AutoTS
AutoTS (Automated Time Series) is a Python library designed to simplify and optimize the process of time series forecasting. It automates model selection, hyperparameter tuning, and ensembling, making it ideal for beginners and professionals looking to streamline their forecasting workflows.
 AutoTS abstracts away much of the complexity of time series forecasting. With a few lines of code, you can test multiple models and identify the best one based on performance metrics.

---

## Models Used  

### 1. ARIMA (AutoRegressive Integrated Moving Average)  
The ARIMA model combines three components:  
- **AR (AutoRegressive)**: Relates current observations to previous ones.  
- **I (Integrated)**: Makes the series stationary via differencing.  
- **MA (Moving Average)**: Models the relationship between current and previous error terms.

#### ARIMA Formula:  
**Y_t = φ₁Y_{t-1} + φ₂Y_{t-2} + ... + φₚY_{t-p} + θ₁ε_{t-1} + θ₂ε_{t-2} + ... + θₓε_{t-q} + ε_t**  

Where:  
- **Y_t**: Value at time `t`.  
- **φ₁, φ₂, ..., φₚ**: Autoregressive coefficients.  
- **θ₁, θ₂, ..., θₓ**: Moving average coefficients.  
- **ε_t**: Error term at time `t`.  

ARIMA is defined as **ARIMA(p, d, q)**, where:  
- **p**: Lag order.  
- **d**: Degree of differencing.  
- **q**: Order of the moving average.

---

### 2. ETS (Error, Trend, Seasonality)  
ETS is a framework for exponential smoothing models that incorporate:  
- **Error (E)**: Additive or multiplicative error term.  
- **Trend (T)**: Captures trends over time.  
- **Seasonality (S)**: Accounts for recurring patterns.

#### ETS Formula:  
The general ETS model is expressed as:  
**Y_t = [Level_t + Trend_t + Seasonality_t] × Error_t**

Where:  
- **Level_t**: Smoothed average at time `t`.  
- **Trend_t**: Trend component.  
- **Seasonality_t**: Seasonal effect.  
- **Error_t**: Residual/error term.

---

### 3. FBProphet  
FBProphet, developed by Meta, is a robust forecasting tool that handles irregular data and strong seasonality. It models:  
- **Trend**: Captures long-term increases or decreases.  
- **Seasonality**: Accounts for periodic patterns.  
- **Holiday Effects**: Adjusts for specific dates.

#### FBProphet Formula:  
**y(t) = g(t) + s(t) + h(t) + ε_t**

Where:  
- **g(t)**: Trend function for non-periodic changes.  
- **s(t)**: Periodic seasonal component.  
- **h(t)**: Effects of holidays.  
- **ε_t**: Error term.

---

# Conclusion

This project is currently in the testing phase. The aim is to analyze and predict the EUR/USD exchange rate using various statistical and machine learning techniques. 
