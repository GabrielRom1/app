from flask import Blueprint,  render_template

#se va a definir los blueprints, son un monton de rutas para poder dividir el codigo
auth = Blueprint('auth', __name__)



@auth.route('/login',  methods=['GET'])
def login():
    print("en login")

    # como hacer un query?
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up', methods = ['POST'])
def sign_up():
    # AQUI LEES EL FORM DEL USUARIO Y PONES EL USER EN LA TABLA DE USERS
    return render_template('signup.html')




