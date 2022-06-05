import config
import tweepy

def LoginOnTwitter():
    return tweepy.Client(consumer_key=config.API_KEY,
			     consumer_secret=config.API_SECRET,
			     access_token=config.ACCESS_TOKEN,
			     access_token_secret=config.ACCESS_TOKEN_SECRET)
