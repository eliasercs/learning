from flask import Blueprint, jsonify
import random as ra

Station = Blueprint("Station", __name__)

stations = [
    {"id": 1, "x": -38.738223, "y": -72.601198},
    {"id": 2, "x": -38.725602, "y": -72.573003},
    {"id": 3, "x": -38.734508, "y": -72.583217},
    {"id": 4, "x": -38.731846, "y": -72.605189},
    {"id": 5, "x": -38.731712, "y": -72.588324}
]

@Station.route("/get-stations", methods=["GET"])
def get_stations():
    return jsonify(stations)

@Station.route("/set-data/<id_station>/<number>", methods=["GET"])
def generate_data(id_station, number):
    material = {
        "station_id": id_station,
        "01": [ra.randint(5,20) for e in range(int(number))],
        "25": [ra.randint(5,20) for e in range(int(number))],
        "10": [ra.randint(5,20) for e in range(int(number))],
        "labels": [e for e in range(int(number))]
    }
    if id_station != "0":
        return jsonify(material)
    return jsonify({"msg": "error"})

