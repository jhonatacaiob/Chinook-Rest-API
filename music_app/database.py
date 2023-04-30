import os

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine import URL
from dotenv import load_dotenv


load_dotenv()
db = SQLAlchemy()


def configure(app):
    url = URL.create(
        os.getenv('DRIVERNAME'),
        username=os.getenv('USERNAME'),
        password=os.getenv('PASSWORD'),
        host=os.getenv('HOST'),
        database=os.getenv('DATABASE'),
        port=os.getenv('PORT'),
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = url
    app.db = db
    db.init_app(app)
