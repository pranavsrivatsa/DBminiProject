#import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from datetime import datetime
from alembic import op
import populateDB


# >rm -R migrations
# >python3 models.py db init
# >python3 models.py db migrate
# >python3 models.py db upgrade
# >python3 models.py seed


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/apms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return self.password

class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(128), nullable=False)
    rides = db.relationship('CustomerRidesLink')

class Ride(db.Model):
    __tablename__ = 'ride'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    maintenance_cost = db.Column(db.Integer, nullable=False)

class CustomerRidesLink(db.Model):
    __tablename__ = 'customerrides'
    id = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.Integer, db.ForeignKey('customer.id'))
    rideId = db.Column(db.Integer, db.ForeignKey('ride.id'))
    customer = db.relationship('Customer')
    ride = db.relationship('Ride')
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class day(db.Model):
    __tablename__ = 'daydetails'
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Date)
    revenue = db.Column(db.Integer)
    count = db.Column(db.Integer)

class dayrev(db.Model):
    __tablename__ = 'dayrev'
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Date, nullable = False)
    rideId = db.Column(db.Integer, db.ForeignKey('ride.id'))
    ride = db.relationship('Ride')
    revenue = db.Column(db.Integer)
    count = db.Column(db.Integer)

class month(db.Model):
    __tablename__ = 'monthdetails'
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.Date)
    revenue = db.Column(db.Integer)
    count = db.Column(db.Integer)

class monthrev(db.Model):
    __tablename__ = 'monthrev'
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.Date)
    rideId = db.Column(db.Integer, db.ForeignKey('ride.id'))
    ride = db.relationship('Ride')
    revenue = db.Column(db.Integer)
    count = db.Column(db.Integer)

@manager.command
def seed():
    populateDB.populateRide()
    for i in range(1,11):
        db.session.add(dayrev(id=i,day=datetime(2018,1,1),rideId=i,revenue=0,count=0))
        db.session.add(monthrev(id=i,month=datetime(2018,1,1),rideId=i,revenue=0,count=0))
        db.session.commit()

if __name__=='__main__':
    manager.run()
