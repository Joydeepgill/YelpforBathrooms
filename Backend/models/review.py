from flask_restful import Resource, reqparse, inputs
import json
from flask.ext.api import status

import datetime
import sqlite3
TABLE_NAME = "reviews"

example = json.dumps({'rating': 5, 'comment':'very nice', 'washroom_id':123})
example_text = "\n Please refer to example: " + example
class SpecificReview(Resource):

    @classmethod
    def find_by_id(cls, review_id):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE review_id=?".format(table=TABLE_NAME)
        result = cursor.execute(query, (review_id,))
        row = result.fetchone()
        if row:
            return {"review_id": row[0], 'washroom_id': row[1], 'rating': row[2], 'comment': row[3],
                    'created_at': row[4]}

    def get(self, review_id):
        review = self.find_by_id(review_id)
        if review:
            print("Found")
            return review
        return status.HTTP_404_NOT_FOUND


class InsertReview(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('comment',
                        required=True,
                        help="Comment cannot be left blank" + example_text)
    parser.add_argument('rating',
                        type=int,
                        required=True,
                        help="Rating cannot be left blank" + example_text)
    parser.add_argument('washroom_id',
                        type=int,
                        required=True,
                        help="Washroom id cannot be left blank" + example_text)

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        query = "INSERT INTO {table} VALUES (NULL, ?, ?, ?, ?)".format(table=TABLE_NAME)
        cursor.execute(query, (item['washroom_id'], item['rating'], item['comment'], item['created_at']))
        connection.commit()
        connection.close()
    def post(self):
        try:
            data = InsertReview.parser.parse_args()
        except:
            return example_text

        review = {'washroom_id': data['washroom_id'], 'rating': data['rating'], 'comment': data['comment'],
                  'created_at': datetime.datetime.now()}
        print(review)
        InsertReview.insert(review)
        return status.HTTP_200_OK

class ReviewList(Resource):
    def get(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=TABLE_NAME)
        result = cursor.execute(query)
        fetch = result.fetchall()
        response = []
        for row in fetch:
            response.append({"review_id": row[0], 'washroom_id': row[1], 'rating': row[2], 'comment': row[3],
                    'created_at': row[4]})
        connection.close()
        return {"reviews": response}
