from flask_restful import fields


category_items_fields = dict(
    id=fields.Integer,
    name=fields.String
)

CATEGORY_FIELDS = dict(
    id=fields.Integer,
    name=fields.String,
    items=fields.List(fields.Nested(category_items_fields))
)
