#!/usr/bin/python3
""" this script start a new application flask """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """ print Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ print HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return "C " + text.replace("_", " ")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
