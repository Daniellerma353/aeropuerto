from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.vuelo import Vuelo, VueloSchema
from models.reserva import Reserva, ReservasSchema
from models.avion import Avion, AvionSchema

ruta_Vuelo = Blueprint("ruta_Vuelo", __name__)

Vuelo_schema = VueloSchema()
Vuelos_schema = VueloSchema(many=True)


@ruta_Vuelo.route("/vuelo", methods=["GET"])
def vuelo():
    resultall = Vuelo.query.all()  # Select * from Clientes
    resultado_Vuelo = Vuelos_schema.dump(resultall)
    return jsonify(resultado_Vuelo)


@ruta_Vuelo.route("/saveVuelo", methods=["POST"])
def save():
    id_reserva = request.json["idreserva"]
    id_avion = request.json["idavion"]
    id_aeropuerto = request.json["idaeropuerto"]
    new_Vuelo = Vuelo(
        id_reserva,
        id_avion,
        id_aeropuerto,
    )
    db.session.add(new_Vuelo)
    db.session.commit()
    return "datos guardado con exito"


@ruta_Vuelo.route("/deleteVuelo/<id>", methods=["GET"])
def delete(id):
    Vuelo = Vuelo.query.get(id)
    db.session.delete(Vuelo)
    db.session.commit()
    return "datos eliminado con exito"


@ruta_Vuelo.route("/updatevuelo/<id>", methods=["PUT"])
def update(id):
    id_reserva = request.json["idreserva"]
    id_avion = request.json["idavion"]
    id_aeropuerto = request.json["idaeropuerto"]
    vuelo = Vuelo.query.get(id)
    if vuelo:
        print(vuelo)
        Vuelo.idreserva = id_reserva
        Vuelo.idavion = id_avion
        Vuelo.idaeropuerto = id_aeropuerto
        db.session.commit()
        return "datos actualizado con exito"
    else: 
        return "Error"
