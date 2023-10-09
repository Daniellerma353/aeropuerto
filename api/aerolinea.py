from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.aerolinea import Aerolinea, AerolineaSchema

ruta_Aerolinea = Blueprint("ruta_Aerolinea", __name__)

Aerolinea_schema = AerolineaSchema()
Aerolineas_schema = AerolineaSchema(many=True)


@ruta_Aerolinea.route("/aerolinea", methods=["GET"])
def aerolinea():
    resultall = Aerolinea.query.all()  # Select * from Clientes
    resultado_Aerolinea = Aerolineas_schema.dump(resultall)
    return jsonify(resultado_Aerolinea)


@ruta_Aerolinea.route("/saveaerolinea", methods=["POST"])
def save():
    nombre = request.json["nombre"]
    new_aerolinea = Aerolinea(nombre)
    db.session.add(new_aerolinea)
    db.session.commit()
    return "datos guardado con exito"


@ruta_Aerolinea.route("/updateaerolinea", methods=["PUT"])
def Update():
    id = request.json["id"]
    nombre = request.json["nombre"]
    aerolinea = Aerolinea.query.get(id)
    if aerolinea:
        print(aerolinea)
        aerolinea.nombre = nombre
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"


@ruta_Aerolinea.route("/deleteaerolinea/<id>", methods=["DELETE"])
def eliminar(id):
    aerolinea = Aerolinea.query.get(id)
    db.session.delete(aerolinea)
    db.session.commit()
    return jsonify(
        Aerolinea_schema.dump(aerolinea),
    )
