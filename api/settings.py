from decouple import config


class Base:
    DEBUG = True
    SECRET_KEY = config("SECRET_KEY", default="kjghlij2hlk35jkl5")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = config("SQLALCHEMY_DATABASE_URI")


class Development(Base):
    DEBUG = True


class Production(Base):
    pass
