import functools

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('music', __name__, url_prefix='/music')


@bp.route('/bla', methods=['GET'])
def register():
    return 'BLA'
