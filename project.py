import pandas as pan
import yfinance as finace
from datetime import datetime
from prophet import Prophet
from prophet.plot import plot_plotly
import plotly
import sys
import warnings
import os


# Ignore warnings
warnings.filterwarnings('ignore')

# Display prices in usd and 2 numbers after coma
pan.options.display.float_format = '${:,.2f}'.format

# Data for coin symbols and names
coins = [
        {"name":"binance","symbol":"BNB"},
        {"name":"bitcoin","symbol":"BTC"},
        {"name":"etherium","symbol":"ETH"},
        {"name":"solana","symbol":"SOL"},
        {"name":"xrp","symbol":"XRP"},
        {"name":"dogecoin","symbol":"DOGE"},
        {"name":"avalanche","symbol":"AVAX"},
        {"name":"tron","symbol":"TRX"},
    ]


def main():
    name,coin = Get_coin(input("Which Cryptocoin do you want to forecast?: ").strip())
    Duration = Get_duration(input("How many months do you want to see ahead ?: ").strip())
    data = Get_Data(coin)
    Graph = Create_plot(data,Duration)
    Graph = Style_plot(Graph,name)
    if input("Do you wish to see the resuls right now ?: ").lower().strip() in ["yes","y"]:
        Graph.show()
    if not os.path.exists("Plots"):
        os.mkdir("Plots")
    Save_plot(input("Do you wish to save the results ?: "),Graph,name)


# Getting number of days (refusing all but strict number of days)
def Get_duration(d):
    try :
        d = int(d)
    except:
        sys.exit("Invalid number of days")
    return d*30


def Get_coin(coin):
    for crypto in coins:
        if coin.lower() == crypto["name"] :
            return crypto["name"],crypto["symbol"]
        if coin.upper() == crypto["symbol"]:
            return crypto["name"],coin.upper()
    sys.exit("Invalid name/symbol\nExample of use : BTC\n-or-\nExample of use : Bitcoin")
            
            
# Getting data for the Coin
def Get_Data(c):
    today_date = datetime.today().strftime('%Y-%m-%d')
    # The first date where we can get Eth price info
    start_date = '2014-01-01'
    Eth_data = finace.download(f"{c}-USD",start = start_date,end = today_date)
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
def Style_plot(Final,n):
    Final.update_layout(title_text=f"{n.capitalize()} Open Price Plot",
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



def Save_plot(response,Graph,name):
    if "yes" in response.lower() or "y" in response.lower():
        print("Writing...")
        Graph.write_image(f"Plots/{name}.pdf")
    else: pass
    return print("Thanks for using my program ")
    
    
    
if __name__ == "__main__":
    main()




















