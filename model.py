from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Community(db.Model):
    __tablename__ = 'community'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200))
    
    # Relationships
    users = db.relationship('User', backref='community', lazy=True)
    events = db.relationship('Event', backref='community', lazy=True)
    estates = db.relationship('Estate', backref='community', lazy=True)
    notifications = db.relationship('Notification', backref='community', lazy=True)

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    occupation = db.Column(db.String(100))
    phoneno = db.Column(db.Integer)
    houseno = db.Column(db.Integer)
    community_id = db.Column(db.Integer, db.ForeignKey('community.id'), nullable=False)
    
   
    estates = db.relationship('Estate', backref='user', lazy=True)
    notifications = db.relationship('Notification', backref='user', lazy=True)

class Event(db.Model):
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    eventname = db.Column(db.String(200), nullable=False)
    eventdate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    community_id = db.Column(db.Integer, db.ForeignKey('community.id'), nullable=False)

class Estate(db.Model):
    __tablename__ = 'estate'
    
    id = db.Column(db.Integer, primary_key=True)
    estatename = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    community_id = db.Column(db.Integer, db.ForeignKey('community.id'), nullable=False)

class Notification(db.Model):
    __tablename__ = 'notifications'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    rsvp = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    community_id = db.Column(db.Integer, db.ForeignKey('community.id'), nullable=False)

class RSVP(db.Model):
    __tablename__ = 'rsvp'
    
    id = db.Column(db.String(50), primary_key=True)
   

