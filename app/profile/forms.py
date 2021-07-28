# app/profile/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import Profile


class ProfileForm(FlaskForm):

    """Form for profile to create new account"""

    email = StringField('Email', validators=[DataRequired(), Email()])
    name = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password')
                                        ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if Profile.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        if Profile.query.filter_by(name=field.data).first():
            raise ValidationError('Username is already in use.')


class LoginForm(FlaskForm):

    """Form for profile update"""

    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('passwords', validators=[DataRequired()])
    submit = SubmitField('Login')