from flask import request
from flask_restful import Resource, marshal_with
from ..extensions import db
from ..models import ItemModel, CategoryModel
from ..utils.outputs import ITEM_FIELDS


class Items(Resource):

    @marshal_with(ITEM_FIELDS)
    def get(self):
        return ItemModel.query.all()

    @marshal_with(ITEM_FIELDS)
    def post(self):
        item = request.form.to_dict()
        category = CategoryModel.query.filter_by(
                    name=item.get('category')).one()
        item['category'] = category
        new_item = ItemModel(**item)
        db.session.add(new_item)
        db.session.commit()
        return new_item

    def put(self):
        pass

    def delete(self):
        pass
