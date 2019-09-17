"""
main application and routing logic for twitoff
"""

# import flask, 'DB' from .models folder
from flask import Flask
from .models import DB


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    # vvvvv use sqlite database vvvvv
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    # vvvvv have DB initialize the app
    DB.init_app(app)

    @app.route('/')
    def root():
        return 'Welcome to TwitOff!'

    return app