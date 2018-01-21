Add new washroom
Send POST request to /api/v1/washroom/add
{
    "primary_address": "U of T Bookstore",
	"city": "Toronto",
	"province": "Ontario",
    "postal_code": "M5T 3A1",
	"longitude": -43.6586389,
	"latitude": -79.3992498,
	"comments": "Cool!"
}

Show all existing washrooms
Send GET request to /api/v1/washrooms

Show closest washrooms
Send GET request to /api/v1/washrooms?long=10?lat=10
Example response:

{
    "washrooms": [
        {
            "washroom_id": 1,
            "primary_address": "Bahen Centre for Information Technology",
            "city": "Toronto",
            "province": "Ontario",
            "postal_code": "M2W1W4",
            "longitude": -79.3980115,
            "latitude": -79.3980115,
            "comments": "Cool!",
            "created_at": "2018-01-20 13:11:28.918964"
        },
        {
            "washroom_id": 2,
            "primary_address": "Bahen Centre for Information Technology",
            "city": "Toronto",
            "province": "Ontario",
            "postal_code": "M2W1W4",
            "longitude": -79.3980115,
            "latitude": -79.3980115,
            "comments": "Cool!"
            "created_at": "2018-01-20 13:11:28.918964"
        }]
}

Get particular washroom based on washroom_id
Send GET request tp /api/v1/washroom/washroom_id

Example response:

{
    "washroom_id": 1,
    "primary_address": "Bahen Centre for Information Technology",
    "city": "Toronto",
    "province": "Ontario",
    "postal_code": "M2W1W4",
    "longitude": -79.3980115,
    "latitude": -79.3980115,
    "comments": "Good stuff!",
    "created_at": "2018-01-20 13:11:28.918964",
    "reviews": [
        {
            "review_id": 1,
            "washroom_id": 1,
            "rating": 3,
            "comment": "COol1",
            "created_at": "2018-01-20 13:34:36.818788"
        },
        {
            "review_id": 2,
            "washroom_id": 1,
            "rating": 4,
            "comment": "Testing123",
            "created_at": "2018-01-20 14:30:13.593537"
        }
    ]
}



Add new review
Send POST request to /api/v1/review/add
{
	"rating":5,
	"comment":"cool!!",
	"washroom_id":2
}

