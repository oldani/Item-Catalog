from flask_restful import Resource


class Categories(Resource):

    def get(self, id=None):
        return {'hey': 1}

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
