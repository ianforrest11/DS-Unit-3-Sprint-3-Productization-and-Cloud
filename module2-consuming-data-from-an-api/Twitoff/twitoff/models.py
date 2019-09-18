"""SQLAlchemy models for TwitOff."""

# SQLAlchemy lets us use OOP to interact w relational databases
# similar to DJango

# models in different sense, schemas, way to specify type/structure of data
# and state that application cares about

from flask_sqlalchemy import SQLAlchemy


# declarative base class
# DB.create_all() creates empty database
# can view newly-created database using DB Browser
# create User example: u1 = User(name='Austin')
# create Tweet example: t1 = Tweet(text='LS Rocks!')
# to add u1/t1 to db: DB.session.add(u1)
#                     DB.session.add(t1)
# note: above only works on new entities, not modifying existing entities
# to save u1/t1 to db: DB.session.commit()
# re-open DB
# re-import DB 'from twitoff.models import *'
# User query: User.query.all(), positional: User.query.all()[0].name
# Tweet query: Tweet.query.all()[0].text
DB = SQLAlchemy()

# build user class based on declarative base class
# will be creating table, define details about the table within class
class User(DB.Model):
    """Twitter users that we pull and analyze tweets for"""
    # change DB.Integer to DB.BigInteger, as we are now pulling Twitter data
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger)

    # define way to represent data in rable, instead of displaying as memory address, e.g.:
    # >>> u1
    # <User (transient 4484608464)>   <<<<<FIX THIS
    def __repr__(self):
        return '<USER {}>'.format(self.name)

class Tweet(DB.Model):
    """Tweets."""
    id = DB.Column(DB.Integer, primary_key=True)
    text = DB.Column(DB.Unicode(500))
    
    # add embeddings to each class, considered a column
    # considered a blob, supported by SQL systems
    # PickleType is a blob in SQLAlchemy terms
    # nullable = False makes embedding a required field
    embedding = DB.Column(DB.PickleType, nullable=False)
    
    # add reference to each tweet pointing back to user by creating user_id (to link)
    # establish relationship between user and tweets with 'user' variable
    # establish one user to many tweets relationship
    user_id = DB.Column(DB.Integer, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return '<TWEET {}>'.format(self.text)

# drop all exiting tables using DB.drop_all()
# re-do DB.create_all(), creates new database with correct formatting and linked tables
# assign tweet 't1' to user 'u1' with u1.tweets.append(t1)
# >>> DB.session.add(u1)
# >>> DB.session.add(t1)
# >>> DB.session.commit()
# >>> quer = User.query.filter(User.name == 'Austin').first()
# <USER Austin>

# >>> quer.tweets
# [<TWEET tweet!>]