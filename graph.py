from flask_sqlalchemy import SQLAlchemy
from models import *
from collections import Counter

def getAgeRanges():
    customers = Customer.query.all()
    ageRange = [0,0,0,0,0,0]
    for customer in customers:
        age = customer.age
        if age <= 10:
            ageRange[0] += 1
        elif 10 < age <= 18:
            ageRange[1] += 1
        elif 19 < age <= 30:
            ageRange[2] += 1
        elif 30 < age <= 50:
            ageRange[3] += 1
        elif 50 < age <= 70:
            ageRange[4] += 1
        else:
            ageRange[5] += 1
    return ageRange
