from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
import models
import random
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/apms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

fake = Faker()

def populateCustomerRides():
    customerList = models.Customer.query.all()
    rideList = models.Ride.query.all()
    time = datetime.datetime.now()
    while True:
        customer = random.choice(customerList)
        ride = random.choice(rideList)
        newTime = time + datetime.timedelta(0,3) # days, seconds, then other fields.
        time = newTime
        #db.session.execute(models.CustomerRides_Table.insert().values([(customer.id,ride.id,time)]))
        customerride = models.CustomerRidesLink(customerId=customer.id,rideId=ride.id,time=time)
        db.session.add(customerride)
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

def populateRide():
    ride_list = ['Carousel','Dark ride','Drop tower','Ferris wheel','Gravity ride','Gyro tower','Pendulum ride','Roller coaster','Simulator ride','Swing ride','Water ride','Spiral Slide ride','Circus','Enterprise','Gravitron']
    for ride in ride_list:
        name = ride
        price = random.randint(100,250)
        rideDetails = models.Ride(name=name,price=price)
        db.session.add(rideDetails)
        db.session.commit()
