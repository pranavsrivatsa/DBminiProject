from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from datetime import datetime

"""
>python3 models.py db --help
>python3 models.py db init
>python3 models.py db migrate
>python3 models.py db upgrade
"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/apms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app,db)

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

# CustomerRides_Table = db.Table('customerrides',
#     db.Column('customerId',db.Integer, db.ForeignKey('customer.id'),primary_key=False),
#     db.Column('rideId',db.Integer, db.ForeignKey('ride.id'), primary_key=False)
#     )

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

    def __repr__(self):
        return self.price

class CustomerRidesLink(db.Model):
    __tablename__ = 'customerrides'
    id = db.Column(db.Integer, primary_key=True)
    customerId = db.Column(db.Integer, db.ForeignKey('customer.id'))
    rideId = db.Column(db.Integer, db.ForeignKey('ride.id'))
    customer = db.relationship('Customer',uselist=False)
    ride = db.relationship('Ride',uselist=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


if __name__=='__main__':
    manager.run()
