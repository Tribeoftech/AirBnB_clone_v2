#!/usr/bin/python3

""" Start a Flask web application """

from flask import Flask


def StartFlask():
    """ Start a Flask web application """
    app = Flask(__name__)

    @app.route('/', strict_slashes=False)
    def hello():
        """ Display 'Hello HBNB!' """
        return 'Hello HBNB!'

    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    StartFlask()
