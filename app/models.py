from app import db
from datetime import datetime

class Estudiante(db.Model):
    __tablename__ = "estudiantes"

    id       = db.Column(db.Integer, primary_key=True)
    nombre   = db.Column(db.String(100), nullable=False)
    carrera  = db.Column(db.String(100), nullable=False)
    semestre = db.Column(db.Integer, nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id":       self.id,
            "nombre":   self.nombre,
            "carrera":  self.carrera,
            "semestre": self.semestre,
            "fecha_registro": self.fecha_registro.isoformat()
        }