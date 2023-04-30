import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from music_app.api import music
from music_app.database import configure_db
from music_app.api import artistas


def create_app(test_config=None):
    # create and configure_db the app
    app = Flask(__name__, instance_relative_config=True)
    configure_db(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(music.bp)
    app.register_blueprint(artistas.bp)

    return app
