from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure(app):
    app.db = db
    db.init_app(app)
