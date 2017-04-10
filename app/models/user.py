from flask_login import UserMixin
from ..extensions import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    picture = db.Column(db.String(250))

    def __repr__(self):
        return "<User: {}>".format(self.name)

    @classmethod
    def add(cls, **kwargs):
        new = cls(**kwargs)
        db.session.add(new)
        db.session.commit()
        return new
