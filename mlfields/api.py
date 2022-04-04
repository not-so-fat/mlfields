from flask import ( 
    Blueprint,
    request,
    jsonify
)
from flask_restful import (
    Resource,
    reqparse
)

from mlfields.data_models import (
    db,
    Projects
)


bp = Blueprint('api', __name__)


@bp.route('projects/', methods=('GET', 'POST'))
def create_project():
    if request.method == 'POST':
        name = request.json['name']
        note = request.json['note']
        new_project = Projects(name=name, note=note)
        db.session.add(new_project)
        db.session.commit()
        return jsonify({"project_id": new_project.project_id}), 201



@bp.route('fms', methods=('GET', 'POST'))
def register_feature_matrix(project_id):
    pass


@bp.route('fds', methods=('GET', 'POST'))
def register_feature_definition(project_id):
    if request.method == 'POST':
        content = request.json
        new_fd = FeatureDefinition(
            project_id=project_id,
            name=content["name"],
            formula=content["formula"],
            note=content["note"]
        )
        db.session.add(new_fd)
        db.session.commit()
        return jsonify({"feature_id": new_fd.feature_id}), 201


@bp.route('projects/<int:project_id>/fds/<int:feature_id>', methods=('GET', 'DELETE'))
def access_feature_definition(project_id, feature_id):
    if request.method == 'DELETE':
        fd = FeatureDefinitions.query.filter_by(project_id=project_id, feature_id=feature_id)
