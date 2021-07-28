# app/auth/views.py

from flask import flash, redirect, render_template, url_for,jsonify,request
from flask_login import login_required, login_user, logout_user
from ..auth import forms as fm

from . import profile
from .forms import ProfileForm
from .. import db
from ..models import Profile, Users


@profile.route('/profile', methods=['GET', 'PUT','POST'])
def register_profile():
    """Handle requests to the /profile route
        Add a profile to the database through the Profileform form"""
    form = ProfileForm()
    if form.validate_on_submit():
        user = Profile.query.filter_by(email=form.email.data).first()
        if user is None:
            profile = Profile(First_name=form.First_name.data,
                              Last_name=form.Last_name.data,
                              User_Name=form.User_Name.data,
                              email=form.email.data,
                              City=form.City.data,
                              Country=form.Country.data,
                              Portfolio=form.Portfolio.data,
                              Bio=form.Bio.data,
                              Skills=form.Skills.data)

            # add employee to the database
            db.session.add(profile)
            db.session.commit()
            flash('You have successfully registered! You may now login.')

            # redirect to the login page
            #return redirect(url_for('profile.display'))
        else:
            id = 1
            users = Profile.query.get_or_404(id)
            try:
                users.First_name=request.form['First_name']
                users.Last_name=request.form['Last_name']
                users.User_Name=request.form['User_Name']
                users.email= request.form['email']
                users.City=request.form['City']
                users.Country=request.form['Country']
                users.Portfolio=request.form['Portfolio']
                users.Bio=request.form['Bio']
                users.Skills=request.form['Skills']

            # update profile to the database

                db.session.commit()
                flash('You have successfully updated your profile.')
            except:
                flash('sorry mate')



    # load registration template
    return render_template('profile.html', form=form, title='Profile')

"""@profile.route('/profile', methods=['GET','PUT', 'POST'])
def update_profile():
    Handle requests to the /profile route
        Add a profile to the database through the Profileform form

    form = ProfileForm()
    if form.validate_on_submit():
        user = Profile.query.filter_by(email=form.email.data).first()
        if user is not None:
            user.data=Profile(First_name=form.First_name.data,
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

        # load registration template
    return render_template('profile.html', form=form, title='Profile')

"""

""""@profile.route('/profile_display', methods=['GET', 'POST'])
def display():

    
    form = prof_disp()
    form.First_name.data=Profile.query.get('First_name')

    return render_template('display.html', title='Profile')"""


