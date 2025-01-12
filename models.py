from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

# Create SQLAlchemy instance
db = SQLAlchemy()

# User Model
class Usuario(db.Model):
    __tablename__ = 'Usuarios'  # Use existing table
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)
    creado_en = db.Column(db.DateTime, default=text('GETDATE()'), nullable=False)
