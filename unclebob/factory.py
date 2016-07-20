from flask.app import Flask
from unclebob import config


def create_app(app_name=None):
    app = Flask(app_name or config.PROJECT)
    app.config.from_object(config)

    configure_blueprints(app)

    return app


def configure_blueprints(app):
    from unclebob.api import api

    app.register_blueprint(api)
