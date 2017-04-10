from flask_restful.reqparse import RequestParser


# Request parser for Get method in Item Resourse
item_get_parser = RequestParser()
item_get_parser.add_argument('sort_by', type=str)
item_get_parser.add_argument('order', type=str, default="asc")
