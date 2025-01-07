#archivo para crear al primer admin 
from flask import Blueprint, render_template, redirect, url_for, request, flash, session, Flask, Request
from .models import Admin
from flask import jsonify
from . import db




install = Blueprint('install', __name__)

@install.route('/finstall', methods = ['GET'])
def finstall():
    admin = Admin.query.all()
    if admin:
        return redirect(url_for('views.index'))
    
    return render_template('install.html')



@install.route('/JSON', methods = ['POST'])
def JSON():
    # Recibe los datos enviados en el cuerpo de la solicitud
    data = request.get_json()
    
    # Procesa los datos
    name2 = data.get('name2', 'No name provided')
    email2 = data.get('email2', 'No email provided')
    password2 = data.get('password2', 'No password provided')
    print(f"Nombre recibido: {name2}")
    print(f"Email recibido: {name2}")
    print(f"Password recibido: {name2}")


    # Responde al cliente
    return jsonify({'message': f'Hola, {name2}!', 'success': True, 'redirect_url': url_for('auth.login')}), 200


@install.route('/flask', methods=['POST'])
def finstall_post():
    print("LLEGO AL POST BIEN")

    # Obtener los datos enviados por el formulario
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')



    first_admin = Admin(name=name, email = email,password=password, id= 1) # Crear un nuevo usuario
    # Agregar el usuario a la base de datos
    try:
        db.session.add(first_admin)
        db.session.commit()  # Guardar cambios
        print("paso el 3")
        return redirect(url_for('views.index'))
        # return jsonify({'success': True, 'message': 'Usuario registrado con éxito'}), 201
    except Exception as e:
        db.session.rollback()  # Revertir cambios si hay un error
        # return jsonify({'success': False, 'message': str(e)}), 500