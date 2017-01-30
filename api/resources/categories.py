from flask_restful import Resource, marshal_with
from ..extensions import db
from ..models import CategoryModel
from ..utils.outputs import CATEGORY_FIELDS
from ..utils.parsers import category_parser


class Categories(Resource):

    @marshal_with(CATEGORY_FIELDS)
    def get(self, category_id=None):
        if category_id:
            return CategoryModel.query.get_or_404(category_id)
        return CategoryModel.query.all()

    @marshal_with(CATEGORY_FIELDS)
    def post(self):
        category = category_parser.parse_args()
        new_category = CategoryModel(**category)
        db.session.add(new_category)
        db.session.commit()
        return new_category

    @marshal_with(CATEGORY_FIELDS)
    def put(self, category_id):
        category = CategoryModel.query.get_or_404(category_id)
        new_category = category_parser.parse_args()
        category.name = new_category.name
        db.session.commit()
        return category

    def delete(self, category_id):
        category = CategoryModel.query.get_or_404(category_id)
        db.session.delete(category)
        return 200
