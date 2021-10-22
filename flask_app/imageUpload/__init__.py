from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Teo/Desktop/workspace/flaskFace/flaskFace.db'
db = SQLAlchemy(app)

from os import urandom
app.config['SECRET_KEY'] = urandom(32)

from imageUpload.home.views import home
from imageUpload.auth.views import auth
from imageUpload.landing.views import landing
app.register_blueprint(home)
app.register_blueprint(auth)
app.register_blueprint(landing)

db.create_all()