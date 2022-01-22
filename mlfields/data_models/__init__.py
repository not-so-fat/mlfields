from datetime import datetime

import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

from mlfields import create_app


db = SQLAlchemy()


class Projects(db.Model):
    __tablename__ = "projects"
    project_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, unique=True, nullable=False)
    note = db.Column(db.String)
    created = db.Column(db.DateTime, nullable=False, default=sqlalchemy.sql.func.now())


class FeatureDefinitions(db.Model):
    __tablename__ = "feature_definitions"
    feature_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.project_id"), nullable=False)
    name = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    note = db.Column(db.String)


class FeatureMatrices(db.Model):
    __tablename__ = "feature_matrices"
    fm_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.project_id"), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    filepath = db.Column(db.String, nullable=False)
    note = db.Column(db.String)


class FeatureListInFM(db.Model):
    __tablename__ = "feature_list_in_fm"
    row_id = db.Column(db.Integer, primary_key=True)
    fm_id = db.Column(db.Integer, db.ForeignKey("feature_matrices.fm_id"), nullable=False)
    feature_id = db.Column(db.Integer, db.ForeignKey("feature_definitions.feature_id"), nullable=False)


class BaseEvaluation(db.Model):
    __tablename__ = "base_evaluation"
    row_id = db.Column(db.Integer, primary_key=True)
    feature_id = db.Column(db.Integer, db.ForeignKey("feature_definitions.feature_id"), nullable=False)
    fm_id = db.Column(db.Integer, db.ForeignKey("feature_matrices.fm_id"), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    mean = db.Column(db.Numeric)
    max = db.Column(db.Numeric)
    min = db.Column(db.Numeric)
    stdev = db.Column(db.Numeric)
