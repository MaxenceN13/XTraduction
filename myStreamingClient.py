import config
import tweepy
import translateDeeplAPI

# Class héritant de StreamingClient
class myStreamingClient(tweepy.StreamingClient):
	def __init__(self, bearer_token, callback_function):
		tweepy.StreamingClient.__init__(self, bearer_token = bearer_token)
		delAllRules(self)
		self.add_rules(tweepy.StreamRule(value=f"(is:quote OR is:reply) {config.BOT_TWITTER_ACCOUNT_NAME} -from:{config.BOT_TWITTER_ACCOUNT_ID}"))
		self.callback_function = callback_function

	# Redéfinit la méthode on_response
	# Lorsque que l'on detecte un évenement, la recupère sous forme d'objet Reponse
	def on_response(self, response):
		self.callback_function(response)
		
 
# Supprime toutes les règles d'un StreamingClient
def delAllRules(streamingClient):
	rules = streamingClient.get_rules().data
	if rules != None:
		for rule in rules:
			streamingClient.delete_rules(rule.id)