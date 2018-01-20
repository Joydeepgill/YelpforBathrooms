# /api/vi/review/<reviewId>
{
    'id': fields.Integer,
    'rating':fields.Integer,
    'comment':fields.String,
    'created_at':fields.datetime
}


# /api/v1/washroom/<washroomId>
{
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

# /api/v1/washrooms/?long=23.234234234?lat=12.32324234234
{
	'washrooms': [washrooms]
}
