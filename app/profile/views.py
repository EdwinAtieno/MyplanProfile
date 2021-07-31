# app/auth/views.py

from flask import flash, redirect, render_template, url_for,jsonify,request
from flask_login import login_required, login_user, logout_user
from ..auth import forms as fm

from . import profile
from .forms import ProfileForm
from .. import db
from ..models import Profile, Users


@profile.route('/profile', methods=['GET', 'PUT','POST'])
@login_required
def register_profile():
    """Handle requests to the /profile route
        Add a profile to the database through the Profileform form"""

    data = request.get_json()
    user = Profile.query.filter_by(email=data['email']).first()
    if user is None:
       profile = Profile(First_name=data['First_name'],
                              Last_name=data['Last_name'],
                              User_Name=data['User_Name'],
                              email=data['email'],
                              City=data['City'],
                              Country=data['Country'],
                              Portfolio=data['Portfolio'],
                              Bio=data['Bio'],
                              Skills=data['Skills'])

            # add employee to the database
       db.session.add(profile)
       db.session.commit()
       flash('You have successfully registered! You may now login.')

            # redirect to the dashboard page
       return jsonify({"message": "Invalid email or password!"}), 401
    else:
       id = 1
       users = Profile.query.filter_by(email=data['email']).first()
       try:
                users.First_name=data['First_name']
                users.Last_name=data['Last_name']
                users.User_Name=data['User_Name']
                users.email= data['email']
                users.City=data['City']
                users.Country=data['Country']
                users.Portfolio=data['Portfolio']
                users.Bio=data['Bio']
                users.Skills=data['Skills']

            # update profile to the database

                db.session.commit()
                flash('You have successfully updated your profile.')
                return jsonify({"message": "we are good mate"})
       except:
                flash('sorry mate')



    # load registration template
    return redirect(url_for('profile.get_profiles')),200

@profile.route('/profile_details', methods=['GET'])
#@login_required
def get_profiles():

    profiles = Profile.query.all()
    if not profiles:
        return 404
    output = []
    for profile in profiles:
        profile_data = {'user_id': profile.id, 'First_name': profile.First_name, 'Last_name': profile.Last_name,
                        'User_Name': profile.User_Name, 'email': profile.email, 'City': profile.City,
                        'Country': profile.Country, 'Portfolio': profile.Portfolio,'Bio': profile.Bio,'Skills': profile.Skills}
        output.append(profile_data)

    return jsonify({"profiles": output}), 200


