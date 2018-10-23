from flask import Flask, url_for, render_template, g, request, redirect
import os
from flask_sqlalchemy import SQLAlchemy
import models
import populateDB


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://dbbkiputbafcju:3477b7be42046136fa9d2dec76b7b397933f1314dcbf136a64e1d1288185663a@ec2-54-83-29-34.compute-1.amazonaws.com:5432/d78tp1vprns7ma?sslmode=require'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/apms'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

@app.route("/", methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template("auth/login.html")
	error = None
	if request.method == 'POST':
		inputEmail = request.form["InputEmail"]
		actualPassword = models.Account.query.filter_by(email=inputEmail).first()
		if request.form['In`putPassword'] != str(actualPassword):
			error = "Invalid Credentials."
			return render_template('auth/login.html', error=error)
		else:
			return render_template('dashboard.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == "GET":
		return render_template("auth/register.html")
	if request.method == "POST":
		inputCredentials = request.form.to_dict()
		user = models.Account(fullname=inputCredentials["InputName"], email=inputCredentials["InputEmail"], password=inputCredentials["InputPassword"])
		db.session.add(user)
		db.session.commit()
		return redirect(url_for("index"))

@app.route("/dashboard", methods=['GET', 'POST'])
def index():
	if request.method == "GET":
		return render_template("dashboard.html")
	if request.method == "POST":
		if request.form['pop'] == 'popcust':
			populateDB.populateCustomer()
		if request.form['pop'] == 'poprides':
			populateDB.populateRide()
		return render_template('dashboard.html')

if __name__ == '__main__':
	app.run(host="localhost",port=5010, debug=True)
