"""retrieve tweets, embeddings, and persist in database."""
import tweepy
from decouple import config
from .models import DB, Tweet, User
import basilica

TWITTER_AUTH = tweepy.OAuthHandler(config('TWITTER_CONSUMER_KEY'),
                                   config('TWITTER_CONSUMER_SECRET'))
TWITTER_AUTH.set_access_token(config('TWITTER_ACCESS_TOKEN'),
                              config('TWITTER_ACCESS_TOKEN_SECRET'))
TWITTER = tweepy.API(TWITTER_AUTH)

BASILICA = basilica.Connection(config('BASILICA_KEY'))



# >>> from twitoff.twitter import *
# >>> twitter_user = TWITTER.get_user('john')
# >>> twitter_user
# >>> tweets = twitter_user.timeline()
# >>> len(tweets)
# 20
# >>> tweets[0].text
# 'RT @shots: How To Get a Latina by @ElJuanpaZurita with @lelepons via Shots Studios: https://t.co/4HzyjN47sq https://t.co/uJHbeV16kO'
# >>> tweets = twitter_user.timeline(count=200, exclude_replies=True, include_rts=False, tweet_mode = 'extended')
# >>> tweets[0].full_text
# 'I always snarkily ask late-stage CEOs when they’re going public.\n\n Sid is the only one who ever responded with a hopeful date.\n\nI respect so much the way that company is run. https://t.co/ZrsdGmkVy4'
# >>> tweets[0].created_atdatetime.datetime(2019, 9, 17, 13, 45, 19)
# >>> tweets[0].retweeted
# False
# >>> tweets[0].id
# 1173956097754980354
# >>> tweet_text = tweets[0].full_text
# >>> embedding = BASILICA.embed_sentence(tweet_text, model = 'twitter')
# >>> embedding
# [-0.293004, -0.485193, 0.701077, -0.681001,