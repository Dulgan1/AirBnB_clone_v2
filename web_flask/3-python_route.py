#!/usr/bin/python3
"""
    Creates flask application with routings
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """
        Returns string when route / is queried
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
        Returns string when route /hbnb is queried
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """
        Returns formed string with passed argument
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """
        Returns formed srting with optional passed argument
    """
    return "Python " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
