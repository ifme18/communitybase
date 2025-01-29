from  flask import Flask ,jsonify, session
from flask_sqlalchemy import SQLAlchemy
from model import db ,Estates, Events,Community,User,Notifications
from flask_migrate import Migrate
from flask_cors/ 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)


