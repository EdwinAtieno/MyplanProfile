from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class User(UserMixin, db.Model):
    """
    Create an Users table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(80))

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User: {}>'.format(self.name)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Profile(db.Model):
    """
    Create a Profile table
    """

    __tablename__ = 'Profile'

    id = db.Column(db.Integer, primary_key=True)
    First_name = db.Column(db.String(50))
    Last_name = db.Column(db.String(50))
    User_Name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(50), db.ForeignKey('users.email'))
    City = db.Column(db.String(80))
    Country = db.Column(db.String(80))
    Portfolio = db.Column(db.String(80))
    Bio = db.Column(db.String(500))
    Skills = db.Column(db.String(80))

    def __repr__(self):
        return '<Profile: {}>'.format(self.First_name)


#db.create_all()
