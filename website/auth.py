from flask import Blueprint,  render_template

#se va a definir los blueprints, son un monton de rutas para poder dividir el codigo
auth = Blueprint('auth', __name__)



@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up')
def sign_up():
    return render_template('signup.html')
