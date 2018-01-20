from flask import jsonify, Blueprint
from flask.ext.restful import Resource, Api

import models
api_endpoint = '/api/v1/'


class WashroomList(Resource):
    def get(self):
        return jsonify({'washrooms': ''})


class Washroom(Resource):
    def get(self, id):
        return jsonify({'washroom': id})

    def delete(self, id):
        return jsonify({'washroom': ''})


washrooms_api = Blueprint('resources.washrooms', __name__ )
api = Api(washrooms_api)
api.add_resource(
    Washroom,
    api_endpoint + 'washrooms/<int:id>',
    endpoint='washroom'
)
api.add_resource(
    WashroomList,
    api_endpoint + '/',
    endpoint="washroom_list"

)