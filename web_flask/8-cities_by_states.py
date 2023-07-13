#!/usr/bin/python3

"""
Lists all State objects present in DBStorage
sorted by name (A-Z)
"""

from models import storage
from models.state import State
from flask import Flask, request, render_template

app = Flask(__name__)


@app.teardown_appcontext
def tearDown(self):
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def statesList():
    data = storage.all(State).values()
    states = sorted(data, key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
