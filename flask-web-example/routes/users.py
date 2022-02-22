from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_user
from models.Form.LoginForm import LoginForm
from models.Form.SignUpForm import SignUpForm
from models.users import get_user, _users
from models.User import User
import uuid

users = Blueprint("users",__name__)

@users.route("/signup",methods=["POST","GET"])
def signup_user():
    signup_form = SignUpForm()
    if request.method == "POST":
        if signup_form.validate_on_submit():
            id = uuid.uuid4()
            name = signup_form.name.data
            lastname = signup_form.lastname.data
            username = signup_form.username.data
            email = signup_form.email.data
            password = signup_form.password.data
            user = User(id,name,lastname,username,email,password)
            if user not in _users:
                _users.append(user)
        return redirect(url_for("users.login"))
    return render_template("signup.html", form=signup_form)

@users.route("/login",methods=["POST","GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("users.login"))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.username.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get("next")
            if not next_page:
                next_page = url_for("users.home")
            return redirect(next_page)
    return render_template("login.html", form=form)

@users.route("/home")
def home():
    return render_template("home.html")