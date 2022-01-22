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
    jsonify
)
import pandas

from mlfields.data_models import (
    db,
    Projects
)


bp = Blueprint('projects', __name__, url_prefix='/projects')


@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        note = request.form['note']
        error = None

        if not name:
            error = 'Name is required.'

        if error is not None:
            flash(error)
        else:
            new_project = Projects(name=name, note=note)
            db.session.add(new_project)
            db.session.commit()
            return redirect(url_for("projects.list"))

    return render_template('projects/create.html')


@bp.route('/', methods=('GET',))
def list():
    projects = Projects.query
    return render_template('projects/list.html', projects=projects)
