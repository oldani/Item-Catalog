from ..extensions import db


class Category(db.Model):
    """ Categories model. """

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('categories', lazy='joined'))

    def __repr__(self):
        return "Category: {}".format(self.name)

    @classmethod
    def add(cls, **kwargs):
        new = cls(**kwargs)
        db.session.add(new)
        db.session.commit()
        return new
