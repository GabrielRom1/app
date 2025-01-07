from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'THIS IS A SECRET KEY. DO NOT SHARE. PLEASE CHANGE.'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    # link db with the app
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .install import install

# to put a prefix (in this case non prefix) to every route
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(install, url_prefix='/')




    # incluir las demas tablas ademas de Admin
    from .models import Admin, Users

    create_database(app)


    return app


def create_database(app):
    # check if the db is already create.
    if not path.exists('website/' + DB_NAME):
        with app.app_context():  # Entra al contexto de la aplicación
            db.create_all()
            print("Created Database!!")



