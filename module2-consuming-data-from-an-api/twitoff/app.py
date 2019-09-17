"""
main application and routing logic for twitoff
"""

# import flask, 'DB' from .models folder
from flask import Flask, render_template, request
from .models import DB, User



def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    # vvvvv use sqlite database vvvvv
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    # add code to tell SQLAlchemy not to track modifications
    # removes warning
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # add debugging configuration
    app.config['ENV'] = 'debug'

    # vvvvv have DB initialize the app
    DB.init_app(app)

    @app.route('/')
    def root():
        # add users, import user from .models folder
        # get all users
        users = User.query.all()

        # render_template knows to look in templates directory
        # FLASK_APP=twitoff:APP flask run
        # add title (defined in html file) and users (defined above and in html)
        return render_template('base.html', title = 'Home', users = users)

    return app