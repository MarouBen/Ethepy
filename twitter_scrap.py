import tweepy as twe
import pandas as pan
import numpy as np
from matplotlib import pyplot as ppt

# Here are the four needed variables given by tweeter developer you can get yours if those dosent works
Key = ""
Secret = ""
Token = ""
TokenSecret = ""

# Authentification 
authen = twe.OAuthHandler(Key,Secret)
authen.set_access_token(Token,TokenSecret)
api = twe.API(authen,wait_on_rate_limit = True)
