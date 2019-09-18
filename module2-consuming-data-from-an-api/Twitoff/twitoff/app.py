"""
main application and routing logic for twitoff
"""

# import flask, 'DB' from .models folder
from flask import Flask, render_template, request
from .models import DB, User

# import config from decouple, allows us to change URI to DATABASE_URL from .env
from decouple import config



def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    # vvvv replaced sqlite:/// with link to DB, will be PostGresURL in future, will work just the same
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')

    # add code to tell SQLAlchemy not to track modifications
    # removes warning
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # set ENV in .env, so replacing 'debug' with 'config('ENV')'
    # will change to PROD once finished
    app.config['ENV'] = config('ENV')

    # vvvvv have DB initialize the app
    DB.init_app(app)

    @app.route('/')
    def root():
        # add users, import user from .models folder
        # get all users
        # pass whole user object, gives access to all variables
        # can pull user.tweets, user.name, user.id
        users = User.query.all()

        # render_template knows to look in templates directory
        # FLASK_APP=twitoff:APP flask run
        # add title (defined in html file) and users (defined above and in html)
        return render_template('base.html', title = 'Home', users = users)

    return app