from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Events(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    eventname = db.Column(db.String(100), nullable=False)
    eventDate = db.Column(db.DateTime, nullable=False)
    
    
    community_id = db.Column(db.Integer, db.ForeignKey('community.id'), nullable=False)
    community = db.relationship('Community', backref=db.backref('events', lazy=True))

    def __repr__(self):
        return f'<Event {self.id}: {self.eventname}>'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    phoneno = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(300), unique=True, nullable=False)
    occupation = db.Column(db.String(400), nullable=True)
    houseno = db.Column(db.Integer, nullable=True)

   
    community_id = db.Column(db.Integer, db.ForeignKey('community.id'), nullable=True)
    community = db.relationship('Community', backref=db.backref('users', lazy=True))
    
    def __repr__(self):
        return f'<User {self.id}: {self.name}>'

class Community(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(400), nullable=False)
    location = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f'<Community {self.id}: {self.name}>'

class Notifications(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('notifications', lazy=True))

    def __repr__(self):
        return f'<Notification {self.id}: {self.name}>'

class Estates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    estateName = db.Column(db.String(100), nullable=False)
    
    
    community_id = db.Column(db.Integer, db.ForeignKey('community.id'), nullable=False)
    community = db.relationship('Community', backref=db.backref('estates', lazy=True))

    def __repr__(self):
        return f'<Estate {self.id}: {self.estateName}>'
   

