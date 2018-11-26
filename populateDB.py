from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
import models
import random
from datetime import datetime, timedelta
import time

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/apms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

fake = Faker()

def change():
    global a
    a = 0

def populateCustomerRides():
    a = 1
    customerList = models.Customer.query.all()
    rideList = models.Ride.query.all()
    tim = datetime(2018,12,27,10,0)
    while True:
        if a is 0:
            break
        customer = random.choice(customerList)
        ride = random.choice(rideList)
        newTime = tim + timedelta(0,300) # days, seconds, then other fields.
        if newTime.hour == 18:
            tim = datetime(newTime.year,newTime.month,newTime.day+1,10,00)
            if newTime.day == 28:
                if newTime.month < 12:
                    tim = datetime(newTime.year,newTime.month+1,1,10,00)
                if newTime.month == 12:
                    tim = datetime(newTime.year+1,1,1,10,00)
        else:
            tim = newTime
        customerride = models.CustomerRidesLink(customerId=customer.id,rideId=ride.id,time=newTime)
        db.session.add(customerride)
        db.session.commit()

def populateRide():
    ride_list = ['Carousel','Darkride','Droptower','Ferriswheel','Gyrotower','Rollercoaster','Waterride','SpiralSlide','Circus','Gravitron']
    for ride in ride_list:
        name = ride
        price = (random.randint(20,30)) * 10
        maintenance_cost = (random.randint(20,30)) * 100
        rideDetails = models.Ride(name=name,price=price,maintenance_cost=maintenance_cost)
        db.session.add(rideDetails)
        db.session.commit()

def populateCustomer():
    count = 100
    type_list = ['normal','student']
    age10 = list(range(5,10))
    age20 = list(range(11,19))
    age30 = list(range(20,30))
    age50 = list(range(31,50))
    age70 = list(range(51,70))
    age100 = list(range(71,100))
    wr = age10*70+age20*20+age30*5+age50*3+age70*1+age100*1
    while count > 0:
        name = fake.name()
        age = random.choice(wr)
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
