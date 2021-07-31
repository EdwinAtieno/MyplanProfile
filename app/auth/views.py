# app/auth/views.py

from flask import flash, redirect, render_template, url_for,request,jsonify
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token,create_refresh_token
from flask_jwt_extended import unset_jwt_cookies
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db,cors, cross_origin
from ..models import Users


@auth.route('/register', methods=['GET', 'POST'])
@cross_origin()
def register():
    """
    Handle requests to the /register route
    Add an user to the database through the registration form
    """

    data = request.get_json()
    if data['email'] is None or data['password'] is None:
        return 400  # missing arguments
    if Users.query.filter_by(email=data['email']).first() is not None:
        return 400  # existing user
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = Users(email=data['email'], name=data['name'], password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'username': new_user.name}), 201



@auth.route('/login', methods=['GET','POST'])
@cross_origin()
def login():
    """
    Handle requests to the /login route
    Log an user in through the login form
    """
    data = request.get_json()
    user = Users.query.filter_by(email=data["email"]).first()
    if not user:
        return jsonify({"message": "Invalid email or password!"})
    if check_password_hash(user.password_hash, data['password']):

       """ return redirect(url_for('home.dashboard')),200"""
       access_token = create_access_token(identity = data["email"])
       return jsonify({"access_token": access_token})

    return jsonify({"message": "Invalid email or password!"}), 401

@auth.route('/refresh', methods=['GET','POST'])
@jwt_required(refresh=True)
@cross_origin()
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify(access_token=access_token)


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an user out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)

    # redirect to the login page
    return redirect(url_for('auth.login'))