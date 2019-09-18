"""entry point for twitoff flask application"""

from .app import create_app

# create object inside 'twitoff' package namespace
# packages have __init__.py
APP = create_app()