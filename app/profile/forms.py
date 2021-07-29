# app/profile/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import Profile



class ProfileForm(FlaskForm):

    """Form for profile to create new account"""

    First_name = StringField('First_name', validators=[DataRequired()])
    Last_name = StringField('Last_name', validators=[DataRequired()])
    User_Name = StringField('User_Name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    City = StringField('City', validators=[DataRequired()])
    Country = StringField('Country',validators=[DataRequired()])
    Portfolio = StringField('Portfolio', validators=[DataRequired()])
    Bio = StringField('Bio', validators=[DataRequired()])
    Skills = StringField('Skills', validators=[DataRequired()])
    submit = SubmitField('Save/update')



