from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from routes.Station import Station
from routes.Vehicles import vehicles
from utils.db import db

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Eliaser/Desktop/Proyecto_4_INFO1128/utils/gps.db'
SQLAlchemy(app)
db.init_app(app)

app.register_blueprint(Station)
app.register_blueprint(vehicles)