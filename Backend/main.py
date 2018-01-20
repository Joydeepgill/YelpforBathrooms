from flask import Flask
import models
from resources.washrooms import washrooms_api

app = Flask(__name__)
app.register_blueprint(washrooms_api)


@app.route("/")
def index():
    return "working!"


if __name__ == '__main__':
    models.initialize()
    app.run(debug=True, port=8000, host='0.0.0.0')
