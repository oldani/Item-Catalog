from ..extensions import db
from datetime import datetime


class Item(db.Model):

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
