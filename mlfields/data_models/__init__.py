from datetime import datetime

import sqlalchemy
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Projects(db.Model):
    __tablename__ = "projects"
    project_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    note = db.Column(db.String)
    created = db.Column(db.DateTime, nullable=False, default=sqlalchemy.sql.func.now())


class FeatureDefinitions(db.Model):
    __tablename__ = "feature_definitions"
    feature_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.project_id"), nullable=False)
    name = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=sqlalchemy.sql.func.now())
    note = db.Column(db.String)


class FeatureMatrices(db.Model):
    __tablename__ = "feature_matrices"
    fm_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.project_id"), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=sqlalchemy.sql.func.now())
    name = db.Column(db.String, nullable=False)
    note = db.Column(db.String)


class MetricsInUse(db.Model):
    __tablename__ = "metrics_in_use_project"
    row_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.project_id"), nullable=False)
    metric_id = db.Column(db.Integer, db.ForeignKey("evaluation_metrics.metric_id"), nullable=False)
    __table_args__ = (db.UniqueConstraint("project_id", "metric_id", name="_project_id_metric_id_uc"),)


class FeatureEvaluations(db.Model):
    __tablename__ = "feature_evaluation"
    row_id = db.Column(db.Integer, primary_key=True)
    feature_id = db.Column(db.Integer, db.ForeignKey("feature_definitions.feature_id"), nullable=False)
    fm_id = db.Column(db.Integer, db.ForeignKey("feature_matrices.fm_id"), nullable=False)
    metric_id = db.Column(db.Integer, db.ForeignKey("evaluation_metrics.metric_id"), nullable=False)
    value = db.Column(db.Numeric)


class EvaluationMetrics(db.Model):
    __tablename__ = "evaluation_metrics"
    metric_id = db.Column(db.Integer, primary_key=True)
    metric_name = db.Column(db.String, unique=True, nullable=False)
    script = db.Column(db.String)
