from decouple import config
from flask_script import Manager, Shell, Server
from flask_migrate import MigrateCommand
from api import create_app
from api.extensions import db
from api.settings import Development, Production


ENVIRONMENT = config("ENVIRONMENT", default="DEV")

if ENVIRONMENT == "DEV":
    app = create_app(Development)
else:
    app = create_app(Production)


manager = Manager(app)


def _make_context():
    return dict(app=app, db=db)


manager.add_command("db", MigrateCommand)
manager.add_command("runserver", Server())
manager.add_command("shell", Shell(make_context=_make_context))


if __name__ == "__main__":
    manager.run()
