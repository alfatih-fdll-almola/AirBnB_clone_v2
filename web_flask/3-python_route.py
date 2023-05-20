#!/usr/bin/python3
"""Starts a web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Resturn some text"""
    return "Hello BNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns BNB"""
    return "HBNB"


@app.route("/c/<txt>", strict_slashes=False)
def txt(txt):
    """" Returns C is + <txt>"""
    return "C is {}".format(txt.replace("_", " "))


@app.route("/python/", strict_slashes=False, defaults={'txt': 'is cool'})
@app.route("/python/<txt>", strict_slashes=False)
def python(txt):
    """ Return Python is <txt> """
    return "Python {}".format(txt.replace("_", " "))


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
