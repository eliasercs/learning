import pandas as pd
from flask import Blueprint, jsonify
from utils.db import db
from sqlalchemy.orm import Session

vehicles = Blueprint("vehicles", __name__)
models = []

class Data(db.Model):
    __tablename__ = "data"
    npk = db.Column(db.Integer, primary_key = True)
    id = db.Column(db.String(20))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    velo = db.Column(db.Integer)
    angu = db.Column(db.Integer)
    fecha = db.Column(db.String(10))
    hora = db.Column(db.String(10))
    onoff = db.Column(db.Integer)
    nsat = db.Column(db.Integer)

    def __repr__(self) -> str:
        return super().__repr__()

@vehicles.route("/set-gps", methods=["GET"])
def set_gps():
    df = pd.read_csv("./data/rutas.csv", sep=',')
    for i in df.index:
        print(df['id'][i])
        d = Data(npk=int(df["npk"][i]), id=str(df["id"][i]), lat=df["lat"][i], lon=df["lon"][i], velo=int(df["velo"][i]), angu=int(df["angu"][i]), fecha=df["fecha"][i], hora=df["hora"][i], onoff=int(df["onoff"][i]), nsat=int(df["nsat"][i]))
        db.session.add(d)
    db.session.commit()
    return "Models created"

@vehicles.route("/get-vehicles", methods=["GET"])
def get_vehicles():
    vehicles = []
    data = Data.query.all()
    for d in data:
        if d.id not in vehicles:
            vehicles.append(d.id)
    data = {"id": vehicles}
    return jsonify(data)
    

@vehicles.route("/get-gps/<v>", methods=["GET"])
def get_gps(v):
    gps = []
    data = Data.query.filter_by(id=v).all()
    for e in data:
        gps.append({
            'npk': e.npk,
            "id": e.id,
            "lat": e.lat,
            "lon": e.lon,
            "velo": e.velo,
            "angu": e.angu,
            "fecha": e.fecha,
            "hora": e.hora,
            "onoff": e.onoff,
            "nsat": e.nsat
        })
    print(len(gps))
    return jsonify(gps)