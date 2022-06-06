import config
import tweepy
import translateDeeplAPI

# Class héritant de StreamingClient
class TweetPrinterV2(tweepy.StreamingClient):
	# Redéfinit la méthode on_response
	# Lorsque que l'on detecte un évenement, la recupère sous forme d'objet Reponse
	def on_response(self, response):
		# Recupère le tweet qui à initier l'évenement
		initialTweet = response.data
		# Recupère le tweet cité ou répondu
		tweetToTranslate = response.includes['tweets'][0]
		# Recupère le client (pour effectuer des actions sur le compte Twitter)
		client = getClient()
		# Traduit le texte du tweet
		translatedTweet = translateDeeplAPI.Translate(tweetToTranslate.text)
		# Répond aux tweet initial avec la traduction du tweet
		AnswerToTweet(client, translatedTweet, initialTweet.id)
 

# Recupère un client object (permet d'effectuer des actions sur un compte comme tweeter par exemple)
def getClient():
	return tweepy.Client(consumer_key=config.API_KEY,
						 consumer_secret=config.API_SECRET,
						 access_token=config.ACCESS_TOKEN,
						 access_token_secret=config.ACCESS_TOKEN_SECRET)


# Recupère un StreamingClient (flux ouvert en continue), ajoute une règle, attend un évenement
def startListeningNewTweetWithSpecificRules():
	# Recupère un objet TweetPrinterV2
	printer = TweetPrinterV2(config.BEARER_TOKEN)
	delAllRules(printer)
	rule = tweepy.StreamRule(value=f"(is:quote OR is:reply) {config.BOT_TWITTER_ACCOUNT_NAME} -from:{config.BOT_TWITTER_ACCOUNT_ID}")
	printer.add_rules(rule)
	printer.filter(expansions=["referenced_tweets.id"])


# Post un tweet avec le compte Client en réponse à un TweetId avec comme contenue le TweetText
def AnswerToTweet(Client, TweetText, IdSourceTweet):
	Client.create_tweet(text=TweetText,
						in_reply_to_tweet_id=IdSourceTweet,
						user_auth=1)

# Supprime toutes les règles d'un StreamingClient
def delAllRules(streamingClient):
	rules = streamingClient.get_rules().data
	if rules != None:
		for rule in rules:
			streamingClient.delete_rules(rule.id)