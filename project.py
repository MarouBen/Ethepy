import sys
from forecast import coins,forecast
from twitter_scrap import scrap



def main():
    name = Get_name()
    symbol = Get_symbol(name)
    Duration = Get_duration()
    forecast(name,symbol,Duration)
    scrap(name.capitalize())




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


if __name__ == "__main__":
    main()