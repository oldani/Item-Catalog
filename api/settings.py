from decouple import config


class Base:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = config("SQLALCHEMY_DATABASE_URI")


class Development(Base):
    DEBUG = True


class Production(Base):
    pass
