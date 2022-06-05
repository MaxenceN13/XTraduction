import twitterengine

if __name__ == "__main__":
	print("⭐ Lancement de TradInstant ⭐")
	print("Authentification de l'utilisateur")
	Client = twitterengine.LoginOnTwitter()
	MentionsList = twitterengine.SearchRecentMentions(Client)
	# Recupère le quoted tweet du dernier tweet de la liste
	print(MentionsList)
	print()
	print(MentionsList.includes['tweets'][0])
