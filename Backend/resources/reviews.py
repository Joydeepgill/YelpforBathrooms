from flask import jsonify, Blueprint
from flask.ext.restful import Resource, Api, marshal, marshal_with, fields, reqparse

import models
api_endpoint = '/api/v1/'

review_fields = {
    'id': fields.Integer,
    'rating':fields.Integer,
    'comment':fields.String,
    'created_at':fields.datetime
}

class ReviewList(Resource):

    def get(self):
        reviews = [marshal(review, review) for review in models.Review.select()]
        return jsonify({'washrooms': reviews})


class Review(Resource):
    def get(self, id):
        return jsonify({'review': id})

    def delete(self, id):
        return jsonify({'review': ''})

    def post(self, id):
        args =
        return


reviews_api = Blueprint('resources.washrooms', __name__ )
api = Api(reviews_api)
api.add_resource(
    Review,
    api_endpoint + 'review/<int:id>',
    endpoint='review'
)
api.add_resource(
    ReviewList,
    api_endpoint + "reviews",
    endpoint="reviews"
)