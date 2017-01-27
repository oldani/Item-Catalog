from flask import Flask
from .extensions import db, migrate, api


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_resources()

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app)
    api.init_app(app)


def register_resources():
    pass
