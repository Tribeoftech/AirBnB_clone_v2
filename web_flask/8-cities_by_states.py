#!/usr/bin/python3
'''Flask app for states'''


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def citiesByStates():
    return render_template('8-cities_by_states.html',
                           states=storage.all(State))


@app.teardown_appcontext
def teardown(context):
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
