import tweepy as twe
import pandas as pan
import numpy as np
import re
import nltk
from textblob import TextBlob
import matplotlib.pyplot as ppt
from forecast import Get_coin

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')


# Here are the four needed variables given by tweeter developer you can get yours if those dosent works
Key = "bpWyda2RuIryjyHGLUOGM6QFK"
Secret = "JWlQnGoUrK72YyQZzcMeEr0m6RIgP0Uy4TDr6mryNkKSqVmjil"
Token = "1597963175479201792-9GhrfziYt6Bsmm58BwYmGDelOumiLk"
TokenSecret = "lqZOQwZvvyjkRPxW0EViQaaQrmoJGVe86NZtNXGGMy2M7"

# Authentification 
authen = twe.OAuthHandler(Key,Secret)
authen.set_access_token(Token,TokenSecret)
api = twe.API(authen,wait_on_rate_limit = True)

def main():
    Tweets = Get_tweets("Bitcoin")
    df = Build_df(Tweets)
    Build_plot(df,"Bitcoin")



# Get tweets
def Get_tweets(name):
    keyword = f"#{name} -filter:retweets"
    Full_tweets = twe.Cursor(api.search_tweets, q = keyword, lang = "en").items(2000)
    # Filter just the tweets text
    Tweets = [{"Tweets":tweet.text} for tweet in Full_tweets]
    return Tweets

# Function that get the polarity of a tweet
def Get_polarity(twt):
    return TextBlob(twt).sentiment.polarity


# Function that gets the sentiment of the tweet
def Get_sentiment(n):
    if n < 0:
        return "NEG"
    elif n > 0 :
        return "POS"
    
# Functin that build the dataframe with the polarity and sentiment
def Build_df(Tweets):
    # Creating panda dataframe
    df = pan.DataFrame.from_dict(Tweets)
    df["CleanTweets"] = df["Tweets"].apply(Clean_tweets)
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


def Clean_tweets(tweet):
    tweet = tweet.lower()
    tweet = re.sub("'", "", tweet) # to avoid removing contractions in english
    tweet = re.sub("@[A-Za-z0-9_]+","", tweet) # Remove mentions
    tweet= re.sub("#[A-Za-z0-9_]+","", tweet) # Remove any word that start with #
    tweet = re.sub(r'https?\S+', '', tweet) # Remove links
    tweet = re.sub('[()!?]', ' ', tweet) # Removing punctuations
    tweet = re.sub('\[.*?\]',' ', tweet)
    tweet = re.sub("[^a-z0-9]"," ", tweet) # Filtering non-alphanumeric characters
    tweet = tweet.split() # Tokenization
    tweet = [w for w in tweet if not w in stopwords] # remove stopwords
    tweet = " ".join(word for word in tweet)
    return tweet

if __name__ == "__main__":
    main()
    