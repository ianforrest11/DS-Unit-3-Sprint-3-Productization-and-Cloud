"""main application and routing logic for twitoff."""

from decouple import config
from flask import Flask, render_template, request
from .models import DB, User

def create_app():
    """create/configure flask application."""
    app = Flask(__name__)
    
    # config link to database and env from .env file
    # remove flask shell warning about tracking modifications
    # initiate app
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['ENV'] = config('ENV')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)
    
    # create route to pass Users to application
    # populate user object in html template
    # sets title of application
    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html',
                               title = 'Home',
                               users = users)
        
    # define what to do when user enters /reset at end of URL
    # resets app! clears users
    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html',
                               title = 'DB Reset!',
                               users = [])
    
    return app
    