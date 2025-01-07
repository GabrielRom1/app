from . import db
# from flask_login import UserMixin #para manejo de usuarios
from sqlalchemy.sql import func


# Tabla de Administradores del sistema
class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))



class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))



#  en el tutotial aparece otra clase de Note
# ver que es ForeignKey**
# ver como funciona db.relationship