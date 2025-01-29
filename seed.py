from app import app, db
from models import Community, User, Event, Estate, Notification, RSVP
from datetime import datetime

def seed_database():
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Add sample communities
        community1 = Community(name='Sunrise Valley', location='East District')
        community2 = Community(name='Maple Heights', location='West District')
        db.session.add_all([community1, community2])
        db.session.commit()
        
        # Add sample users
        user1 = User(
            name='John Doe',
            email='john@example.com',
            occupation='Engineer',
            phoneno=1234567890,
            houseno=101,
            community_id=community1.id
        )
        user2 = User(
            name='Jane Smith',
            email='jane@example.com',
            occupation='Designer',
            phoneno=9876543210,
            houseno=202,
            community_id=community2.id
        )
        db.session.add_all([user1, user2])
        db.session.commit()
        
        # Add sample events
        event1 = Event(
            eventname='Summer Festival',
            eventdate=datetime(2025, 6, 15),
            community_id=community1.id
        )
        event2 = Event(
            eventname='Community Meeting',
            eventdate=datetime(2025, 2, 1),
            community_id=community2.id
        )
        db.session.add_all([event1, event2])
        db.session.commit()
        
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()