import email
from unicodedata import name
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    lastname = StringField("Lastname",validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    email = EmailField("Email",validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("submit")