#!/usr/bin/python3
'''Flask app for states'''


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def statesList():
    state = storage.all(State)
    return render_template('7-states_list.html', States=state)


@app.teardown_appcontext
def teardown(context):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
