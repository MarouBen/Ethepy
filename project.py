import sys
from forecast import coins



def main():
    name = Get_name()


def Get_name():
    return input("Which Cryptocoin do you want to forecast?: ").strip()

def Get_coin(coin):
    for crypto in coins:
        if coin.lower() == crypto["name"] :
            return crypto["name"],crypto["symbol"]
        if coin.upper() == crypto["symbol"]:
            return crypto["name"],coin.upper()
    sys.exit("Invalid name/symbol\nExample of use : BTC\n-or-\nExample of use : Bitcoin")