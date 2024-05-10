import pandas as pd
from pmdarima.arima import auto_arima

# Load the CSV file with the specified date format
file_path = "../FTSE TWSE Taiwan 50 Index.csv"
data = pd.read_csv(file_path, usecols=['Date', 'Price Index'], parse_dates=['Date'], date_parser=lambda x: pd.to_datetime(x, format='%Y/%m/%d'))

# Filter data from 26 April 2024 onwards
start_date = pd.to_datetime('2024-05-09', format='%Y-%m-%d')
filtered_data = data[data['Date'] >= start_date]

# Check if filtered data is not empty
if not filtered_data.empty:
    # Create the auto ARIMA model
    model = auto_arima(filtered_data['Price Index'], seasonal=False, trace=True)

    # Forecast the next 5 business days
    next_business_days = pd.date_range(start=start_date, periods=5, freq='B')
    forecast, conf_int = model.predict(n_periods=5, return_conf_int=True)

    # Create a DataFrame for the forecast
    forecast_df = pd.DataFrame({'Date': next_business_days, 'Forecast': forecast, 'Lower': conf_int[:, 0], 'Upper': conf_int[:, 1]})
    forecast_df.set_index('Date', inplace=True)

    # Print or save the forecast DataFrame
    print(forecast_df)
else:
    print("No data available for forecasting.")
