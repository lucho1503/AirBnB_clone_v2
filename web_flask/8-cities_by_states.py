#!/usr/bin/python3
# starts a web application flask and display states and cities

from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def close_sesion(exception):
    """ close the session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_of_states():
    """ list cities by states and render template in file .html"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html',
                           Table="States", states=states)

if __name__ == "__main__":
    """ run application """
    app.run(host='0.0.0.0', port=5000)
