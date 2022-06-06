import config
import tweepy
import re

class TweetPrinterV2(tweepy.StreamingClient):
	
	def on_response(self, response):
		initialTweet = response.data
		tweetToTranslate = response.includes['tweets'][0]
		print(initialTweet.text)
		print(tweetToTranslate.text)
		# print(f"{tweet.id} {tweet.created_at} ({tweet.author_id}): {tweet.text}")
		# print("-"*50)
 


def LoginOnTwitter():
	return tweepy.Client(consumer_key=config.API_KEY,
						 consumer_secret=config.API_SECRET,
						 access_token=config.ACCESS_TOKEN,
						 access_token_secret=config.ACCESS_TOKEN_SECRET)

# Requetes faites a Twitter

def getStreamingClient():
	printer = TweetPrinterV2(config.BEARER_TOKEN)
	rule = tweepy.StreamRule(value="(is:quote OR is:reply) @elon_musk_fr")
	printer.add_rules(rule)
	printer.filter(expansions=["referenced_tweets.id"])

def SearchRecentMentions(ClientTweepy):
	TweetList = ClientTweepy.search_recent_tweets(query="(is:quote OR is:reply) @elon_musk_fr",
												  max_results=10,
												  expansions=[
													  "referenced_tweets.id"],
												  user_auth=1)
	# print(TweetList)
	return TweetList


def AnswerToTweet(Client, TweetText, IdSourceTweet):
	Client.create_tweet(text=TweetText,
						in_reply_to_tweet_id=IdSourceTweet,
						user_auth=1)
