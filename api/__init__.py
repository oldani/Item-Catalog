from flask import Flask
from . import resources
from .extensions import db, migrate, api


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_resources()
    register_extensions(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app)
    api.init_app(app)


def register_resources():
    api.add_resource(resources.Categories, '/categories',
                     '/categories/<int:id>')
