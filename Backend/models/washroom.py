from flask_restful import Resource, reqparse, inputs
import json
from flask.ext.api import status

import datetime
import sqlite3
TABLE_NAME = "washrooms"

example = json.dumps({'primary_address': "Bahen Centre for Information Technology", 'longitude':'-79.3980115', 'latitude': '43.6596427'})
example_text = "\n Please refer to example: " + example
class SpecificWashroom(Resource):

    @classmethod
    def find_by_id(cls, washroom_id):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE washroom_id=?".format(table=TABLE_NAME)
        result = cursor.execute(query, (washroom_id,))
        row = result.fetchone()
        #TODO: Join to return reviews
        if row:
            return {"washroom_id":row[0], "primary_address": row[1], 'city': row[2], 'province': row[3], 'postal_code': row[4], 'longitude' :row[5], 'latitude':row[6], 'comments':row[7], 'created_at':row[8]}

    def get(self, washroom_id):
        washroom = self.find_by_id(washroom_id)
        if washroom:
            return washroom
        return status.HTTP_404_NOT_FOUND


class InsertWashroom(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('primary_address',
                        required=True,
                        help="Primary address cannot be left blank" + example_text)
    parser.add_argument('longitude',
                        type=int,
                        required=True,
                        help="Longitude cannot be left blank" + example_text)
    parser.add_argument('latitude',
                        type=int,
                        required=True,
                        help="Latitude id cannot be left blank" + example_text)

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        query = "INSERT INTO {table} VALUES (NULL, ?, ?, ?, ?, ?, ? ,? , ?)".format(table=TABLE_NAME)
        cursor.execute(query, (item['washroom_id'], item['primary_address'], item['city'], item['province'], item['postal_code'], item['longitude'], item['latitude'], item['comment'], item['created_at']))
        connection.commit()
        connection.close()
    def post(self):
        try:
            data = InsertWashroom.parser.parse_args()
        except:
            return example_text

        washroom = {"washroom_id":data["washroom_id"], "primary_address": data["primary_address"], 'city': data["city"], 'province': data["province"], 'postal_code': data["postal_code"], 'longitude' :data['longitude'], 'latitude':data["longitude"], 'comments':data['comments'], 'created_at':datetime.datetime.now()}
        try:
            InsertWashroom.insert(washroom)
        except:
            return status.HTTP_400_BAD_REQUEST
        return status.HTTP_200_OK

class WashroomList(Resource):
    def get(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=TABLE_NAME)
        result = cursor.execute(query)
        fetch = result.fetchall()
        response = []
        for row in fetch:
            response.append({"washroom_id":row[0], "primary_address": row[1], 'city': row[2], 'province': row[3], 'postal_code': row[4], 'longitude' :row[5], 'latitude':row[6], 'comments':row[7], 'created_at':row[8]})
        connection.close()
        return {"washrooms": response}
