from dataclasses import dataclass

from flask import current_app

from ..database import db


@dataclass
class Artista(db.Model):

    id: db.Mapped[int] = db.mapped_column(
        primary_key=True,
    )
    nome: db.Mapped[str] = db.mapped_column()
    albuns: db.Mapped[list['Album']] = db.relationship(back_populates='artista')
