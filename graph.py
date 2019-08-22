from models import *
import time


def getAgeRanges():
    customers = Customer.query.all()
    ageRange = [0, 0, 0, 0, 0, 0]
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
    return dates, revenue, count


def getDayRideRevenue():
    dayRideRevenue = dayrev.query.all()
    dates = []
    Carousel = []
    Darkride = []
    Droptower = []
    Ferriswheel = []
    Gyrotower = []
    Rollercoaster = []
    Waterride = []
    SpiralSlide = []
    Circus = []
    Gravitron = []
    for d in dayRideRevenue:
        dates.append(date_to_millis(d.time))
        Carousel.append(d.Carousel)
        Darkride.append(d.Darkride)
        Droptower.append(d.Droptower)
        Ferriswheel.append(d.Ferriswheel)
        Gyrotower.append(d.Gyrotower)
        Rollercoaster.append(d.Rollercoaster)
        Waterride.append(d.Waterride)
        SpiralSlide.append(d.SpiralSlide)
        Circus.append(d.Circus)
        Gravitron.append(d.Gravitron)
    return dates, Carousel, Darkride, Droptower, Ferriswheel, Gyrotower, Rollercoaster, Waterride, SpiralSlide, Circus, Gravitron


def getDayRideCount():
    dayRideRevenue = daycount.query.all()
    Carousel = []
    Darkride = []
    Droptower = []
    Ferriswheel = []
    Gyrotower = []
    Rollercoaster = []
    Waterride = []
    SpiralSlide = []
    Circus = []
    Gravitron = []
    for d in dayRideRevenue:
        Carousel.append(d.Carousel)
        Darkride.append(d.Darkride)
        Droptower.append(d.Droptower)
        Ferriswheel.append(d.Ferriswheel)
        Gyrotower.append(d.Gyrotower)
        Rollercoaster.append(d.Rollercoaster)
        Waterride.append(d.Waterride)
        SpiralSlide.append(d.SpiralSlide)
        Circus.append(d.Circus)
        Gravitron.append(d.Gravitron)
    return Carousel, Darkride, Droptower, Ferriswheel, Gyrotower, Rollercoaster, Waterride, SpiralSlide, Circus, Gravitron


def getMonthStats():
    monthstats = month.query.all()
    dates = []
    revenue = []
    count = []
    for d in monthstats:
        dates.append(date_to_millis(d.time))
        revenue.append(d.month_rev)
        count.append(d.month_count)
    return dates, revenue, count


def getMonthRideRevenue():
    monthRideRevenue = monthrev.query.all()
    dates = []
    Carousel = []
    Darkride = []
    Droptower = []
    Ferriswheel = []
    Gyrotower = []
    Rollercoaster = []
    Waterride = []
    SpiralSlide = []
    Circus = []
    Gravitron = []
    for d in monthRideRevenue:
        dates.append(date_to_millis(d.time))
        Carousel.append(d.Carousel)
        Darkride.append(d.Darkride)
        Droptower.append(d.Droptower)
        Ferriswheel.append(d.Ferriswheel)
        Gyrotower.append(d.Gyrotower)
        Rollercoaster.append(d.Rollercoaster)
        Waterride.append(d.Waterride)
        SpiralSlide.append(d.SpiralSlide)
        Circus.append(d.Circus)
        Gravitron.append(d.Gravitron)
    return dates, Carousel, Darkride, Droptower, Ferriswheel, Gyrotower, Rollercoaster, Waterride, SpiralSlide, Circus, Gravitron


def getMonthRideCount():
    monthRideRevenue = monthcount.query.all()
    Carousel = []
    Darkride = []
    Droptower = []
    Ferriswheel = []
    Gyrotower = []
    Rollercoaster = []
    Waterride = []
    SpiralSlide = []
    Circus = []
    Gravitron = []
    for d in monthRideRevenue:
        Carousel.append(d.Carousel)
        Darkride.append(d.Darkride)
        Droptower.append(d.Droptower)
        Ferriswheel.append(d.Ferriswheel)
        Gyrotower.append(d.Gyrotower)
        Rollercoaster.append(d.Rollercoaster)
        Waterride.append(d.Waterride)
        SpiralSlide.append(d.SpiralSlide)
        Circus.append(d.Circus)
        Gravitron.append(d.Gravitron)
    return Carousel, Darkride, Droptower, Ferriswheel, Gyrotower, Rollercoaster, Waterride, SpiralSlide, Circus, Gravitron
