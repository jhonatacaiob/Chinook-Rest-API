from dataclasses import dataclass

from flask import current_app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


@dataclass
class Artista(db.Model):

    id: db.Mapped[int] = db.mapped_column(
        primary_key=True,
    )
    nome: db.Mapped[str] = db.mapped_column()
