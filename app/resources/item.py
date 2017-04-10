from flask_restful import Resource, marshal_with
from ..models import ItemModel
from ..utils.outputs import ITEM_FIELDS
from ..utils.parsers import item_get_parser


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
