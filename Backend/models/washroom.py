from flask_restful import Resource, reqparse, inputs
import json
from flask.ext.api import status

import datetime
import sqlite3

TABLE_NAME = "washrooms"

example = json.dumps({
    "primary_address": "U of T Bookstore",
    "city": "Toronto",
    "province": "Ontario",
    "postal_code": "M5T 3A1",
    "longitude": -43.6586389,
    "latitude": -79.3992498,
    "comments": "Good stuff!"
})
example_text = "\n Please refer to example: " + example


class SpecificWashroom(Resource):
    parser = reqparse.RequestParser()
    @classmethod
    def retrieve_reviews(cls, washroom_id):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        query = "SELECT * FROM reviews WHERE washroom_id =?;"
        results = cursor.execute(query, (washroom_id,)).fetchall()
        response = []
        for row in results:
            response.append({"review_id": row[0], 'washroom_id': row[1], 'rating': row[2], 'comment': row[3],
                    'created_at': row[4]})
        return response

    @classmethod
    def find_by_id(cls, washroom_id):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE washroom_id=?;".format(table=TABLE_NAME)
        result = cursor.execute(query, (washroom_id,))
        row = result.fetchone()
        if row:
            return {"washroom_id": row[0], "primary_address": row[1], 'city': row[2], 'province': row[3],
                    'postal_code': row[4], 'longitude': row[5], 'latitude': row[6], 'comments': row[7],
                    'created_at': row[8], "reviews": cls.retrieve_reviews(row[0])}

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
                        type=float,
                        required=True,
                        help="Longitude cannot be left blank" + example_text)
    parser.add_argument('latitude',
                        type=float,
                        required=True,
                        help="Latitude id cannot be left blank" + example_text)
    parser.add_argument('city')
    parser.add_argument('province')
    parser.add_argument('postal_code')
    parser.add_argument('comments')

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        query = "INSERT INTO {table} VALUES (NULL, ?, ?, ?, ?, ?, ? ,? , ?)".format(table=TABLE_NAME)
        cursor.execute(query, (
        item['primary_address'], item['city'], item['province'], item['postal_code'], item['longitude'],
        item['latitude'], item['comments'], item['created_at']))
        connection.commit()
        connection.close()

    def post(self):
        try:
            data = InsertWashroom.parser.parse_args()
        except:
            return example_text, status.HTTP_400_BAD_REQUEST

        washroom = {"primary_address": data["primary_address"], "city": data["city"], "province": data["province"],
                    "postal_code": data["postal_code"], "longitude": data["longitude"], "latitude": data["longitude"],
                    "comments": data["comments"], "created_at": datetime.datetime.now()}
        try:
            InsertWashroom.insert(washroom)
        except:
            return status.HTTP_400_BAD_REQUEST
        return status.HTTP_200_OK


class WashroomList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("long", float)
    parser.add_argument("lat", float)

    def get(self):
        finding_closest = True
        try:
            args = WashroomList.parser.parse_args()
            start_lat = args["lat"]
            start_long = args["long"]
        except:
            finding_closest = False


        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        query = "SELECT * FROM {table}".format(table=TABLE_NAME)

        if(finding_closest):
            query = "SELECT * FROM {table}".format(table=TABLE_NAME)
            #print("lat = " + str(start_lat) + "lng = " + str(start_long))
            ##SQL Closest based on long and lat
            #query = "SELECT latitude, longitude, SQRT(POW(69.1 * (latitude - [{start_lat}]), 2) + POW(69.1 * ([{start_lng}] - longitude) * COS(latitude / 57.3), 2)) AS distance FROM washrooms ORDER BY distance;".format(start_lat=start_lat, start_lng=start_long)
        else:
            query = "SELECT * FROM {table}".format(table=TABLE_NAME)
        result = cursor.execute(query)
        fetch = result.fetchall()
        response = []
        for row in fetch:
            response.append({"washroom_id": row[0], "primary_address": row[1], 'city': row[2], 'province': row[3],
                             'postal_code': row[4], 'longitude': row[5], 'latitude': row[6], 'comments': row[7],
                             'created_at': row[8]})
        connection.close()
        return {"washrooms": response}
