import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

# Load data
data = pd.read_csv("../TW50.csv", usecols=["Date", "Price Index"])

# Convert Date column to datetime format
data["Date"] = pd.to_datetime(data["Date"])

# Extract quarter from Date column
data["Quarter"] = data["Date"].dt.quarter

print(data)
# Filter out weekends (Saturday and Sunday)
data = data[data["Date"].dt.dayofweek < 5]

# Create dummy variables for quarters
data = pd.get_dummies(data, columns=["Quarter"], drop_first=True)

# Change True to 1 and False to 0 in quarter dummy variables
data = data.astype(int)

# Prepare data for regression
X = data.drop(["Date", "Price Index"], axis=1)
y = data["Price Index"]

# Define the regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Forecast for the next 7 days (excluding weekends)
# current_date = data["Date"].max()  # Get the latest date from the data as a datetime object
current_date = pd.to_datetime(data["Date"].max(), unit='ns')  # Get the latest date from the data as a datetime object
forecast_dates = []
forecast_quarters = []
days_to_forecast = 0

# Calculate the next 7 weekdays for forecasting
while days_to_forecast < 5:
    current_date += timedelta(days=1)
    if current_date.weekday() < 5:
        forecast_dates.append(current_date)
        forecast_quarters.append(1 if current_date.month in [1, 2, 3] else 2 if current_date.month in [4, 5,
                                                                                                       6] else 3 if current_date.month in [
            7, 8, 9] else 4)
        days_to_forecast += 1

# Create dummy variables for forecast quarters
forecast_X = pd.DataFrame({
    "Quarter_2": [1] * 5,  # Set all values in Quarter_2 column to 1
    "Quarter_3": [0] * 5,  # Set all values in Quarter_3 column to 0
    "Quarter_4": [0] * 5   # Set all values in Quarter_4 column to 0
})

print(forecast_X)

# Predict the Price Index for the next 7 weekdays
forecasted_prices = model.predict(forecast_X)

# Display the forecasted prices
forecast_df = pd.DataFrame({"Date": forecast_dates, "Forecasted Price Index": forecasted_prices})
print(forecast_df)
