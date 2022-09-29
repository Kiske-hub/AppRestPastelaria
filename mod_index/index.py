from flask import Blueprint, render_template

bp_index = Blueprint('index', __name__, url_prefix="/", template_folder='templates')

''' rotas do index '''

@bp_index.route('/')
def formListaIndex():
    return render_template('formListaIndex.html'), 200

