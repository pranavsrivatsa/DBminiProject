from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

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

CustomerRides_Table = db.Table('customerrides',
    db.Column('customerId',db.Integer, db.ForeignKey('customer.id')),
    db.Column('rideId',db.Integer, db.ForeignKey('ride.id'))
    )

class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    age = db.Column(db.String(128), nullable=False)
    type = db.Column(db.String(128), nullable=False)
    rides = db.relationship('Ride', secondary=CustomerRides_Table, lazy='subquery',
        backref=db.backref('customers', lazy=True))

    def __repr__(self):
        return self.type

class Ride(db.Model):
    __tablename__ = 'ride'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return self.price

if __name__=='__main__':
    manager.run()
