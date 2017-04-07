from flask import render_template
from flask_classy import FlaskView
from ..models import CategoryModel, ItemModel


class Main(FlaskView):

    route_base = "/"

    def index(self):
        categories = CategoryModel.query.limit(10).all()
        items = ItemModel.query.order_by('created').limit(10).all()
        return render_template('index.html', categories=categories,
                               items=items)


class Category(FlaskView):

    def get(self, id):
        category = CategoryModel.query.get(id)
        return render_template('category.html', category=category)


class Item(FlaskView):

    def get(self, id):
        item = ItemModel.query.get(id)
        return render_template('item.html', item=item)
