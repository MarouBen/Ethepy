import os
import sys
import shutil
from forecast import coins,forecast
from twitter_scrap import scrap
from pdf_creation import Creat_pdf


def main():
    # Getting the name of the cryptocurrency and it symbol
    name = Get_name()
    symbol = Get_symbol(name)
    # Duration that we will forecast
    Duration = Get_duration()
    
    # The three projects that make this work
    forecast(name,symbol,Duration)
    scrap(name.capitalize())
    Creat_pdf(name.lower())
    
    # Cleaning up
    clean_up()




# Getting the name of the crypto
def Get_name():
    name = input("Which Cryptocoin do you want to forecast?: ").strip()
    for crypto in coins:
        if name.lower() == crypto["name"] or name.upper() == crypto["symbol"]:
            return crypto["name"]
    sys.exit("Invalid name/symbol\nExample of use : BTC\n-or-\nExample of use : Bitcoin")


# Getting the symbol of the crypto
def Get_symbol(name):
    for crypto in coins:
        if name.lower() == crypto["name"]:
            return crypto["symbol"]
    sys.exit("ERROR 101")


# Getting number of days (refusing all but strict number of days)
def Get_duration():
    months = input("How many months do you want to see ahead ?: ").strip()
    try :
        days = int(months)
    except:
        sys.exit("Invalid number of days")
    return days*30

# A clean up function
def clean_up():
    if os.path.exists("Plots"):
        shutil.rmtree("Plots")
    return print("Thanks for using my program ")


if __name__ == "__main__":
    main()