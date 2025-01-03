from website import create_app
from flask import Blueprint, Flask, render_template, url_for, redirect


app = create_app()

main = Blueprint('main', __name__)

#only run the app if main is execute
if __name__ == '__main__':
    app.run(debug = True)



















# def create_app():
#     app = Flask(__name__)
    
#     app.config['SECRET_KEY'] = 'THIS IS A SECRET KEY. DO NOT SHARE. PLEASE CHANGE.'

#     return app




# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)

# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     completed = db.Column(db.Integer, default=0)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<Task %r>' % self.id

# @app.route('/')
# def index():

#     # verify if exists a database

#     # if not exists redirect to first install and create the database with the first global admin
#         #redirect(url_for('install.finstall'))
#     return render_template('index.html')


# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)
