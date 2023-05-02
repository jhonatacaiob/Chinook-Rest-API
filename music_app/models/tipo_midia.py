from dataclasses import dataclass

from ..database import db


@dataclass
class TipoMidia(db.Model):
    id: db.Mapped[int] = db.mapped_column(
        primary_key=True,
    )
    nome: db.Mapped[str] = db.mapped_column()
