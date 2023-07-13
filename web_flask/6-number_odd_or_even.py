#!/usr/bin/python3

"""
Write a script that starts a Flask web application
"""

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    return "C %s" % str(text.replace("_", " "))


@app.route("/python/<string:text>", strict_slashes=False)
@app.route("/python/")
def python(text="is_cool"):
    return "Python %s" % str(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def intCheck(n):
    return "%d is a number" % (n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def intCheckTemplate(n):
    return render_template('5-number.html', value=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def intOddOrEven(n):
    if n % 2 != 0:
        return render_template('6-number_odd_or_even.html', value=n,
                               sign="odd")
    else:
        return render_template('6-number_odd_or_even.html', value=n,
                               sign="even")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
