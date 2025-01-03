

#archivo para crear al primer admin 

from flask import Blueprint, render_template, redirect, url_for, request, flash, session, Flask
from .models import Admin


install = Blueprint('install', __name__)

@install.route('/install')
def finstall():
    admin = Admin.query.all()
    if admin:
        return redirect(url_for('main.index'))
    
    return render_template('install.html')

# @install.route('/install', methods=['POST'])
# def finstall_post():

#     admin = Admin.query.all()  # if this returns a user, then the email already exists in database
#     if admin:
#         return redirect(url_for('main.index'))

#     # code to validate and add user to database goes here
#     email = request.form.get('email')
#     name = request.form.get('name')
#     password = request.form.get('password')

#     # create a new user with the form data. Hash the password so the plaintext version isn't saved.
#     new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'), active=True)

#     # add the new user to the database
#     db.session.add(new_user)
#     db.session.commit()

#     # add the new user as the main administrator
#     new_admin = Admin(email=email)
#     db.session.add(new_admin)
#     db.session.commit()

#     return redirect(url_for('auth.login'))   

