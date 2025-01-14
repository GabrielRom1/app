from flask import Blueprint,  render_template, request, jsonify, url_for, flash
from . import db
from .models import Admin


#se va a definir los blueprints, son un monton de rutas para poder dividir el codigo
auth = Blueprint('auth', __name__)



@auth.route('/login',  methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        print("EN EL GET DE LOGIN")

    if request.method == 'POST':
        print("EN EL POST DE LOGIN")


        data = request.get_json()
    
        # Procesa los datos
        email = data.get('email', 'No email provided')
        password = data.get('password', 'No password provided')
        
        user = Admin.query.filter_by(email = email).first()
        if user:
            print(user.name)
            if password == user.password:
                print("password correct")
                return jsonify({'success': True, 'message': 'Niice',  'redirect_url': url_for('views.home')}), 201
            else:
                print("Password incorrect")
                flash("Incorrect password", 'danger')

                return jsonify({'success': False, 'message': 'Password incorrect',  'redirect_url': url_for('auth.login')}), 201


        else:
            flash("No user", 'danger')
            return jsonify({'success': False, 'message': 'No User',  'redirect_url': url_for('auth.login')}), 201

    return render_template('login.html')


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up', methods = ['POST'])
def sign_up():
    # AQUI LEES EL FORM DEL USUARIO Y PONES EL USER EN LA TABLA DE USERS
    return render_template('signup.html')




