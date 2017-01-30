from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api


db = SQLAlchemy()
migrate = Migrate()
api = Api(prefix="/api", catch_all_404s=True)
