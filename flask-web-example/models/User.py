from utils.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

"""
id
name
lastname
username
email
password
registration_date
"""


class User(UserMixin):

    is_authenticated = False
    is_active = True
    is_anonymous = False


    def __init__(self, id, name, lastname, username, email, password, is_admin=False) -> None:
        self.id = id
        self.name = name
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin

    def set_password(self,password):
        self.password = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password, password)

    def __repr__(self) -> str:
        return "<User {}>".format(self.username)