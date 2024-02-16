#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """define to display what it's returning"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """define to display what it's returning"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """define to display what it's returning"""
    return 'C {}'.format(escape(text.replace('_', ' ')))


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """define to display what it's returning"""
    return 'Python {}'.format(escape(text.replace('_', ' ')))


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    """define to display what it's returning"""
    return '{} is a number'.format(escape(n))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
