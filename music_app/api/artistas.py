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
    query = current_app.db.select(Artista)
    artistas = current_app.db.session.execute(query).fetchall()
    return [asdict(artista[0]) for artista in artistas], 200


@bp.get('/<id>')
def visualizar(id):
    artista = current_app.db.get_or_404(Artista, id)

    return asdict(artista), 200


@bp.post('/')
def criar():
    if request.is_json:
        try:
            payload = request.get_json()
            artista = Artista(**payload)

            if artista.id is not None or artista.nome is None:
                raise TypeError()

            stmt = current_app.db.session.add(artista)
            current_app.db.session.commit()

            return (
                {
                    'artista': asdict(artista),
                    'url': f'{request.base_url}{artista.id}',
                    'mensagem': f'O artista de   nome {artista.nome} foi criado com sucesso',
                },
                201,
            )

        except TypeError:
            return {'erro': 'Verifique os campos enviados na requisição'}, 400

    return {'erro': 'O payload precisa ser um json'}, 400


@bp.put('/<id>')
def editar(id):
    if request.is_json:
        try:
            payload = request.get_json()
            artista_payload = Artista(**payload)

            if artista_payload.id is not None or artista_payload.nome is None:
                raise TypeError()

            artista_atual = current_app.db.get_or_404(Artista, id)
            artista_atual.nome = artista_payload.nome

            current_app.db.session.commit()
            return (
                {
                    'artista': asdict(artista_atual),
                    'url': f'{request.base_url}{artista_atual.id}',
                },
                200,
            )
        except TypeError:
            return {'erro': 'Verifique os campos enviados na requisição'}, 400

    return {'erro': 'O payload precisa ser um json'}, 400


@bp.delete('/<id>')
def deletar(id):
    artista_atual = current_app.db.get_or_404(Artista, id)
    current_app.db.session.delete(artista_atual)
    current_app.db.session.commit()

    return {}, 204
