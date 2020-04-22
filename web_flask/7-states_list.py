#!/usr/bin/python3
""" start a application web flask """


from models import storage
from models.state import State
from flask import render_template, Flask

app = Flask(__name__)


@app.teardown_appcontext
def tear_down(exception):
    """ close session SQLalchemy """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ list states for id : name and display in html file"""
    states = storage.all(State)
    dictt = {value.id: value.name for value in states.values()}
    return render_template('7-states_list.html', Table="States", my_dict=dictt)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
