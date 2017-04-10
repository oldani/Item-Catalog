from flask_restful import fields

# Serializer for items list in categories response
category_items_fields = dict(
    id=fields.Integer,
    name=fields.String
)

# Serializer for categories response
CATEGORY_FIELDS = dict(
    id=fields.Integer,
    name=fields.String,
    items=fields.List(fields.Nested(category_items_fields))
)

# Serializer for items response
ITEM_FIELDS = dict(
    id=fields.Integer,
    name=fields.String,
    description=fields.String,
    created=fields.DateTime,
    edited=fields.DateTime,
    category=fields.String(attribute='category.name')
)
