from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.avion import Avion, AvionSchema

ruta_Avion = Blueprint("ruta_Avion", __name__)

Avion_schema = AvionSchema()
Aviones_schema = AvionSchema(many=True)


@ruta_Avion.route("/avion", methods=["GET"])
def avion():
    resultall = Avion.query.all()  # Select * from Clientes
    resultado_Avion = Aviones_schema.dump(resultall)
    return jsonify(resultado_Avion)


@ruta_Avion.route("/saveavion", methods=["POST"])
def save():
    idaerolinea = request.json["idaerolinea"]
    modelo = request.json["modelo_avion"]
    new_avion = Avion(
        idaerolinea,
        modelo,
    )
    db.session.add(new_avion)
    db.session.commit()
    return "datos guardado con exito"


@ruta_Avion.route("/updateavion", methods=["PUT"])
def Update():
    id = request.json["id"]
    id_aerolinea = request.json["idaerolinea"]
    modelo_avion = request.json["modelo_avion"]
    avion = Avion.query.get(id)
    if avion:
        print(avion)
        avion.idaerolinea = id_aerolinea
        avion.modelo_avion = modelo_avion
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"


@ruta_Avion.route("/deleteavion/<id>", methods=["GET"])
def eliminar(id):
    avion = Avion.query.get(id)
    db.session.delete(avion)
    db.session.commit()
    return jsonify(
        Avion_schema.dump(avion),
    )
