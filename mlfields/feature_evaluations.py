from flask import (
    Blueprint,
    render_template,
    url_for
)

from mlfields.data_models import (
    Projects,
    FeatureMatrices,
    FeatureEvaluations
)


bp = Blueprint('feature_evaluations', __name__)


@bp.route('', methods=('GET',))
def list(project_id, fm_id):
    project = Projects.query.filter_by(project_id=project_id).first()
    fm = FeatureMatrices.query.filter_by(fm_id=fm_id)
    fes = FeatureEvaluations.query.filter_by(fm_id=fm_id)
    return render_template('feature_evaluations/list.html', project=project, fm=fm, fes=fes)
