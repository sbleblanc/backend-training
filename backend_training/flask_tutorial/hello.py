from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/")
def index():
    return "Index Page"
