from flask import Blueprint, render_template, redirect, url_for
from .models import Admin

#se va a definir los blueprints, son un monton de rutas para poder dividir el codigo

views = Blueprint('views', __name__)



@views.route('/')
def index():
    admin = Admin.query.all()

    # 1, 0, None
    print("llego aqui")

    # si no hay nada en la db entonces a esa ruta
    if not admin:
        return redirect(url_for('install.finstall'))

    return render_template('index.html')





