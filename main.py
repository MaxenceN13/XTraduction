import myStreamingClient
import tweepy
import translateDeeplAPI
import config

# Recupère un client object (permet d'effectuer des actions sur un compte comme tweeter par exemple)
def getClient():
	return tweepy.Client(consumer_key=config.API_KEY,
						 consumer_secret=config.API_SECRET,
						 access_token=config.ACCESS_TOKEN,
						 access_token_secret=config.ACCESS_TOKEN_SECRET)

# Post un tweet avec le compte Client en réponse à un TweetId avec comme contenue le TweetText
def answerToTweet(Client, TweetText, IdSourceTweet):
	Client.create_tweet(text=TweetText,
						in_reply_to_tweet_id=IdSourceTweet,
						user_auth=1)

if __name__ == "__main__":
	print("⭐ Lancement de TradInstant ⭐")

	def tweetTranslatedText(response):
		# Recupère le tweet qui à initier l'évenement
		initialTweet = response.data
		# Recupère le tweet cité ou répondu
		tweetToTranslate = response.includes['tweets'][0]
		# Recupère le client (pour effectuer des actions sur le compte Twitter)
		client = getClient()
		# Traduit le texte du tweet
		translatedTweet = translateDeeplAPI.translate(tweetToTranslate.text)
		# Répond aux tweet initial avec la traduction du tweet
		answerToTweet(client, translatedTweet, initialTweet.id)
	
	client = getClient()

	streaming_client = myStreamingClient.myStreamingClient(config.BEARER_TOKEN, tweetTranslatedText)

	streaming_client.filter(expansions=["referenced_tweets.id"])

	print("Programme effectué avec succès !")