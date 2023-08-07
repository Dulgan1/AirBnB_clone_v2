#!/usr/bin/python3
"""
Creates flask application with two routings
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """Returns string when route /
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Returns string when route /hbnb
    """
    return "HBNB"

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
