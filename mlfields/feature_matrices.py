from flask import (
    Blueprint,
    render_template,
    url_for
)

from mlfields.data_models import (
    Projects,
    FeatureMatrices
)


bp = Blueprint('feature_matrices', __name__)

@bp.route('', methods=('GET',))
def list(project_id):
    project = Projects.query.filter_by(project_id=project_id).first()
    fms = FeatureMatrices.query.filter_by(project_id=project_id)
    return render_template('feature_matrices/list.html', project=project, fms=fms)
