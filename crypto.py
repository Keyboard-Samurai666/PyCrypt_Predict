# Import Libraries
import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta

# Create the 'today' variable with the current date as it's value.
today = date.today()

# Use the strftime method to format the current date and store it as a string in the variable d1.
d1 = today.strftime("%Y-%m-%d")
# Set the value of end_date equal to d1.
end_date = d1
# Calculate 730 days (2 years) before the current date, and store it as a string in the variable d2 using the strftime method.
d2 = date.today() - timedelta(days=730)
d2 = d2.strftime("%Y-%m-%d")
# Set the value of end_date equal to d2
start_date = d2
# Retrieve historical data for BTC-USD pair between the start_date and the end_date using the yfinance library.
data = yf.download('BTC-USD', 
                   start=start_date, 
                   end=end_date, 
                   progress=False)
# Add a new column called "Date" to the data frame, and set its values equal to the index of the data frame.
data['Date'] = data.index
# Reorder the columns of the data frame to be ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"].
data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
# Reset the index of the data frame, dropping the old index and replacing it with a new sequential index starting at 0.
data.reset_index(drop=True, inplace=True)
# Print the first few rows of the data frame using the head method.
# print(data.head())
# Verify the dataframe has 730 rows
# print(data.shape)
# import the plotly graph objects
import plotly.graph_objects as go
# Create a Candlestick trace and specify which columns in the 'data' DataFrame should be used in the chart.
figure = go.Figure(data=[go.Candlestick(x=data["Date"],
                                        open=data["Open"], 
                                        high=data["High"],
                                        low=data["Low"], 
                                        close=data["Close"])])
# Update the layout of the chart and set chart Title to; "Bitcoin Price Analysis", and hiding the x-axis range slider.
figure.update_layout(title = "Bitcoin Price Analysis", 
                     xaxis_rangeslider_visible=False)
# Display the Chart
figure.show()
# The "Close" column in the dataset is the one we want to focus on to make predictions.
correlation = data.corr()
# print(correlation["Close"].sort_values(ascending=False))
# Import the AutoTS function from the autots library.
from autots import AutoTS
# Create and store an instance of the AutoTS Class in the 'model' variable.
model = AutoTS(forecast_length=30, 
               frequency='infer',
               ensemble='simple',)
# Fit the model to the 'data' dataset
model = model.fit(data, date_col='Date', value_col='Close', id_col=None)
# Predict
prediction = model.predict()
forecast = prediction.forecast
print(forecast)