#!/usr/bin/python3
"""
    Creates flask application with routings
"""

from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """
        Returns string when route / is queried
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
        Returns string when route /hbnb queried
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """
        Returns formed string wotg passed argument
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """
        Returns formed string with optional passed argument
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n=None):
    """
        Returns formed string with integer n if its an integer
    """
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    """
        Retrieves and render template for request
    """
    temp = '5-number.html'
    return render_template(temp, n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
