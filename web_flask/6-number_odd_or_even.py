#!/usr/bin/python3
"""
    Creates flask application with routings and rendering
"""
from flask import Flask, render_template
app.url_map.strict_slashes = False
app = Flask(__name__)


@app.route('/')
def hello():
    """
        Returns string when route /
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
        Returns string when requesting /hbnb
    """
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
    """
        Returns formed string with oassdd argument
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """
        Returns formed string with optional argument
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n=None):
    """
        Returns formed string with passedd integer argument
        only if argument is integer
    """
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    """Retrieves and renders template for request
    """
    temp = '5-number.html'
    return render_template(temp, n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Retrieves and render template based on conditional
    """
    temp = '6-number_odd_or_even.html'
    return render_template(temp, n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
