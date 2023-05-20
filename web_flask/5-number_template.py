#!/usr/bin/python3
""" Start a flask web app """
from flask import Flask, render_template
from werkzeug.exceptions import abort

app = Flask(__name__)


@app.route("/")
def hello():
    """Returns Hello HBNB"""
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Return HBNB"""
    return "HBNB"


@app.route("/c/<txt>", strict_slashes=False)
def c(txt):
    """Return C is + <txt>"""
    return f"C is {txt.repalce('_', ' ')}"


@app.route(
    "/python/",
    strict_slashes=False,
    defaults={'txt': 'is cool'}
)
@app.route("/python/<txt>")
def python(txt):
    """Return Python is cool if no argument passed"""
    return f"Python {txt.replace('_', ' ')}"


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """Return n is a number if it is an int"""
    try:
        int(n)
        return f"{n} is a number"

    except ValueError:
        abort(404)


@app.route("/number_template/<n>")
def number_template(n):
    """Return number_template only if n is int"""
    try:
        int(n)
        return render_template("5-number_template.html", n=n)

    except ValueError:
        abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)#!/usr/bin/python3
""" Start a flask web app """
from flask import Flask, render_template
from werkzeug.exceptions import abort

app = Flask(__name__)


@app.route("/")
def hello():
    """Returns Hello HBNB"""
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Return HBNB"""
    return "HBNB"


@app.route("/c/<txt>", strict_slashes=False)
def c(txt):
    """Return C is + <txt>"""
    return f"C is {txt.repalce('_', ' ')}"


@app.route(
    "/python/",
    strict_slashes=False,
    defaults={'txt': 'is cool'}
)
@app.route("/python/<txt>")
def python(txt):
    """Return Python is cool if no argument passed"""
    return f"Python {txt.replace('_', ' ')}"


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    """Return n is a number if it is an int"""
    try:
        int(n)
        return f"{n} is a number"

    except ValueError:
        abort(404)


@app.route("/number_template/<n>")
def number_template(n):
    """Return number_template only if n is int"""
    try:
        int(n)
        return render_template("5-number_template.html", n=n)

    except ValueError:
        abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
