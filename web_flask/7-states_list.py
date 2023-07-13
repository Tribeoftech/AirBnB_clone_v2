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


@app.route("/states_list", strict_slashes=False)
def statesList():
    objs = storage.all(State)
    obj_list = sorted(objs.values(), key=lambda x: x.name)
    return render_template('7-states_list.html', s=obj_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
