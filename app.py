from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Community, User, Event, Estate, Notification, RSVP

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///community.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/communities', methods=['GET'])
def get_communities():
    communities = Community.query.all()
    return jsonify([{
        'id': c.id,
        'name': c.name,
        'location': c.location
    } for c in communities])

@app.route('/communities', methods=['POST'])
def create_community():
    data = request.json
    new_community = Community(
        name=data['name'],
        location=data['location']
    )
    db.session.add(new_community)
    db.session.commit()
    return jsonify({
        'id': new_community.id,
        'name': new_community.name,
        'location': new_community.location
    }), 201


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{
        'id': u.id,
        'name': u.name,
        'email': u.email,
        'occupation': u.occupation,
        'phoneno': u.phoneno,
        'houseno': u.houseno,
        'community_id': u.community_id
    } for u in users])

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(
        name=data['name'],
        email=data['email'],
        occupation=data['occupation'],
        phoneno=data['phoneno'],
        houseno=data['houseno'],
        community_id=data['community_id']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({
        'id': new_user.id,
        'name': new_user.name,
        'email': new_user.email
    }), 201

@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    return jsonify([{
        'id': e.id,
        'eventname': e.eventname,
        'eventdate': e.eventdate.isoformat(),
        'community_id': e.community_id
    } for e in events])

@app.route('/events', methods=['POST'])
def create_event():
    data = request.json
    new_event = Event(
        eventname=data['eventname'],
        eventdate=datetime.fromisoformat(data['eventdate']),
        community_id=data['community_id']
    )
    db.session.add(new_event)
    db.session.commit()
    return jsonify({
        'id': new_event.id,
        'eventname': new_event.eventname,
        'eventdate': new_event.eventdate.isoformat()
    }), 201

if __name__ == '__main__':
    app.run(debug=True)