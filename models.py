from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from datetime import datetime
import populateDB


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://wjnrdgerdnlecm:a55ffe88fa53928bff22271ac7b51b8381244f317f9d12a01b08ac330bbf9038@ec2-54-235-180-123.compute-1.amazonaws.com:5432/db140ed2g8ukhd'
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
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    day_rev = db.Column(db.Integer)
    day_count = db.Column(db.Integer)


class dayrev(db.Model):
    __tablename__ = 'dayrev'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    Carousel = db.Column(db.Integer)
    Darkride = db.Column(db.Integer)
    Droptower = db.Column(db.Integer)
    Ferriswheel = db.Column(db.Integer)
    Gyrotower = db.Column(db.Integer)
    Rollercoaster = db.Column(db.Integer)
    Waterride = db.Column(db.Integer)
    SpiralSlide = db.Column(db.Integer)
    Circus = db.Column(db.Integer)
    Gravitron = db.Column(db.Integer)


class daycount(db.Model):
    __tablename__ = 'daycount'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    Carousel = db.Column(db.Integer)
    Darkride = db.Column(db.Integer)
    Droptower = db.Column(db.Integer)
    Ferriswheel = db.Column(db.Integer)
    Gyrotower = db.Column(db.Integer)
    Rollercoaster = db.Column(db.Integer)
    Waterride = db.Column(db.Integer)
    SpiralSlide = db.Column(db.Integer)
    Circus = db.Column(db.Integer)
    Gravitron = db.Column(db.Integer)


class month(db.Model):
    __tablename__ = 'monthdetails'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    month_rev = db.Column(db.Integer)
    month_count = db.Column(db.Integer)


class monthrev(db.Model):
    __tablename__ = 'monthrev'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    Carousel = db.Column(db.Integer)
    Darkride = db.Column(db.Integer)
    Droptower = db.Column(db.Integer)
    Ferriswheel = db.Column(db.Integer)
    Gyrotower = db.Column(db.Integer)
    Rollercoaster = db.Column(db.Integer)
    Waterride = db.Column(db.Integer)
    SpiralSlide = db.Column(db.Integer)
    Circus = db.Column(db.Integer)
    Gravitron = db.Column(db.Integer)


class monthcount(db.Model):
    __tablename__ = 'monthcount'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    Carousel = db.Column(db.Integer)
    Darkride = db.Column(db.Integer)
    Droptower = db.Column(db.Integer)
    Ferriswheel = db.Column(db.Integer)
    Gyrotower = db.Column(db.Integer)
    Rollercoaster = db.Column(db.Integer)
    Waterride = db.Column(db.Integer)
    SpiralSlide = db.Column(db.Integer)
    Circus = db.Column(db.Integer)
    Gravitron = db.Column(db.Integer)


@manager.command
def seed():
    populateDB.populateRide()


if __name__ == '__main__':
    manager.run()
