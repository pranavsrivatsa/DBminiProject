from flask import Flask, url_for, render_template, g, request, redirect
import os
from flask_sqlalchemy import SQLAlchemy
from models import Accounts


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
		actualPassword = Accounts.query.filter_by(email=inputEmail).first()
		if request.form['InputPassword'] != str(actualPassword):
			error = "Invalid Credentials."
		else:
			return render_template('index.html')
	return render_template('auth/login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == "GET":
		return render_template("auth/register.html")
	if request.method == "POST":
		inputCredentials = request.form.to_dict()
		user = Accounts(fullname=inputCredentials["InputName"], email=inputCredentials["InputEmail"], password=inputCredentials["InputPassword"])
		db.session.add(user)
		db.session.commit()
		return redirect(url_for("index"))

@app.route("/", methods=['GET', 'POST'])
def index():
	return render_template("index.html")

@app.route('/update/<int:Id>', methods=['GET', 'POST'])
def update(Id):
	if request.method == "GET":
		staff = query_db("SELECT * FROM staff WHERE Id=?", [Id], one=True)
		return render_template("update.html", staff=staff)
	if request.method == "POST":
		staff = request.form.to_dict()
		values = [staff["Id"], staff["name"], staff["age"], staff["salary"], staff["work"], Id]
		change_db("UPDATE staff SET Id=?, Name=?, Age=?, Salary=?, Work=? WHERE Id=?", values)
		return redirect(url_for("index"))

@app.route('/delete/<int:Id>', methods=['GET', 'POST'])
def delete(Id):
	if request.method == "GET":
		staff = query_db("SELECT * FROM staff WHERE Id=?", [Id], one=True)
		return render_template("delete.html", staff=staff)
	if request.method == "POST":
		change_db("DELETE FROM staff where Id=?", [Id])
		return redirect(url_for("index"))

if __name__ == '__main__':
	app.run(host="localhost",port=5010, debug=True)
