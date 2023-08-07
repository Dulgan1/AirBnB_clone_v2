#!/usr/bin/python3
"""
    Creates web application with two routings
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """
        Returns string when route queried
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
        Returns string when route queried
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """
        Returns passed as argument with extras
    """
    return 'C ' + text.replace('_', ' ')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
