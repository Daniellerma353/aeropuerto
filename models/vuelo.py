from config.db import db, ma, app


class Vuelo(db.Model):
    __tablename__ = "tblvuelo"
    id = db.Column(db.Integer, primary_key=True)
    idreserva = db.Column(db.Integer, db.ForeignKey("tblreserva.id"))
    idavion = db.Column(db.Integer, db.ForeignKey("tblavion.id"))
    idaeropuerto = db.Column(db.Integer, db.ForeignKey("tblaeropuerto.id"))

    def __init__ (self, idreserva, idavion, ideropuerto):
        self.idreserva = idreserva
        self.idavion = idavion
        self.idaeropuerto = ideropuerto

with app.app_context():
    db.create_all()


class VueloSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "idreserva",
            "idavion",
            "idaeropuerto",
        )
