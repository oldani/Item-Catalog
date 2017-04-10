from flask import Flask
from . import resources
from . import views
from .extensions import db, migrate, toolbar, login_manager, api


def create_app(config):
    """ App factory func. """
    app = Flask(__name__)
    app.config.from_object(config)
    register_resources()
    register_views(app)
    register_extensions(app)

    return app


def register_extensions(app):
    """ Registter all the extensions with the current app. """
    api.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    toolbar.init_app(app)


def register_views(app):
    """ Register FlaskViews views. """
    views.Main.register(app)
    views.Category.register(app)
    views.Item.register(app)
    views.Login.register(app)


def register_resources():
    """ Register resources and add url. """
    # Rources have been created since once review pass
    # this project is going to be api with a SPA
    api.add_resource(resources.Categories, '/categories',
                     '/categories/<int:category_id>')
    api.add_resource(resources.Items, '/items',
                     '/items/<int:item_id>')