from flask import jsonify, Blueprint
from flask.ext.restful import Resource, Api, marshal, marshal_with, fields

import models
api_endpoint = '/api/v1/'

washroom_fields = {
    'id': fields.Integer,

    'address_for_washroom': fields.Integer,
    'primary_address' : fields.String,
    'city': fields.String,
    'province': fields.String,
    'postal_code': fields.String,

    'longitude': fields.Integer,
    'latitude': fields.Integer,

    'created_at': fields.DateTime
}

class WashroomList(Resource):

    def get(self):
        washrooms = [marshal(washroom, washroom_fields) for washroom in models.Washroom.select()]
        return jsonify({'washrooms': washrooms})


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
    api_endpoint + 'washrooms',
    endpoint="washroom_list"

)