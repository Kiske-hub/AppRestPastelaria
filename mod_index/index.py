from flask import Blueprint, render_template

bp_index = Blueprint('index', __name__, url_prefix="/", template_folder='templates')

''' rotas do index '''

@bp_index.route('/', methods=['GET', 'POST'])
def formListaIndex():
    return render_template('formListaIndex.html')

@bp_index.route('/form-index/', methods=['GET'])
def formIndex():
    return render_template('formIndex.html')

