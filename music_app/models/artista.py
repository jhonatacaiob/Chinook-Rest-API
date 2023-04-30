from dataclasses import dataclass

from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import synonym


db = SQLAlchemy()


@dataclass
class Artista(db.Model):
    __tablename__ = 'Artist'

    id: db.Mapped[int]
    name: db.Mapped[str]

    ArtistId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(
        db.String,
    )

    id = synonym('ArtistId')
    name = synonym('Name')
