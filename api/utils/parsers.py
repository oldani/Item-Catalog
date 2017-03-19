from flask_restful.reqparse import RequestParser


def description_validator(value):
    """ Validate that the given description is large enough. """
    if len(value) < 10:
        raise ValueError("The Item description must be a least 10 chars length.")
    return value

# Required params for new category
category_parser = RequestParser()
category_parser.add_argument('name', required=True, location='form',
                             help="A category name is required.")

# Required params for new item
item_parser = RequestParser()
item_parser.add_argument('name', required=True, location='form',
                         help="A item name is required.")

item_parser.add_argument('description', required=True, location='form',
                         type=description_validator)

item_parser.add_argument('category', required=True, location='form',
                         help="Must supply wich is the category of the item.")

# Request parser for Get method in Item Resourse
item_get_parser = RequestParser()
item_get_parser.add_argument('sort_by', type=str)
item_get_parser.add_argument('order', type=str, default="asc")
