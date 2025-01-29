from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_migrate import Migrate
from datetime import datetime
from models import Events, User, Community, Notifications, Estates 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///model.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)



class Home(Resource):
    def get(self):
        return {"message": "Welcome to the Community Management System"}

class EventsResource(Resource):
    def get(self):
        events = Events.query.all()
        return [{'id': event.id, 'name': event.eventname, 'date': event.eventDate} for event in events]

    def post(self):
        data = request.get_json()
        new_event = Events(eventname=data['eventname'], eventDate=datetime.strptime(data['eventDate'], '%Y-%m-%d'), community_id=data['community_id'])
        db.session.add(new_event)
        db.session.commit()
        return {"message": "Event added successfully"}, 201

class UsersResource(Resource):
    def get(self):
        users = User.query.all()
        return [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]

class CommunitiesResource(Resource):
    def get(self):
        communities = Community.query.all()
        return [{'id': community.id, 'name': community.name, 'location': community.location} for community in communities]
    
class NotificationsResource(Resource):
    def get(self):
        notifications = Notifications.query.all()
        return [{'id': notification.id, 'name': notification.name, 'user_id': notification.user_id} for notification in notifications]

class EstatesResource(Resource):
    def get(self):
        estates = Estates.query.all()
        return [{'id': estate.id, 'estateName': estate.estateName, 'community_id': estate.community_id} for estate in estates]

api.add_resource(Home, '/')
api.add_resource(EventsResource, '/events')
api.add_resource(UsersResource, '/users')
api.add_resource(CommunitiesResource, '/communities')
api.add_resource(EstatesResource, '/estates')
api.add_resource(NotificationsResource, 'notifications')

if __name__ == '__main__':
    app.run(debug=True)