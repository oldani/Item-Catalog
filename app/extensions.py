from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# Here are pre configured all the App extensions
api = Api(prefix='/api', catch_all_404s=True)
db = SQLAlchemy()
migrate = Migrate()
toolbar = DebugToolbarExtension()
login_manager = LoginManager()
