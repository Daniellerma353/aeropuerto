from flask import Blueprint, request, jsonify, json
from config.db import db, app, ma
from models.reserva import Reserva, ReservasSchema

ruta_reservas = Blueprint("ruta_reserva", __name__)

reserva_schema = ReservasSchema()
reservas_schema = ReservasSchema(many=True)


@ruta_reservas.route("/reserva", methods=["GET"])
def reserva():
    resultall = Reserva.query.all()  # Select * from Clientes
    resultado_reserva = reservas_schema.dump(resultall)
    return jsonify(resultado_reserva)


@ruta_reservas.route("/savereserva", methods=["POST"])
def save():
    idcliente = request.json["idcliente"]
    fecha_reserva = request.json["fecha_reserva"]
    asiento = request.json["asiento"]
    new_reserva = Reserva(
        idcliente,
        fecha_reserva,
        asiento,
    )
    db.session.add(new_reserva)
    db.session.commit()
    return "datos guardado con exito"


@ruta_reservas.route("/deleteReserva/<id>", methods=["GET"])
def delete(id):
    reserva = Reserva.query.get(id)
    db.session.delete(reserva)
    db.session.commit()
    return jsonify(
        reserva_schema.dump(reserva),
    )


@ruta_reservas.route("/updateReserva/<id>", methods=["PUT"])
def update():
    idcliente = request.json["idcliente"]
    fecha_reserva = request.json["fecha_reserva"]
    asiento = request.json["asiento"]
    reserva = Reserva.query.get(id)
    if reserva:
        print(reserva)
        reserva.idcliente = idcliente
        reserva.fecha_reserva = fecha_reserva
        reserva.asiento = asiento
        db.session.commit()
        return "Datos actualizado con exitos"
    else:
        return "Error"
