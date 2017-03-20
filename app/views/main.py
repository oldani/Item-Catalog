from flask import render_template
from flask_classy import FlaskView
from ..models import CategoryModel, ItemModel


class Main(FlaskView):

    route_base = "/"

    def index(self):
        categories = CategoryModel.query.all()
        items = ItemModel.query.order_by('created desc').limit(10).all()
        print(categories, items)
        return render_template('index.html', categories=categories,
                               items=items)
