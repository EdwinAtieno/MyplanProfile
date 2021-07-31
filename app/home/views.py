# app/home/views.py

from flask import render_template,jsonify
from flask_login import login_required

from . import home


@home.route('/')
def homepage():
    """
    Render the homepage templates on the / route
    """
    return render_template('index.html')


@home.route('/dashboard')
#@login_required
def dashboard():
    """
    Render the dashboard templates on the /dashboard route
    """
    return jsonify({'message':'your are now in'})