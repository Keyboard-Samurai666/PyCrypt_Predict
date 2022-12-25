# Cryptocurrency Price Prediction using Python
---
## Step 1: **Import the necessary libraries**

- pandas

- yfinance (This is the Yahoo Finance API, it will collect the latest Bitcoin prices and serve as our dataset)

- datetime (as well as ```from datetime import date, timedelta```)

- plotly

- autots
---
## Step 2: **Collect latest data and prep the Dataset**

**Create the 'today' variable with the current date as it's value.**
```today = date.today()```

**Then covert the current date and store it as a string in the variable d1**
```d1 = today.strftime("%Y-%m-%d")```

**Create an end_date variable and set it's value equal to d1(current date)**
```end_date = d1```

**Calculate 2 years before d1 (current date) and convert it to a string using strftime method**
```d2 = date.today() - timedelta(days=730)```
```d2 = d2.strftime("%Y-%m-%d")```

**Then create the start_date variable with a value equal to d2**
```start_date = d2```

**Retreave historical data for 'BTC-USD' between the start_date(d2) and the end_date(current date) using the yfinance library, and store it in the 'data' variable.**

```type(data) == pandas.core.frame.DataFrame```

**Add a new column called "Date" to the data frame, and set its values equal to the index of the data frame.**

```data['Date'] = data.index```

**Reorder the columns of the data frame to be ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"].**

```data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]```

**Reset the index of the data frame, dropping the old index and replacing it with a new sequential index starting at 0.**

```data.reset_index(drop=True, inplace=True)```

**Print the first few rows of the data frame using the head method.**

```print(data.head())```

### Sample Output:

![Image not Found](https://scontent-atl3-2.xx.fbcdn.net/v/t39.30808-6/321792675_1202392977055850_5566260706950432521_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=730e14&_nc_ohc=VMuQWlpuFkMAX87p3FH&_nc_ht=scontent-atl3-2.xx&oh=00_AfDt8m-b4OOudneaktCY5lA8gdaKEm-z0fw9FmkPuDvO3Q&oe=63AC9CE3)

**We can check the 'shape' of the Dataset to verify if we are working with 730 rows or not using the shape method:**

**In:** ``print(data.shape)``

**Out:** ```(730, 7)```
---## Step 3: Visualize the change in Bitcoin Prices from 730 days(2 years) to today using a candlestick chart:

**Import the plotly graph object**

``import plotly.graph_objects as go``

**Create a Candlestick trace and specify which columns in the 'data' DataFrame should be used in the chart.**

```figure = go.Figure(data=[go.Candlestick(x=data["Date"], open=data["Open"], high=data["High"],low=data["Low"], close=data["Close"])])```

**Update the layout of the chart and set chart Title to; "Bitcoin Price Analysis", and hiding the x-axis range slider**

``figure.update_layout(title = "Bitcoin Price Analysis", xaxis_rangeslider_visible=False)``

**Display the Chart**

``figure.show()``

**Example:**

![Candlestick Chart](https://i0.wp.com/thecleverprogrammer.com/wp-content/uploads/2021/12/bitcoin-price-analysis.png?resize=768%2C348&ssl=1)


# The "Close" column in the dataset is the one we want to focus on to make predictions.

``correlation = data.corr()``

``print(correlation["Close"].sort_values(ascending=False))``

**Sample Output:**

![Output](https://photos.app.goo.gl/PPjC3vu4iKUWhTSQ8)
---
### Step 4: Building the Crypto Price Predition Model

**Predicting the price of Crypto depends on** __Time Series Analysis__ **This is a statistical technique for analyzing and modeling time-dependent data.**

**I will use the __AutoTS__ library to predict the Crypto Prices for the next 30 days:**

``from autots import AutoTs``

**Create an instance of the 'AutoTS' class and store it in the "model" variable**

``model = AutoTS(forecast_length=30, frequency='infer', ensemble='simple',)``

**Fit the model to the 'data' Dataset**

``model = model.fit(data, date_col='Date', value_col='Close', id_col=None)``

**Predict and print out the forecast to the console**

``prediction = model.predict()``
``forecast = prediction.forecast``
``print(forecast)``

### Disclamer:
***Buying and selling result in a change in the price of any cryptocurrency, but buying and selling trends depend on many factors. Using machine learning for cryptocurrency price prediction can only work in situations where prices change due to historical prices that people see before buying and selling their cryptocurrency.**
