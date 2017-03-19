from flask_restful import Resource, marshal_with
from ..extensions import db
from ..models import ItemModel, CategoryModel
from ..utils.outputs import ITEM_FIELDS
from ..utils.parsers import item_parser, item_get_parser


class Items(Resource):

    @marshal_with(ITEM_FIELDS)
    def get(self, item_id=None):
        result = None
        if item_id:
            result = ItemModel.query.get_or_404(item_id)
        params = item_get_parser.parse_args()
        if params:
            if params.get('sort_by'):
                query = '{sort_by} {order}'.format(**params)
                result = ItemModel.query.order_by(query).all()
        return result if result else ItemModel.query.all()

    @marshal_with(ITEM_FIELDS)
    def post(self):
        item = item_parser.parse_args()
        category = CategoryModel.query.filter_by(
                    name=item.category).one()
        item.category = category
        new_item = ItemModel(**item)
        db.session.add(new_item)
        db.session.commit()
        return new_item

    @marshal_with(ITEM_FIELDS)
    def put(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        new_item = item_parser.parse_args()
        category = CategoryModel.query.filter_by(
                    name=new_item.category).one()
        item.name = new_item.name
        item.description = new_item.description
        item.category = category
        db.session.commit()
        return item

    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return 200
