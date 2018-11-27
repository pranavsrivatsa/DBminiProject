from flask import Flask, url_for, render_template, g, request, redirect, Markup, json
import os
from flask_sqlalchemy import SQLAlchemy
from models import *
import populateDB
import graph

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://dbbkiputbafcju:3477b7be42046136fa9d2dec76b7b397933f1314dcbf136a64e1d1288185663a@ec2-54-83-29-34.compute-1.amazonaws.com:5432/d78tp1vprns7ma?sslmode=require'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/apms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

@app.route("/", methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		inputEmail = request.form["InputEmail"]
		actualPassword = Account.query.filter_by(email=inputEmail).first()
		if request.form['InputPassword'] != str(actualPassword):
			error = "Invalid Credentials."
			return render_template('auth/login.html', error=error)
		else:
			return redirect('/dashboard')
	else:
		return render_template("auth/login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == "POST":
		inputCredentials = request.form.to_dict()
		user = Account(fullname=inputCredentials["InputName"], email=inputCredentials["InputEmail"], password=inputCredentials["InputPassword"])
		db.session.add(user)
		db.session.commit()
		return redirect(url_for("index"))
	else:
		return render_template("auth/register.html")

@app.route("/dashboard", methods=['GET', 'POST'])
def index():
	daystats = day.query.all()
	dayRideRev = dayrev.query.all()
	dayRideCnt = daycount.query.all()
	customerrides = CustomerRidesLink.query.all()
	if request.method == "POST":
	    if request.form['pop'] == 'popcust':
	        populateDB.populateCustomer()
	    if request.form['pop'] == 'startpark':
	        populateDB.populateCustomerRides()
	    if request.form['pop'] == 'stoppark':
		    populateDB.change()
	return render_template("dashboard.html",dayStats=daystats,dayriderev=dayRideRev,dayridecnt=dayRideCnt,customerRides=customerrides)

@app.route("/graphs",methods=['GET'])
def getGraph():
	ageList = graph.getAgeRanges()
	datems,dayrevenue,daycount = graph.getDayStats()
	days = len(datems)
	ridedates,cr,drr,dtr,fwr,gtr,rcr,wrr,ssr,cir,gr = graph.getDayRideRevenue()
	hours = len(ridedates)
	cc,drc,dtc,fwc,gtc,rcc,wrc,ssc,cic,gc = graph.getDayRideCount()
	return render_template("graphs.html",ageRanges=ageList,Days=days,Hours=hours,dates=datems,dayRevenue=dayrevenue,dayCount=daycount,rideDates=ridedates,CR=cr,DRR=drr,DTR=dtr,FWR=fwr,GTR=gtr,RCR=rcr,WRR=wrr,SSR=ssr,CIR=cir,GR=gr,CC=cc,DRC=drc,DTC=dtc,FWC=fwc,GTC=gtc,RCC=rcc,WRC=wrc,SSC=ssc,CIC=cic,GC=gc)


if __name__ == '__main__':
	app.run(host="localhost",port=5010, debug=True)
