from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.aeropuerto import Aeropuerto, AeropuertoSchema

ruta_Aeropuerto = Blueprint("ruta_aeropuerto", __name__)

Aeropuerto_schema = AeropuertoSchema()
Aeropuertos_schema = AeropuertoSchema(many=True)


@ruta_Aeropuerto.route("/aeropuerto", methods=["GET"])
def aerolinea():
    resultall = Aeropuerto.query.all()  # Select * from Clientes
    resultado_Aerolinea = Aeropuertos_schema.dump(resultall)
    return jsonify(resultado_Aerolinea)


@ruta_Aeropuerto.route("/saveaeropuerto", methods=["POST"])
def save():
    nombre = request.json["nombre_aeropuerto"]
    ciudad = request.json["ciudad"]
    pais = request.json["pais"]
    new_aeropuerto = Aeropuerto(
        nombre,
        ciudad,
        pais,
    )
    db.session.add(new_aeropuerto)
    db.session.commit()
    return "datos guardado con exito"


@ruta_Aeropuerto.route("/updateaeropuerto", methods=["PUT"])
def Update():
    id = request.json["id"]
    nombre = request.json["nombre_aeropuerto"]
    ciudad = request.json["ciudad"]
    pais = request.json["pais"]
    aeropuerto = Aeropuerto.query.get(id)
    if aeropuerto:
        print(aeropuerto)
        aeropuerto.nombre_aeropuerto = nombre
        aeropuerto.ciudad = ciudad
        aeropuerto.pais = pais
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"


@ruta_Aeropuerto.route("/deleteaeropuerto/<id>", methods=["GET"])
def eliminar(id):
    aeropuerto = Aeropuerto.query.get(id)
    db.session.delete(aeropuerto)
    db.session.commit()
    return jsonify(
        Aeropuerto_schema.dump(aeropuerto),
    )
