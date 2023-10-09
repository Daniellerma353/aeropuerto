from flask import Flask, jsonify,json
from config.db import  db, ma, app
from api.aeropuerto import Aeropuerto, ruta_Aeropuerto
from api.reserva import Reserva, ruta_reservas
from api.avion import Avion, ruta_Avion
from api.vuelo import Vuelo, ruta_Vuelo
from api.aerolinea import Aerolinea, ruta_Aerolinea
from api.cliente import Cliente, ruta_clientes

app.register_blueprint(ruta_Aeropuerto, url_prefix="/api")
app.register_blueprint(ruta_reservas, url_prefix="/api")
app.register_blueprint(ruta_Avion, url_prefix="/api")
app.register_blueprint(ruta_Vuelo, url_prefix="/api")
app.register_blueprint(ruta_Aerolinea, url_prefix="/api")
app.register_blueprint(ruta_clientes, url_prefix="/api")


@app.route("/")
def index():
    return "Hola Mundo"


@app.route("/cliente-reserva", methods=["GET"])
def clientereserva():
    datos = {}
    resultado = (
        db.session.query(Cliente, Reserva).select_from(Cliente).join(Reserva).all()
    )
    i = 0
    for clientes, reservas in resultado:
        i += 1
        datos[i] = {"cliente": clientes.nombre, "reserva": reservas.id
                    }
    return datos

@app.route("/aerolinea-avion", methods=["GET"])
def aerolineavion():
    datos = {}
    resultado = (
        db.session.query(Aerolinea, Avion).select_from(Aerolinea).join(Avion).all()
    )
    i = 0
    for Aerolinea, Avion in resultado:
        i += 1
        datos[i] = {"aerolinea": Aerolinea.nombre, "avion": Avion.id
                    }
    return datos

@app.route("/varias-tablas", methods=["GET"])
def variastablas():
    datos = {}
    resultado = (
        db.session.query(Cliente, Aeropuerto, Avion, Reserva, Vuelo).select_from(Vuelo).join(Cliente).join(Aeropuerto).join(Avion).join(Reserva).all()
    )
    i = 0
    for Aerolinea, Avion in resultado:
        i += 1
        datos[i] = {"vuelo": Vuelo.id, "avion": Avion.id, "reserva": Reserva.id, "cliente": Cliente.id, "aeropuerto": Aeropuerto.id 
                    }
    return datos

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
