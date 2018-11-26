from flask_sqlalchemy import SQLAlchemy
from models import *
from datetime import datetime
import time
import json

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

def date_to_millis(d):
    """Converts a datetime object to the number of milliseconds since the unix epoch."""
    return int(time.mktime(d.timetuple())) * 1000

def getDayStats():
    daystats = day.query.all()
    dates = []
    revenue = []
    count = []
    for d in daystats:
        dates.append(date_to_millis(d.time))
        revenue.append(d.day_rev)
        count.append(d.day_count)
    return dates,revenue,count
