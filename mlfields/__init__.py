import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    db_path = "{}/mlfields.db".format(app.instance_path)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World'

    from .data_models import db
    db.init_app(app)
    with app.app_context():
        db.create_all()

    from . import project
    app.register_blueprint(project.bp)

    return app
