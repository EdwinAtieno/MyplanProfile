from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager,ma



class Users(db.Model, UserMixin):
    """
    Create an Users table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(80), nullable=False)

    """@property
    def password(self):
        
        Prevent passwords from being accessed
                raise AttributeError('passwords is not a readable attribute.')


        

    @password.setter
    def password(self, password):
        
        Set password to a hashed password
        
        self.password_hash = generate_password_hash(password)"""
    def verify_password(self, password):
        """ Check if hashed passwords matches actual passwords"""
        self.password_hash = generate_password_hash(password)

        return check_password_hash(self.password_hash, password)
    """def __init__(self, email, name, password_hash):
        self.email = email
        self.name = name
        self.password = password_hash"""

    def __repr__(self):
        return '<User: {}>'.format(self.name)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('email','name','password')

user_schema = UserSchema(many=True)






# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Profile(db.Model):
    """
    Create a Profile table
    """

    __tablename__ = 'Profile'

    id = db.Column(db.Integer, primary_key=True)
    First_name = db.Column(db.String(50))
    Last_name = db.Column(db.String(50))
    User_Name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(50), db.ForeignKey('Users.email'))
    City = db.Column(db.String(80))
    Country = db.Column(db.String(80))
    Portfolio = db.Column(db.String(80))
    Bio = db.Column(db.String(500))
    Skills = db.Column(db.String(80))

    def __init__(self, First_name, Last_name, User_Name,email,City,Country,Portfolio,Bio,Skills):
        self.First_name = First_name
        self.Last_name = Last_name
        self.User_Name = User_Name
        self.email = email
        self.City = City
        self.Country = Country
        self.Portfolio = Portfolio
        self.Bio = Bio
        self.Skills = Skills





    def __repr__(self):
        return '<Profile: {}>'.format(self.First_name)


class ProfileSchema(ma.Schema):
    class Meta:
        fields = ('First_name', 'Last_name', 'User_Name', 'City','Country','Portfolio','Bio','Skills')

profile_schema = ProfileSchema(many=True)

