from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired
from ..models import CategoryModel


class ItemForm(FlaskForm):
    """ Form for Items. """
    name = StringField('Name', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    category_id = SelectField('Category', coerce=int,
                              validators=[InputRequired()])

    def __init__(self, *args, **kwargs):
        """ Load all categories, to be rendered in the select field. """
        super().__init__(*args, **kwargs)
        self.category_id.choices = [(c.id, c.name) for c in CategoryModel.query.all()]
