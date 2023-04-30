import sqlalchemy
from sqlalchemy import Column
from flask import current_app

class Artista(current_app.db.Model):
    ArtistId = Column(sqlalchemy.Integer, primary_key=True)
    Name = Column(sqlalchemy.String, )
