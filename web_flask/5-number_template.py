#!/usr/bin/python3
""" this script start a new application flask """


from flask import render_template
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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<py>', strict_slashes=False)
def python_is_cool(py="is_cool"):
    return "Python " + py.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number_int(n):
    if isinstance(n, int):
        return str(n) + " is a number"


@app.route('/number_template/<int:num>', strict_slashes=False)
def num_int(num):
    if isinstance(num, int):
        return render_template('5-number.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
