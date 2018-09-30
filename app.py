from flask import Flask, url_for, render_template, g, request, redirect
import os
import sqlite3


app = Flask(__name__)
DATABASE = "data.db"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def query_db(query, args=(), one=False):
	cur = get_db().execute(query, args)
	rv = cur.fetchall()
	cur.close()
	return (rv[0] if rv else None) if one else rv

def change_db(query,args=()):
    cur = get_db().execute(query, args)
    get_db().commit()
    cur.close()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("/auth/login.html")
    error = None
    if request.method == 'POST':
        username = request.form['username']
        passwordActual = query_db("SELECT password FROM Account WHERE UserName = ? ",[username], one=True)
        if request.form['password'] != str(passwordActual[0]):
            error = "Invalid Credentials."
        else:
            return render_template('index.html')
    return render_template('/auth/login.html', error=error)

@app.route("/index")
def index():
	staff_list = query_db("SELECT * FROM staff")
	return render_template("index.html", staff_list=staff_list)

@app.route('/create', methods=['GET', 'POST'])
def create():
	if request.method == "GET":
		return render_template("create.html",staff=None)
	if request.method == "POST":
		staff = request.form.to_dict()
		values = [staff["Id"], staff["name"], staff["age"], staff["salary"], staff["work"]]
		change_db("INSERT INTO staff (Id, Name, Age, Salary, Work) VALUES (?, ?, ?, ?, ?)", values)
		return redirect(url_for("index"))

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
	app.run(host="0.0.0.0",port=5010, debug=True)
