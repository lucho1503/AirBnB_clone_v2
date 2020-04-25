#!/usr/bin/python3
""" Create database + start server """
import models
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ function to display a html file """
    states = storage.all(State)
    dictt = {value.id: value.name for value in states.values()}
    return render_template('7-states_list.html', Table="States", my_dict=dictt)


@app.teardown_appcontext
def tear_down(exception):
    """ teardown """
    storage.close()


if __name__ == "__main__":
    """ run application """
    app.run(host='0.0.0.0', port=5000)
