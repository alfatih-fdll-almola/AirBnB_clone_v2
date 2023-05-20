#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    """Returns some text"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Returns some other text"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
