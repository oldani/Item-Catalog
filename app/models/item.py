from ..extensions import db
from datetime import datetime


class Item(db.Model):
    """ Items model. """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    description = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now)
    edited = db.Column(db.DateTime, default=datetime.now,
                       onupdate=datetime.now)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('items',
                               lazy='joined'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('items', lazy='joined'))

    def __repr__(self):
        return "<Item: {}".format(self.name)

    @classmethod
    def add(cls, **kwargs):
        new = cls(**kwargs)
        db.session.add(new)
        db.session.commit()
        return new

    def update(self):
        """ If the instace have been mutated or updated, commit the session
            to save the changes. """
        db.session.commit()

    def delete(self):
        """ Delete the instance reference from db and commit the session. """
        db.session.delete(self)
        db.session.commit()
