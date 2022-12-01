import tweepy as twe
import pandas as pan
import numpy as np
from textblob import TextBlob
from matplotlib import pyplot as ppt
from project import Get_coin

# Here are the four needed variables given by tweeter developer you can get yours if those dosent works
Key = ""
Secret = ""
Token = ""
TokenSecret = ""

# Authentification 
authen = twe.OAuth2AppHandler(Key,Secret)
authen.set_access_token(Token,TokenSecret)
api = twe.API(authen,wait_on_rate_limit = True)

# Get tweets
def Get_tweets(name):
    keyword = f"#{name}"
    Full_tweets = twe.Cursor(api.search_30_day, q=keyword)
    # Filter just the tweets text
    Tweets = [{"Tweets":tweet.text} for tweet in Full_tweets]
    #creating panda dataframe
    df = pan.DataFrame(Tweets)
    return df
    