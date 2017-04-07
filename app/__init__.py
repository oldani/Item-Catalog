from flask import Flask
from . import views
from .extensions import db, migrate, toolbar, login_manager


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_views(app)
    register_extensions(app)

    return app


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    toolbar.init_app(app)


def register_views(app):
    views.Main.register(app)
    views.Category.register(app)
    views.Item.register(app)
    views.Login.register(app)
