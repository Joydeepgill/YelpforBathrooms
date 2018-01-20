import datetime

from peewee import *

DATABASE = SqliteDatabase("database.db")


class Washroom(Model):

    # Address
    address_for_washroom = IntegerField(unique=True)
    primary_address = CharField()
    city = CharField()
    province = CharField()
    postal_code = CharField()

    # Coordinates
    longitude = DecimalField(max_digits=9, decimal_places=6)
    latitude = DecimalField(max_digits=9, decimal_places=6)

    # Date
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


class Review(Model):
    #washroom = ForeignKeyField(Washroom, related_name="washrooms")
    rating = IntegerField()
    comment = TextField(default="")
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Washroom, Review], safe=True)
    DATABASE.close()
