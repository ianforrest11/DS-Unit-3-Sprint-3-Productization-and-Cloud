from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    id = DB.Column(DB.Integer, primary_key = True)
    name = DB.Column(DB.String(15), nullable=  False)

    def __repr__(self):
        return '<USER {}>'.format(self.name)

class Tweet(DB.Model):
    id = DB.Column(DB.Integer, primary_key = True)
    text = DB.Column(DB.Unicode(280))
    user_id = DB.Column(DB.Integer, DB.ForeignKey('user.id'), nullable = False)
    user = DB.relationship('User', backref = DB.backref('tweets', lazy = True))

    def __repr__(self):
        return '<TWEET {}>'.format(self.text)