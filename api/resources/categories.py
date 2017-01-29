from flask import request
from flask_restful import Resource, marshal_with
from ..extensions import db
from ..models import CategoryModel
from ..utils.outputs import CATEGORY_FIELDS
from ..utils.parsers import category_parser


class Categories(Resource):

    @marshal_with(CATEGORY_FIELDS)
    def get(self, id=None):
        return CategoryModel.query.all()

    @marshal_with(CATEGORY_FIELDS)
    def post(self):
        category = category_parser.parse_args()
        new_categoty = CategoryModel(**category)
        db.session.add(new_categoty)
        db.session.commit()
        return new_categoty

    def put(self):
        pass

    def delete(self):
        pass
