import config
import tweepy
import translateDeeplAPI


class TweetPrinterV2(tweepy.StreamingClient):
	#Fonction Asyncrone (Declenché par la rule qui detecte les réponses) : Elle extrait le tweet initiant & le tweet a traduire,
	# puis elle tweet la reponse
	def on_response(self, response):
		initialTweet = response.data
		tweetToTranslate = response.includes['tweets'][0]
		print(initialTweet.text)
		print(tweetToTranslate.text)
		client = getClient()
		translatedTweet = translateDeeplAPI.Translate(tweetToTranslate.text)
		AnswerToTweet(client, translatedTweet, initialTweet.id)
 


def getClient():
	return tweepy.Client(consumer_key=config.API_KEY,
						 consumer_secret=config.API_SECRET,
						 access_token=config.ACCESS_TOKEN,
						 access_token_secret=config.ACCESS_TOKEN_SECRET)



def getStreamingClient():
	printer = TweetPrinterV2(config.BEARER_TOKEN)
	rule = tweepy.StreamRule(value="(is:quote OR is:reply) @elon_musk_fr")
	printer.add_rules(rule)
	printer.filter(expansions=["referenced_tweets.id"])


def SearchRecentMentions(ClientTweepy):
	TweetList = ClientTweepy.search_recent_tweets(query="(is:quote OR is:reply) @elon_musk_fr",
												  max_results=10,
												  expansions=["referenced_tweets.id"],
												  user_auth=1)
	return TweetList


def AnswerToTweet(Client, TweetText, IdSourceTweet):
	Client.create_tweet(text=TweetText,
						in_reply_to_tweet_id=IdSourceTweet,
						user_auth=1)
