from decouple import config


class Base:
    DEBUG = False
    SECRET_KEY = config("SECRET_KEY", default="kjghlij2hlk35jkl5")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = config("DATABASE_URL")


class Development(Base):
    DEBUG = True


class Production(Base):
    pass
