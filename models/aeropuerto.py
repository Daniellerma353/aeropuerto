from config.db import db, ma, app


class Aeropuerto(db.Model):
    __tablename__ = "tblaeropuerto"

    id = db.Column(db.Integer, primary_key=True)
    nombre_aeropuerto = db.Column(db.String(70))
    ciudad = db.Column(db.String(70))
    pais = db.Column(db.String(70))

    def __init__(self, nombre_aeropuerto, ciudad, pais):
        self.nombre_aeropuerto = nombre_aeropuerto
        self.ciudad = ciudad
        self.pais = pais

with app.app_context():
    db.create_all()


class AeropuertoSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "nombre_aeropuerto",
            "ciudad",
            "pais",
        )
