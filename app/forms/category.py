from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


class CategoryForm(FlaskForm):
    name = StringField('Category Name', validators=[InputRequired()])
