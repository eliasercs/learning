from flask import Flask
from routes.users import users
from flask_login import LoginManager
from models.users import _users

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    for user in _users:
        if user.id == user_id:
            return user
    return None

app = Flask(__name__)
app.config["SECRET_KEY"] = "08876155ae3bccc5fbc6383876c3ebc27c67a689970abc10f5b02d344181859d"

login_manager.init_app(app)

app.register_blueprint(users)

if __name__ == "__main__":
    app.run(debug=True,port=4000)