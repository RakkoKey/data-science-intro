import tweepy
from textblob import TextBlob

consumer_key = "ZSPG7m3h29gfLiz6Ko10NrCYh"
consumer_key_secret = "sAOdc5PNaRCaXVZzQOp4buB2iykE8XSedRlPO2IEvQXEhHa8Ob"

access_token = "3023875539-9tOCMf1huSXc2nIJQ8lYSPJCs3GP6NlQH6rc5Ws"
access_token_secret = "wew4ZxqO4m6DvyRQJLtxP6IOp6JrG4WCfXRWyYc2sQpwF"
#authentication start
auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#authentication end

public_tweets = api.search_tweets('Hololive')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
