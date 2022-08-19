# For cleaning data
import pandas as pan
# For getting eth prices
import yfinance as finace
from datetime import datetime
from datetime import timedelta

import plotly.graph_objects as plot

from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly,plot_components
import warnings


# Input = int(input("How many days you want to see ahead ?"))
Input = 365

# warnings.filterwarnings('ignore')
# Display prices in usd and 2 numbers after coma
pan.options.display.float_format = '${:,.2f}'.format

today_date = datetime.today().strftime('%Y-%m-%d')
# The first date where we can get Eth price info
start_date = '2017-11-09'

Eth_data = finace.download("ETH-USD",start = start_date,end = today_date)

# Using Eth_data.columns we can see that we dont have a date columns so we need to index it == reseting index to count from first row
Eth_data.reset_index(inplace = True)       # Change the Eth_ data

# We need just tha date and open price
data = Eth_data[["Date", "Open"]]          # We use [[]] to return a panda dataframe in a (m,n) format // [] will return a serie in (n) format

# We need to rename the columns for prophet later
data.rename(columns = {"Date":"ds","Open":"y"}, inplace = True)

# Let's make our graph
# Setting up Xes and Yes and the mode of the Graph
# Graph = plot.Figure(data=[plot.Scatter(
#     x = data["ds"],
#     y = data["y"],
#     mode = "lines",)
# ])
# # Adding a title 
# Graph.update_layout(
#     title_text="Etherium Open Price Plot",
# )
# Graph.update_layout(
#     xaxis=dict(
#         rangeselector=dict(
#             buttons=list(
#                 [
#                     dict(count=1, label="1D", step="day", stepmode="backward"),
#                     dict(count=1, label="1m", step="month", stepmode="backward"),
#                     dict(count=3, label="3m", step="month", stepmode="backward"),
#                     dict(count=1, label="YTD", step="year", stepmode="todate"),
#                     dict(count=1, label="1y", step="year", stepmode="backward"),
#                     dict(step="all"),
#                 ]
#             )
#         ),
#         rangeslider=dict(visible=True),
#         type="date",
#     )
# )



# Now we gotta add the predictions by prophet

Pro = Prophet(seasonality_mode="multiplicative")
Pro.fit(data)

future_years = Pro.make_future_dataframe(periods=Input)
future_price = Pro.predict(future_years)[["ds", "yhat", "yhat_lower", "yhat_upper"]]

Final = plot_plotly(Pro, future_price)
Final.update_layout(title_text="Etherium Open Price Plot",)
Final.show()





