from ..extensions import db


class Category(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return "Category: {}".format(self.name)
