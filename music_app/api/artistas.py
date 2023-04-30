import functools

from flask import (
    Blueprint,
    current_app,
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('artistas', __name__, url_prefix='/artistas')


@bp.route('/', methods=['GET'])
def get_artistas():
    session = current_app.db.session

    return 'BLA'
