#!/usr/bin/python3
"""
    Creates flask application with routings
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """
        Returns string when route / queried
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """
        Returns string when route/hbnb queried
    """
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
    """
        Returns formed string with passed argument
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """Reformat text based on optional variable
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n=None):
    """
        Returns formed string with integer argument
        only if its and integer
    """
    return str(n) + ' is a number'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
