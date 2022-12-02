import tweepy as twe
import pandas as pan
import numpy as np
from textblob import TextBlob
import matplotlib.pyplot as ppt
from project import Get_coin
ppt.style.use("fivethirtyeight")

# Here are the four needed variables given by tweeter developer you can get yours if those dosent works
Key = "bpWyda2RuIryjyHGLUOGM6QFK"
Secret = "JWlQnGoUrK72YyQZzcMeEr0m6RIgP0Uy4TDr6mryNkKSqVmjil"
Token = "1597963175479201792-9GhrfziYt6Bsmm58BwYmGDelOumiLk"
TokenSecret = "lqZOQwZvvyjkRPxW0EViQaaQrmoJGVe86NZtNXGGMy2M7"

# Authentification 
authen = twe.OAuth2AppHandler(Key,Secret)
authen.set_access_token(Token,TokenSecret)
api = twe.API(authen,wait_on_rate_limit = True)

def main():
    Tweets = Get_tweets("Bitcoin")
    df = Build_df(Tweets)



# Get tweets
def Get_tweets(name):
    keyword = f"#{name}"
    Full_tweets = twe.Cursor(api.search_30_day, q=keyword)
    # Filter just the tweets text
    Tweets = [{"Tweets":tweet.text} for tweet in Full_tweets]
    return Tweets

# Function that get the polarity of a tweet
def Get_polarity(twt):
    return TextBlob(twt).sentiment.polarity


# Function that gets the sentiment of the tweet
def Get_sentiment(n):
    if n < 0:
        return "negative"
    elif n > 0 :
        return "positive"
    else:
        return "neutral"
    
# Functin that build the dataframe with the polarity and sentiment
def Build_df(Tweets):
    # Creating panda dataframe
    df = pan.DataFrame(Tweets)
    df["Polarity"] = df["Tweets"].apply(Get_polarity)
    df["Sentiment"] = df["Polarity"].apply(Get_sentiment)
    return df

# Function to create a plot
def Build_plot(df,name):
    plot = df["Sentiment"].value_counts().plot(kind = "bar")
    ppt.title(f"Sentiment Analysis of {name}")
    ppt.xlabel("Sentiment")
    ppt.ylabel("Num of Tweets")
    ppt.savefig(f"Plots/Sentiment of {name}.pdf")
    return None

if __name__ == "__main__":
    main()
    