# app/auth/views.py

from flask import flash, redirect, render_template, url_for,jsonify
from flask_login import login_required, login_user, logout_user
from ..auth import forms as fm

from . import profile
from .forms import ProfileForm
from .. import db
from ..models import Profile, profile_schema


@profile.route('/profile', methods=['GET', 'POST'])
def register_profile():
    """Handle requests to the /profile route
        Add a profile to the database through the Profileform form"""
    forms = fm.RegistrationForm
    form = ProfileForm()
    if form.validate_on_submit():
        user = Profile.query.filter_by(email=form.email.data).first()
        if user is not None:
            Profile(First_name=form.First_name.data,
                    Last_name=form.Last_name.data,
                    User_Name=form.User_Name.data,
                    City=form.City.data,
                    Country=form.Country.data,
                    Portfolio=form.Portfolio.data,
                    Bio=form.Bio.data,
                    Skills=form.Skills.data)

            # add employee to the database

            db.session.commit()
            flash('You have successfully updated your profile.')

            # redirect to the login page
            return redirect(url_for('profile.display'))
        else:
            profile = Profile(First_name = form.First_name.data,
                            Last_name =form.Last_name.data,
                            User_Name = form.User_Name.data,
                            email=forms.email.data,
                            City = form.City.data,
                            Country = form.Country.data,
                            Portfolio = form.Portfolio.data,
                            Bio = form.Bio.data,
                            Skills = form.Skills.data)


            # add employee to the database
            db.session.add(profile)
            db.session.commit()
            flash('You have successfully registered! You may now login.')

            # redirect to the login page
            return redirect(url_for('profile.display'))

    # load registration template
    return render_template('dashboard.html', form=form, title='Profile')



@profile.route('/profile_display')
def dispalay():

    """Handle requests to the /profile route
    update an user """
    Profiles = Profile.query.all()
    profile_list = profile_schema(Profiles)
    return jsonify(profile_list)


