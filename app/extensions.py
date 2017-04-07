from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension


db = SQLAlchemy()
migrate = Migrate()
toolbar = DebugToolbarExtension()
login_manager = LoginManager()
