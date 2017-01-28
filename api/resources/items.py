from flask_restful import Resource


class Items(Resource):

    def get(self):
        return {1: "hola"}

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
