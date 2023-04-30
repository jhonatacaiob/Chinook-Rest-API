from dataclasses import asdict
from flask import (
    Blueprint,
    current_app,
    request,
)

from music_app.models.artista import Artista

bp = Blueprint('artistas', __name__, url_prefix='/artistas')


@bp.get('/')
def listar():
    db = current_app.db
    artistas = db.session.execute(db.select(Artista)).fetchall()

    return [asdict(artista[0]) for artista in artistas]

@bp.get('/<id>')
def visualizar(id):
    db = current_app.db
    artista = db.get_or_404(Artista, id)
    
    return asdict(artista)


@bp.post('/<id>')
def criar(id):
#    data = request.get_json()
    ...

@bp.put('/<id>')
def editar(id):
    ...

@bp.delete('/<id>')
def deletar(id):
    ...
