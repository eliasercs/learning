from utils.db import db
from server import app

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, port=8000)