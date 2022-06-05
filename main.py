import twitterengine
import translateDeeplAPI

if __name__ == "__main__":
    print("⭐ Lancement de TradInstant ⭐")
    print("Authentification de l'utilisateur")
    Client = twitterengine.LoginOnTwitter()
    MentionsList = twitterengine.SearchRecentMentions(Client)

    NewLastTweetId = MentionsList.data[0].id

    LastTweetId = 0

    # Si on trouve un nouveau tweet non traité
    if NewLastTweetId != LastTweetId:
        TweetToTranslate = MentionsList.includes['tweets'][0].text
        TweetTranslated = translateDeeplAPI.Translate(TweetToTranslate)
        twitterengine.AnswerToTweet(Client, TweetTranslated, NewLastTweetId)
