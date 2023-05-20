#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Returns some text"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns some other text"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Returns some other text"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
