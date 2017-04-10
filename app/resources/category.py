from flask_restful import Resource, marshal_with, abort
from ..models import CategoryModel
from ..utils.outputs import CATEGORY_FIELDS


class Categories(Resource):

    @marshal_with(CATEGORY_FIELDS)
    def get(self, category_id=None):
        if category_id:
            category = CategoryModel.query.get(category_id)
            if not category:
                return abort(404, message="This category does not exist.")
            return category
        return CategoryModel.query.all()
