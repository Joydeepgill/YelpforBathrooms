from flask import Flask
import db_handler
from flask_restful import Api
from models.review import SpecificReview, ReviewList, InsertReview

endpoint = "/api/v1"

app = Flask(__name__)
api = Api(app)

# Reviews

#GET
api.add_resource(SpecificReview, endpoint + '/review/<int:review_id>')
#POST
api.add_resource(InsertReview, endpoint + '/review/add')
#GET
api.add_resource(ReviewList, endpoint +'/reviews/')



@app.route("/")
def index():
    return "working!"


if __name__ == '__main__':
    db_handler.initialize("database.db")
    app.run(debug=True, port=80, host='0.0.0.0')
