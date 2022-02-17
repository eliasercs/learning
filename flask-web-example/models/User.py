from utils.db import db
from werkzeug.security import generate_password_hash, check_password_hash

class User:

    user_query = (
        "INSERT INTO users "
        "(name,lastname,username,email,password,registration_date) "
        "VALUES(%(name)s,%(lastname)s,%(username)s,%(email)s,%(password)s,%(registration_date)s)"
    )

    user_data = {
        "name": "",
        "lastname": "",
        "username": "",
        "email": "",
        "password": "",
        "registration_date": ""
    }

    search_user_query = ("SELECT * FROM users WHERE username=%s")

    def __init__(self,**args) -> None:
        self.cursor = db.cursor()
        if len(args)==0:
            self.user_data["name"] = ""
            self.user_data["lastname"] = ""
            self.user_data["username"] = ""
            self.user_data["email"] = ""
            self.user_data["password"] = ""
            self.user_data["registration_date"] = ""
        elif len(args)==6:
            self.user_data["name"] = args["name"]
            self.user_data["lastname"] = args["lastname"]
            self.user_data["username"] = args["username"]
            self.user_data["email"] = args["email"]
            self.user_data["password"] = self.hash_password(args["password"])
            self.user_data["registration_date"] = args["registration_date"]

    def add_user(self):
        self.cursor.execute(self.user_query,self.user_data)
        db.commit()
        self.cursor.close()

    def search_user(self,username):
        self.cursor.execute(self.search_user_query,(username,))
        result = self.cursor.fetchall()
        return len(result)

    def hash_password(self,password):
        return generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.user_data["password"],password)