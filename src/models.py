from . import db
from datetime import datetime

class Auto(db.Model):
    __tablename__ = 'autos'

    id = db.Column(db.Integer, primary_key =  True)
    modelo = db.Column(db.String(50), nullable = False)
    patente = db.Column(db.String(50), nullable = False)
    cant_horas = db.Column(db.Integer, nullable = False)
    image_url = db.Column(db.String(200), nullable = True)
    

    
    

    def __repr__(self) -> str:
        return f"<Auto {self.modelo} {self.patente} {self.cant_horas}>"
    
    

