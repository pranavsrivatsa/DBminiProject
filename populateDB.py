from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
import models
import random
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/apms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

fake = Faker()

def populateCustomerRides():
    customerList = models.Customer.query.all()
    rideList = models.Ride.query.all()
    while True:
        customer = random.choice(customerList)
        ride = random.choice(rideList)
        db.session.execute(models.CustomerRides_Table.insert().values([(customer.id,ride.id)]))
        db.session.commit()

def populateCustomer():
    count = 100
    type_list = ['normal','student']
    while count > 0:
        name = fake.name()
        age = random.randint(3,100)
        type = 'normal'
        if age <= 10:
            type = 'child'
        elif age >= 60:
            type = 'senior'
        else:
            type = random.choice(type_list)
        customer = models.Customer(name=name,age=age,type=type)
        db.session.add(customer)
        db.session.commit()
        count -= 1

def populateRide():
    ride_list = ['Carousel','Dark ride','Drop tower','Ferris wheel','Gravity ride','Gyro tower','Pendulum ride','Roller coaster','Simulator ride','Swing ride','Water ride','Spiral Slide ride','Circus','Enterprise','Gravitron']
    for ride in ride_list:
        name = ride
        price = random.randint(100,250)
        rideDetails = models.Ride(name=name,price=price)
        db.session.add(rideDetails)
        db.session.commit()
