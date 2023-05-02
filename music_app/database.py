import os

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import URL


db = SQLAlchemy()


def configure_db(app):
    load_dotenv()
    url = URL.create(
        os.getenv('DRIVERNAME'),
        username=os.getenv('USERNAME_DB'),
        password=os.getenv('PASSWORD_DB'),
        host=os.getenv('HOST'),
        database=os.getenv('DATABASE'),
        port=os.getenv('PORT'),
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = url

    app.db = db
    db.init_app(app)
