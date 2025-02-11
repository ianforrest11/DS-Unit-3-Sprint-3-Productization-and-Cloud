"""retrieve tweets, embeddings, and persist in database."""

import basilica
from decouple import config
from .models import DB, User, Tweet
import tweepy

TWITTER_AUTH = tweepy.OAuthHandler(config('TWITTER_CONSUMER_KEY'),
                                   config('TWITTER_CONSUMER_SECRET'))
TWITTER_AUTH.set_access_token(config('TWITTER_ACCESS_TOKEN'),
                              config('TWITTER_ACCESS_TOKEN_SECRET'))
TWITTER = tweepy.API(TWITTER_AUTH)
BASILICA = basilica.Connection(config('BASILICA_KEY'))



def add_user(username):
    """Add a user and their Tweets, error if not a Twitter user."""
    try:
        # define twitter user, add to db, pull tweets
        twitter_user = TWITTER.get_user(username)
        db_user = User(id=twitter_user.id, name=username)
        DB.session.add(db_user)
        tweets = twitter_user.timeline(
            count=200, exclude_replies=True, include_rts=False,
            tweet_mode='extended', since_id=db_user.newest_tweet_id)
        # if tweets are present, define the most recent one as 'newest_tweet_id'
        if tweets:
            db_user.newest_tweet_id = tweets[0].id
        # for loop for individual tweet, embed, ID methods of tweet to be displayed         
        for tweet in tweets:
            embedding = BASILICA.embed_sentence(tweet.full_text,
                                                model='twitter')
            db_tweet = Tweet(id=tweet.id,
                             text=tweet.full_text[:500],
                             date=tweet.created_at,
                             embedding=embedding)
            # associate tweets to user, add user/tweets to db
            db_user.tweets.append(db_tweet)
            DB.session.add(db_tweet)
    except Exception as e:
        print('Error processing {}: {}'.format(username, e))
        raise e
    else:
        DB.session.commit()