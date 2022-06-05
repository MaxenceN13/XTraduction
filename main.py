import twitterengine

if __name__ == "__main__":
	print("⭐ Lancement de TradInstant ⭐")
	print("Authentification de l'utilisateur")
	Client = twitterengine.LoginOnTwitter()
	MentionsList = twitterengine.SearchRecentMentions(Client)