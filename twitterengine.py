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
	delAllRules(printer)
	rule = tweepy.StreamRule(value="(is:quote OR is:reply) @elon_musk_fr -from:1533204921868238848")
	printer.add_rules(rule)
	print(printer.get_rules())
	printer.filter(expansions=["referenced_tweets.id"])


def AnswerToTweet(Client, TweetText, IdSourceTweet):
	Client.create_tweet(text=TweetText,
						in_reply_to_tweet_id=IdSourceTweet,
						user_auth=1)

def delAllRules(streamingClient):
	rules = streamingClient.get_rules().data
	if rules != None:
		for rule in rules:
			streamingClient.delete_rules(rule.id)