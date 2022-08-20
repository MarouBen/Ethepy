# For cleaning data
import pandas as pan
# For getting eth prices
import yfinance as finace
from datetime import datetime
from prophet import Prophet
from prophet.plot import plot_plotly
import warnings

# Ignore warnings
warnings.filterwarnings('ignore')
# Display prices in usd and 2 numbers after coma
pan.options.display.float_format = '${:,.2f}'.format


def main():
    Duration = int(input("How many days you want to see ahead ?"))
    data = Get_Data()
    Graph = Create_plot(data,Duration)
    Graph = Style_plot(Graph)
    Graph.show()
    


# Getting data for the Coin
def Get_Data():
    today_date = datetime.today().strftime('%Y-%m-%d')
    # The first date where we can get Eth price info
    start_date = '2016-01-01'
    Eth_data = finace.download("ETH-USD",start = start_date,end = today_date)
    Eth_data.reset_index(inplace = True)       # Using Eth_data.columns we can see that we dont have a date columns so we need to index it == reseting index to count from first row
    # We need just tha date and open price
    data = Eth_data[["Date", "Open"]]          # We use [[]] to return a panda dataframe in a (m,n) format // [] will return a serie in (n) format
    # We need to rename the columns for prophet later
    data.rename(columns = {"Date":"ds","Open":"y"}, inplace = True)
    return data 
    
    
# Creating the graph for the cryptocoin for the specific duration
def Create_plot(data,Input):
    Pro = Prophet(seasonality_mode="multiplicative")
    Pro.fit(data)
    future_years = Pro.make_future_dataframe(periods=Input)
    future_price = Pro.predict(future_years)[["ds", "yhat", "yhat_lower", "yhat_upper"]]
    Final = plot_plotly(Pro, future_price)
    return Final
     
    
# Styling the Graph
def Style_plot(Final):
    Final.update_layout(title_text="Etherium Open Price Plot",
                    title_font_size=30,
                    xaxis_title="Date",
                    yaxis_title="Price in $",
                    showlegend=True,
                    legend_title="Legend",
                    # autosize=True,
                    height=1000,
                    width=1940,
                    margin_autoexpand=True,)
    Final.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ))
    Final.update_traces(marker=dict(size=1,
                                    line=dict(width=2,color='DarkSlateGrey'),
                                    color="purple"
                                    ),
                        selector=dict(mode='markers')
                        )
    return Final
    

    
if __name__ == "__main__":
    main()




















