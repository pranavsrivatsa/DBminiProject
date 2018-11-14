import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy.ext.declarative import DeclarativeMeta


'''
>python3 models.py db --help
>python3 models.py db init
>python3 models.py db migrate
>python3 models.py db upgrade
'''

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/apms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


# class AlchemyEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj.__class__, DeclarativeMeta):
#             fields = {}
#             for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
#                 data = obj.__getattribute__(field)
#                 try:
#                     # this will fail on non-encodable values, like other classes
#                     json.dumps(data)
#                     fields[field] = data
#                 except TypeError:
#                     fields[field] = None
#             return fields
#         return json.JSONEncoder.default(self, obj)


class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return self.password


CustomerRides_Table = db.Table('customerrides',
                               db.Column('customerId', db.Integer, db.ForeignKey(
                                   'customer.id'), primary_key=False),
                               db.Column('rideId', db.Integer, db.ForeignKey(
                                   'ride.id'), primary_key=False)
                               )


class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    age = db.Column(db.String(128), nullable=False)
    type = db.Column(db.String(128), nullable=False)
    rides = db.relationship('Ride', secondary=CustomerRides_Table, lazy='subquery',
                            backref=db.backref('customers', lazy=True))


class Ride(db.Model):
    __tablename__ = 'ride'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return self.price


if __name__ =='__main__':
    manager.run()
