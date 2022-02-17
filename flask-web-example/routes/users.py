from datetime import datetime
from flask import Blueprint, make_response, request, abort
from models.User import User

users = Blueprint("users",__name__)

@users.route("/register",methods=["POST"])
def register_new_user():

    name = request.form.get("name")
    lastname = request.form.get("lastname")
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    registration_date = datetime.now().strftime("%Y-%m-%d")

    print(registration_date)

    user = User(name,lastname,username,email,password,registration_date)
    if user.search_user(username)==0:
        user.add_user()
        return make_response("Ok",200,{"Content-Type":"text/plain"})
    else:
        return make_response("Error",200,{"Content-Type":"text/plain"})