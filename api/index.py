from flask import Flask
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/app/test",methods=["GET"])
def test_reply():
    return {"messgage":"Suscess"}

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'