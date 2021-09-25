from flask import Flask

app = Flask(__name__)


@app.route("/")
def hell_world():
    return "Hello world!"


@app.route("/api/authenticate")
def authenticate():
    return "User authenticated"

