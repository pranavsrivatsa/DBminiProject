from flask import Flask, url_for, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from models import *
import populateDB
import graph

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://wjnrdgerdnlecm:a55ffe88fa53928bff22271ac7b51b8381244f317f9d12a01b08ac330bbf9038@ec2-54-235-180-123.compute-1.amazonaws.com:5432/db140ed2g8ukhd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

monthcount.query.delete()
monthrev.query.delete()
month.query.delete()
daycount.query.delete()
dayrev.query.delete()
day.query.delete()
CustomerRidesLink.query.delete()
Ride.query.delete()
Customer.query.delete()



@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        inputEmail = request.form["InputEmail"]
        actualPassword = Account.query.filter_by(email=inputEmail).first()
        if request.form['InputPassword'] != str(actualPassword):
            error = "Invalid Credentials."
            return render_template('auth/login.html', error=error)
        else:
            return redirect('/Overview')
    else:
        return render_template("auth/login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        inputCredentials = request.form.to_dict()
        user = Account(fullname=inputCredentials["InputName"], email=inputCredentials["InputEmail"], password=inputCredentials["InputPassword"])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("overview"))
    else:
        return render_template("auth/register.html")


@app.route("/dashboard", methods=['GET', 'POST'])
def index():
    daystats = day.query.all()
    dayRideRev = dayrev.query.all()
    dayRideCnt = daycount.query.all()
    if request.method == "POST":
        if request.form['pop'] == 'popcust':
            populateDB.populateCustomer()
        if request.form['pop'] == 'startpark':
            populateDB.populateCustomerRides()
        if request.form['pop'] == 'stoppark':
            populateDB.change()
    datems, dayrevenue, daycunt = graph.getDayStats()
    days = len(datems)
    ridedates, cr, drr, dtr, fwr, gtr, rcr, wrr, ssr, cir, gr = graph.getDayRideRevenue()
    hours = len(ridedates)
    cc, drc, dtc, fwc, gtc, rcc, wrc, ssc, cic, gc = graph.getDayRideCount()
    return render_template("dashboard.html",dayStats=daystats,dayriderev=dayRideRev,dayridecnt=dayRideCnt,Days=days,Hours=hours,dates=datems,dayRevenue=dayrevenue,dayCount=daycunt,rideDates=ridedates,CR=cr,DRR=drr,DTR=dtr,FWR=fwr,GTR=gtr,RCR=rcr,WRR=wrr,SSR=ssr,CIR=cir,GR=gr,CC=cc, DRC=drc, DTC=dtc, FWC=fwc, GTC=gtc, RCC=rcc, WRC=wrc, SSC=ssc, CIC=cic, GC=gc)


@app.route("/monthStats", methods=['GET', 'POST'])
def indexMonth():
    monthstats = month.query.all()
    monthRideRev = monthrev.query.all()
    monthRideCnt = monthcount.query.all()
    if request.method == "POST":
        if request.form['pop'] == 'popcust':
            populateDB.populateCustomer()
        if request.form['pop'] == 'startpark':
            populateDB.populateCustomerRides()
        if request.form['pop'] == 'stoppark':
            populateDB.change()
    datems, dayrevenue, daycunt = graph.getMonthStats()
    days = len(datems)
    ridedates, cr, drr, dtr, fwr, gtr, rcr, wrr, ssr, cir, gr = graph.getMonthRideRevenue()
    hours = len(ridedates)
    cc, drc, dtc, fwc, gtc, rcc, wrc, ssc, cic, gc = graph.getMonthRideCount()
    return render_template("monthStats.html",monthStats=monthstats,monthriderev=monthRideRev,monthridecnt=monthRideCnt,Days=days,Hours=hours,dates=datems,dayRevenue=dayrevenue,dayCount=daycunt,rideDates=ridedates,CR=cr,DRR=drr,DTR=dtr,FWR=fwr,GTR=gtr,RCR=rcr,WRR=wrr,SSR=ssr,CIR=cir,GR=gr,CC=cc,DRC=drc,DTC=dtc,FWC=fwc,GTC=gtc,RCC=rcc,WRC=wrc,SSC=ssc,CIC=cic,GC=gc)


@app.route("/Overview", methods=['GET'])
def overview():
    customers = Customer.query.all()
    rides = Ride.query.all()
    customerrides = CustomerRidesLink.query.all()
    ageList = graph.getAgeRanges()
    datems, dayrevenue, daycunt = graph.getDayStats()
    days = len(datems)
    ridedates, cr, drr, dtr, fwr, gtr, rcr, wrr, ssr, cir, gr = graph.getDayRideRevenue()
    hours = len(ridedates)
    cc, drc, dtc, fwc, gtc, rcc, wrc, ssc, cic, gc = graph.getDayRideCount()
    return render_template("overview.html",Customers=customers,Rides=rides,CustomerRides=customerrides,ageRanges=ageList,Days=days,Hours=hours,dates=datems,dayRevenue=dayrevenue,dayCount=daycunt,rideDates=ridedates,CR=cr,DRR=drr,DTR=dtr,FWR=fwr,GTR=gtr,RCR=rcr,WRR=wrr,SSR=ssr,CIR=cir,GR=gr,CC=cc,DRC=drc,DTC=dtc,FWC=fwc,GTC=gtc,RCC=rcc,WRC=wrc,SSC=ssc,CIC=cic,GC=gc)


@app.route("/backend", methods=['POST', 'GET'])
def backend():
    if request.method == "POST":
        customer = request.form["customer"]
        ride = request.form["ride"]
        time_in = datetime.strptime(request.form['time_in'], '%d-%m-%Y %H:%M')
        new_customerride = CustomerRidesLink(customerId=customer, rideId=ride, time=time_in)
        db.session.add(new_customerride)
        db.session.commit()
        # data = {"id": new_customerride.id,
        #         "customer": customer,
        #         "ride": ride,
        #         "time_in": request.form['time_in']}
        return redirect("/dashboard", code=302)
    else:
        crs = db.session.query(CustomerRidesLink, Customer,Ride).filter_by(customerId=Customer.id, rideId=Ride.id).all()
        return render_template('dashboard.html', customers=crs)


@app.route("/edit/<int:id>", methods=['POST', 'GET'])
def update_record(id):
    if request.method == "POST":
        customer = request.form["customer"]
        ride = request.form["ride"]
        time_in = datetime.strptime(request.form['time_in'], '%d-%m-%Y %H:%M')
        update_customer = db.session.query(CustomerRidesLink,Customer,Ride).filter_by(id=id, customerId=Customer.id, rideId=Ride.id).first()
        update_customer.CustomerRidesLink.customerId = customer
        update_customer.CustomerRidesLink.rideId = ride
        update_customer.CustomerRidesLink.time = time_in
        db.session.commit()
        # data = {"customer": customer,
        #         "ride": ride,
        #         "time_in": request.form['time_in']}
        return redirect("/dashboard", code=302)
    else:
        new_customer = db.session.query(CustomerRidesLink, Customer, Ride).filter_by(id=id, customerId=Customer.id, rideId=Ride.id).first()
        new_customer.CustomerRidesLink.time = new_customer.CustomerRidesLink.time.strftime("%d-%m-%Y %H:%M")
        return render_template('update.html', data=new_customer)


@app.route("/delete/<int:id>", methods=['POST', 'GET'])
def delete_record(id):
    customer = db.session.query(CustomerRidesLink).filter_by(id=id).first()
    db.session.delete(customer)
    db.session.commit()
    return redirect("/dashboard")


@app.route("/Rides", methods=['GET'])
def rides():
    rides = Ride.query.all()
    return render_template("Rides.html", Rides=rides)


@app.route("/Carousel", methods=['GET'])
def carousel():
    return render_template('Carousel.html')


@app.route("/Darkride", methods=['GET'])
def darkride():
    return render_template('Darkride.html')


@app.route("/Droptower", methods=['GET'])
def droptower():
    return render_template('Droptower.html')


@app.route("/Gyrotower", methods=['GET'])
def gyrotower():
    return render_template('Gyrotower.html')


@app.route("/Waterride", methods=['GET'])
def waterride():
    return render_template('Waterride.html')


@app.route("/Rollercoaster", methods=['GET'])
def rollercoaster():
    return render_template('Rollercoaster.html')


@app.route("/SpiralSlide", methods=['GET'])
def spiralslide():
    return render_template('Spiralslide.html')


@app.route("/Circus", methods=['GET'])
def circus():
    return render_template('Circus.html')


@app.route("/Gravitron", methods=['GET'])
def gravitron():
    return render_template('Gravitron.html')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


if __name__ == '__main__':
	app.run(host="localhost", port=5010)
